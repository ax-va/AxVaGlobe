import math

from pyglobe3d.core.geometry.rotation import get_angle_between, get_rotated_vertex
from pyglobe3d.core.icosasphere.any_mesh import AnyMesh


class PartialMesh(AnyMesh):
    def __init__(self, partition: int = 1, radius: float = 1.0):
        AnyMesh.__init__(self, partition, radius)
        self._theta_factor = self.icosahedron.theta / self.logic_mesh.GRID.PARTITION
        self._triangles_offset = self.logic_mesh.GRID.NUMBER_OF_TRIANGLES
        self._add_icosahedron_vertices()

    @property
    def vertex_cash(self):
        return self._vertex_cash

    def add_nodes(self, nodes):
        for node in nodes:
            if node.index not in self._vertex_cash:
                self._add_node(node)
            for neighbor in node.neighboring_nodes:
                if neighbor.index not in self._vertex_cash:
                    self._add_node(neighbor)

    def _add_edge_node(self, edge, node):
        vertex0 = self._vertex_cash[edge.icosahedron_nodes.node0.index]
        vertex1 = self._vertex_cash[edge.icosahedron_nodes.node1.index]
        radians = self._theta_factor * edge.icosahedron_nodes.node0.division_ratios.ratio0
        self._vertex_cash[node.index] = get_rotated_vertex(vertex0, vertex1, radians)

    def _add_edge_nodes(self, edges, nodes):
        for edge, node in zip(edges, nodes):
            if node.index not in self._vertex_cash:
                self._add_edge_node(edge, node)

    def _add_icosahedron_vertices(self):
        icosahedron_vertices = self.icosahedron.vertex_np_array
        icosahedron_nodes_indices = (node.index for node in self.logic_mesh.ICOSAHEDRON_NODES)
        self._vertex_cash = dict(zip(icosahedron_nodes_indices, icosahedron_vertices))

    def _add_node(self, node):
        if node.nearest_layer_edges_number == 2:  # The node is not on an edge
            self._add_edge_nodes(node.nearest_layer_edges, node.nearest_layer_edge_nodes)
            self._add_non_edge_node(node)
        else:  # The node is on an edge: node.nearest_layer_edges_number == 1
            self._add_edge_node(node.nearest_layer_edges.edge0, node)

    def _add_non_edge_node(self, node):
        vertex0 = self._vertex_cash[node.nearest_layer_edge_nodes.node0.index]
        vertex1 = self._vertex_cash[node.nearest_layer_edge_nodes.node1.index]
        radians = (get_angle_between(vertex0, vertex1)
                   / math.fsum(node.division_ratios)
                   * node.division_ratios.ratio0)
        self._vertex_cash[node.index] = get_rotated_vertex(vertex0, vertex1, radians)


if __name__ == '__main__':
    p_msh = PartialMesh(partition=4)
    print(p_msh.vertex_cash)
