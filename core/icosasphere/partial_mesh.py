from pyglobe3d.core.geometry.linear_algebra import change_radius, get_angle_between, get_rotated_vertex, get_midpoint_3
from pyglobe3d.core.icosasphere.any_mesh import AnyMesh


class PartialMesh(AnyMesh):
    def __init__(self, partition: int = 1, radius: float = 1.0):
        AnyMesh.__init__(self, partition, radius)
        self._radius = radius
        self._theta_factor = self.icosahedron.theta / self.logic_mesh.partition
        self._index_offset = self.logic_mesh.GRID.NUMBER_OF_NODES
        self._add_icosahedron_nodes()

    @property
    def vertex_cache(self):
        return self._vertex_cache

    def add_nodes(self, nodes):
        for node in nodes:
            if node.index not in self._vertex_cache:
                self._add_node(node)
            for neighbor in node.neighboring_nodes:
                if neighbor.index not in self._vertex_cache:
                    self._add_node(neighbor)
            for triangle in node.adjacent_triangles:
                if (triangle.index + self._index_offset) not in self._vertex_cache:
                    self._add_triangle_center(triangle)
            ...

    def _add_edge_node(self, edge, node):
        node0, node1 = edge.icosahedron_nodes
        vertex0 = self._vertex_cache[node0.index]
        vertex1 = self._vertex_cache[node1.index]
        radians = self._theta_factor * node0.division_ratios.ratio0
        self._vertex_cache[node.index] = get_rotated_vertex(vertex0, vertex1, radians)

    def _add_edge_nodes(self, edges, nodes):
        for edge, node in zip(edges, nodes):
            if node.index not in self._vertex_cache:
                self._add_edge_node(edge, node)

    def _add_icosahedron_nodes(self):
        icosahedron_vertices = self.icosahedron.vertex_array
        icosahedron_nodes_indices = (node.index for node in self.logic_mesh.ICOSAHEDRON_NODES)
        self._vertex_cache = dict(zip(icosahedron_nodes_indices, icosahedron_vertices))

    def _add_node(self, node):
        if node.nearest_layer_edges_number == 2:  # The node is not on an edge
            self._add_edge_nodes(node.nearest_layer_edges, node.nearest_layer_edge_nodes)
            self._add_non_edge_node(node)
        else:  # The node is on an edge: node.nearest_layer_edges_number == 1
            self._add_edge_node(node.nearest_layer_edges.edge0, node)

    def _add_non_edge_node(self, node):
        node0, node1 = node.nearest_layer_edge_nodes
        vertex0 = self._vertex_cache[node0.index]
        vertex1 = self._vertex_cache[node1.index]
        ratio0, ratio1 = node.division_ratios
        radians = get_angle_between(vertex0, vertex1) * (ratio0 / (ratio0 + ratio1))
        self._vertex_cache[node.index] = get_rotated_vertex(vertex0, vertex1, radians)

    def _add_triangle_center(self, triangle):
        node0, node1, node2 = triangle.triangle_nodes
        vertex0 = self._vertex_cache[node0.index]
        vertex1 = self._vertex_cache[node1.index]
        vertex2 = self._vertex_cache[node2.index]
        triangle_center = get_midpoint_3(vertex0, vertex1, vertex2)
        change_radius(triangle_center, self._radius)
        self._vertex_cache[triangle.index + self._index_offset] = triangle_center


if __name__ == '__main__':
    p_msh = PartialMesh(partition=4)
    print(p_msh.vertex_cache)
