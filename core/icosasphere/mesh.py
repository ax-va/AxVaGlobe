import numpy as np

from pyglobe3d.core.geometry.rotation import get_rotated_vertex
from pyglobe3d.core.icosalogic import Mesh as LogicMesh
from pyglobe3d.core.icosasphere.icosahedron import Icosahedron


class Mesh:
    def __init__(self, partition: int = 1, radius: float = 1.0):
        self._logic_mesh = LogicMesh(partition=partition)
        self._icosahedron = Icosahedron(radius=radius)
        self._cash_icosahedron_vertices()

    def add_nodes(self, nodes):
        for node in nodes:
            if node.index not in self._vertex_cash:
                self._add_edge_nodes(node.nearest_layer_edges, node.nearest_layer_edge_nodes)
                if node.nearest_layer_edges == 2:  # otherwise the node is on an edge and was already cashed
                    vertex0 = self._vertex_cash[node.nearest_layer_edge_nodes.node0.index]
                    vertex1 = self._vertex_cash[node.nearest_layer_edge_nodes.node1.index]
                    radians = ...

    def _add_edge_nodes(self, edges, nodes):
        for edge, node in zip(edges, nodes):
            if node.index not in self._vertex_cash:
                vertex0 = self._vertex_cash[edge.icosahedron_nodes.node0.index]
                vertex1 = self._vertex_cash[edge.icosahedron_nodes.node1.index]
                radians = self._icosahedron.theta / self._logic_mesh.GRID.PARTITION * ...
                self._vertex_cash[node.index] = get_rotated_vertex(vertex0, vertex1, radians)
    
    def _cash_icosahedron_vertices(self):
        icosahedron_vertices = self._icosahedron.vertex_np_array
        icosahedron_nodes_indices = (node.index for node in self._logic_mesh.ICOSAHEDRON_NODES)
        self._vertex_cash = dict(zip(icosahedron_nodes_indices, icosahedron_vertices))


if __name__ == '__main__':
    msh = Mesh(partition=4)
    print(msh._vertex_cash)

