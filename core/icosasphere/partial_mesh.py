from pyglobe3d.core.geometry.vertex import \
    change_vertex_radius, get_angle_between, get_rotated_vertex, get_triangle_midpoint_vertex
from pyglobe3d.core.icosasphere.any_mesh import AnyMesh


class PartialMesh(AnyMesh):
    def __init__(self, partition: int = 1, radius: float = 1.0):
        AnyMesh.__init__(self, partition, radius)
        self._add_icosahedron_nodes()
        self._vertex_indices = set()

    @property
    def vertex_indices(self) -> set:
        return self._vertex_indices

    @property
    def vertices(self) -> dict:
        return self._vertices

    def add_nodes_with_indices(self, node_indices):
        for node_index in node_indices:
            node = self.logic_mesh.create_node(index=node_index)
            if node_index not in self._vertices:
                self._add_node(node)
            self._add_node_neighbors(node)
            self._add_triangle_midpoints(node)
            self._add_vertex_indices(node)

    def _add_edge_node(self, edge, node):
        vertex0 = self._vertices[edge.icosahedron_nodes.node0.index]
        vertex1 = self._vertices[edge.icosahedron_nodes.node1.index]
        radians = self._theta_factor * edge.icosahedron_nodes.division_ratios.ratio0
        self._vertices[node.index] = get_rotated_vertex(vertex0, vertex1, radians)

    def _add_edge_nodes(self, edges, nodes):
        for edge, node in zip(edges, nodes):
            if node.index not in self._vertices:
                self._add_edge_node(edge, node)

    def _add_icosahedron_nodes(self):
        icosahedron_vertices = self.icosahedron.vertex_array
        icosahedron_nodes_indices = (node.index for node in self.logic_mesh.ICOSAHEDRON_NODES)
        self._vertices = dict(zip(icosahedron_nodes_indices, icosahedron_vertices))

    def _add_node(self, node):
        if node.nearest_layer_edges_number == 2:  # The node is not on an edge
            self._add_edge_nodes(node.nearest_layer_edges, node.nearest_layer_edge_nodes)
            self._add_non_edge_node(node)
        else:  # The node is on an edge: node.nearest_layer_edges_number == 1
            self._add_edge_node(node.nearest_layer_edges.edge0, node)

    def _add_node_neighbors(self, node):
        for neighbor in node.neighboring_nodes:
            if neighbor.index not in self._vertices:
                self._add_node(neighbor)

    def _add_non_edge_node(self, node):
        vertex0 = self._vertices[node.nearest_layer_edge_nodes.node0.index]
        vertex1 = self._vertices[node.nearest_layer_edge_nodes.node1.index]
        ratio0, ratio1 = node.division_ratios
        radians = get_angle_between(vertex0, vertex1) * (ratio0 / (ratio0 + ratio1))
        self._vertices[node.index] = get_rotated_vertex(vertex0, vertex1, radians)

    def _add_triangle_midpoint(self, triangle):
        vertex0 = self._vertices[triangle.triangle_nodes.node0.index]
        vertex1 = self._vertices[triangle.triangle_nodes.node1.index]
        vertex2 = self._vertices[triangle.triangle_nodes.node2.index]
        triangle_midpoint_vertex = get_triangle_midpoint_vertex(vertex0, vertex1, vertex2)
        change_vertex_radius(triangle_midpoint_vertex, self.radius)
        self._vertices[triangle.index + self._index_offset] = triangle_midpoint_vertex

    def _add_triangle_midpoints(self, node):
        for triangle in node.adjacent_triangles:
            if (triangle.index + self._index_offset) not in self._vertices:
                self._add_triangle_midpoint(triangle)

    def _add_vertex_indices(self, node):
        last = node.adjacent_triangles_number - 1
        for i in range(last):
            self._vertex_indices.add(
                (node.adjacent_triangles[i + 1].index + self._index_offset,
                 node.adjacent_triangles[i].index + self._index_offset,
                 node.index)
            )
        self._vertex_indices.add(
            (node.adjacent_triangles[0].index + self._index_offset,
             node.adjacent_triangles[last].index + self._index_offset,
             node.index)
        )


if __name__ == '__main__':
    p_msh = PartialMesh(partition=4)
    print(p_msh.vertices)
    s = set()
    s.add((1, 2, 3))
