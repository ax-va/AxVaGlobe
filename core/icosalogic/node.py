from pyglobe3d.core.icosalogic.elements import ElementWithIndexAndLocationObjects
from pyglobe3d.core.icosalogic.node_attrs import NodeIndex, NodeLocation


class Node(ElementWithIndexAndLocationObjects):
    """
    Describes a logical node located on the icosahedron.

    """
    def __init__(self,
                 index_object: NodeIndex = None,
                 location_object: NodeLocation = None
                 ):
        ElementWithIndexAndLocationObjects._set_attributes(self, index_object, location_object)
        self._adjacent_triangles = None
        self._nearest_layer_edge_nodes = None
        self._nearest_layer_edges = None
        self._nearest_layer_edges_number = None
        self._neighboring_nodes = None
        self._neighboring_nodes_number = None
        self._node_neighbors_object = None

    @property
    def adjacent_triangles(self):
        if not self._node_neighbors_object:
            self._set_node_neighbors_object()
        return self._adjacent_triangles

    @property
    def nearest_layer_edge_nodes(self):
        if not self._node_neighbors_object:
            self._set_node_neighbors_object()
        return self._nearest_layer_edge_nodes
    
    @property
    def nearest_layer_edges(self):
        if not self._node_neighbors_object:
            self._set_node_neighbors_object()
        return self._nearest_layer_edges
    
    @property
    def nearest_layer_edges_number(self):
        if not self._nearest_layer_edges_number:
            self._set_node_neighbors_object()
        return self._nearest_layer_edges_number

    @property
    def neighboring_nodes(self):
        if not self._node_neighbors_object:
            self._set_node_neighbors_object()
        return self._neighboring_nodes
    
    @property
    def neighboring_nodes_number(self):
        if not self._neighboring_nodes_number:
            self._set_node_neighbors_object()
        return self._neighboring_nodes_number

    def _set_node_neighbors_object(self):
        from pyglobe3d.core.icosalogic.node_neighbors import NodeNeighbors
        self._node_neighbors_object = NodeNeighbors(base_node=self)
        self._adjacent_triangles = self._node_neighbors_object.adjacent_triangles
        self._nearest_layer_edge_nodes = self._node_neighbors_object.nearest_layer_edge_nodes
        self._nearest_layer_edges = self._node_neighbors_object.nearest_layer_edges
        self._nearest_layer_edges_number = self._node_neighbors_object.nearest_edges_number
        self._neighboring_nodes = self._node_neighbors_object.neighboring_nodes
        self._neighboring_nodes_number = self._node_neighbors_object.neighboring_nodes_number


if __name__ == '__main__':
    from pyglobe3d.core.icosalogic.grid_consts import Grid
    node31 = Node(NodeIndex(grid=Grid(partition=4), index=31))
    for nd in node31.neighboring_nodes:
        # print(nd.index)
        print(nd)
    print('-' * 10)
    node32 = Node(NodeIndex(grid=Grid(partition=4), index=32))
    for nd in node32.neighboring_nodes:
        print(nd.index)
        # print(nd)

    node0 = Node()
    print(node0, node0.grid, node0.index, node0.layer, node0.position_in_layer)
    print(node32 == node31)

    for tr in node31.adjacent_triangles:
        # print(tr.index)
        print(tr)
    print('-' * 10)
    for tr in node32.adjacent_triangles:
        print(tr.index)
        # print(tr)

    print('/'*10)
    print(node31.neighboring_nodes.node0)
    print(node31.adjacent_triangles.triangle0)
    print(node31.nearest_layer_edges.edge0)
    print(node31.nearest_layer_edge_nodes.node0)
    print(node31.neighboring_nodes_number)
    print(node31.nearest_layer_edges_number)

    node161 = Node(NodeIndex(grid=Grid(partition=4), index=161))
    # node162 = Node(NodeIndex(grid=Grid(partition=4), index=162))

    chuck = 'Chuck'
    print(f'Hello {chuck!r}')


