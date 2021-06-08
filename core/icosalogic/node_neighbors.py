from collections import namedtuple

from pyglobe3d.core.icosalogic.edge import Edge
from pyglobe3d.core.icosalogic.node import Node
from pyglobe3d.core.icosalogic.node_attrs import NodeLocation
from pyglobe3d.core.icosalogic.triangle import Triangle
from pyglobe3d.core.icosalogic.triangle_attrs import TriangleLocation


class NodeNeighbors:
    def __init__(self, base_node: Node = Node()):
        self._base_node = base_node
        self._grid = base_node.grid
        self._layer = base_node.layer
        self._layer_up = self._layer - 1
        self._layer_down = self._layer + 1
        self._position_in_layer = base_node.position_in_layer
        self._node_layers = [None] * 6
        self._node_positions_in_layers = [None] * 6
        self._nodes_number = None
        self._neighboring_nodes = None
        self._triangle_layers = [None] * 6
        self._triangle_positions_in_layers = [None] * 6
        self._triangles_defined = None
        self._triangles_number = None
        self._adjacent_triangles = None
        self._edge_indices = [None, None]
        self._edge_node_layers = [None, None]
        self._edge_node_positions_in_layers = [None, None]
        self._edges_number = None
        self._nearest_layer_edges = None
        self._nearest_layer_edge_nodes = None

    @property
    def base_node(self):
        return self._base_node
    
    @property
    def adjacent_triangles(self):
        if not self._adjacent_triangles:
            self._set_adjacent_triangles()
        return self._adjacent_triangles

    @property
    def nearest_layer_edges(self):
        if not self._nearest_layer_edges:
            self._set_nearest_layer_edges_and_edge_nodes()
        return self._nearest_layer_edges

    @property
    def nearest_layer_edge_nodes(self):
        if not self._nearest_layer_edge_nodes:
            self._set_nearest_layer_edges_and_edge_nodes()
        return self._nearest_layer_edge_nodes

    @property
    def neighboring_nodes(self):
        if not self._neighboring_nodes:
            self._set_neighboring_nodes()
        return self._neighboring_nodes

    @property
    def adjacent_triangles_number(self):
        return self._triangles_number

    @property
    def nearest_edges_number(self):
        return self._edges_number

    @property
    def neighboring_nodes_number(self):
        return self._nodes_number

    def _set_adjacent_triangles(self):
        if NodeLocation.is_layer_in_part2_excluding_borders(self._grid, self._layer):
            self._set_adjacent_triangles_in_part2_excluding_borders()

        elif NodeLocation.is_layer_in_part1_excluding_pole(self._grid, self._layer):
            self._set_adjacent_triangles_in_part1_excluding_pole()

        elif NodeLocation.is_layer_in_part3_excluding_pole(self._grid, self._layer):
            self._set_adjacent_triangles_in_part3_excluding_pole()

        elif NodeLocation.is_layer_in_part2_north_border(self._grid, self._layer):
            self._set_adjacent_triangles_in_part2_north_border()

        elif NodeLocation.is_layer_in_part2_south_border(self._grid, self._layer):
            self._set_adjacent_triangles_in_part2_south_border()

        elif NodeLocation.is_layer_in_part1_pole(self._layer):
            self._set_adjacent_triangles_in_part1_pole()

        else:  # The the part-3-pole case
            self._set_adjacent_triangles_in_part3_pole()

        triangle_names = [f'triangle{i}' for i in range(0, self._triangles_number)]
        Result = namedtuple('Triangles', triangle_names)
        self._adjacent_triangles = Result(
            *(
                Triangle(
                    location_object=TriangleLocation(
                        grid=self._grid,
                        layer=self._triangle_layers[i],
                        position_in_layer=self._triangle_positions_in_layers[i]
                    )
                ) for i in range(0, self._triangles_number)
            )
        )

    def _set_adjacent_triangles_in_part1_excluding_pole(self):
        self._triangles_number = 6
        # This is the number of triangles in the 1/5 (i.e. sublayer) of the upper layer:
        t1 = self._layer_up + self._layer_up + 1
        # This is the number of triangles in the 1/5 (i.e. sublayer) of the layer
        t2 = self._layer + self._layer + 1
        n = self._position_in_layer // self._layer
        # This is the increment of n * t1 or n * t2 due to completed sublayers excluding the current sublayer
        k = self._position_in_layer % self._layer

        self._triangle_layers[0] = self._layer_up
        self._triangle_layers[1] = self._layer_up
        self._triangle_layers[3] = self._layer
        self._triangle_layers[4] = self._layer
        self._triangle_layers[5] = self._layer

        if k != 0:  # Adjacent triangles are of the form 3/3
            # The node is not on the edge
            self._triangle_layers[2] = self._layer_up
            self._triangle_positions_in_layers[0] = n * t1 + (k - 1) * 2
            self._triangle_positions_in_layers[1] = self._triangle_positions_in_layers[0] + 1
            self._triangle_positions_in_layers[2] = self._triangle_positions_in_layers[0] + 2
            self._triangle_positions_in_layers[3] = n * t2 + (k - 1) * 2 + 3
            self._triangle_positions_in_layers[4] = self._triangle_positions_in_layers[3] - 1
            self._triangle_positions_in_layers[5] = self._triangle_positions_in_layers[3] - 2
        else:  # Adjacent triangles are of the form 2/4
            # The node is on the edge
            self._triangle_layers[2] = self._layer
            if self._position_in_layer != 0:
                self._triangle_positions_in_layers[1] = n * t1
                self._triangle_positions_in_layers[0] = self._triangle_positions_in_layers[1] - 1
                self._triangle_positions_in_layers[3] = n * t2
                self._triangle_positions_in_layers[2] = self._triangle_positions_in_layers[3] + 1
                self._triangle_positions_in_layers[4] = self._triangle_positions_in_layers[3] - 1
                self._triangle_positions_in_layers[5] = self._triangle_positions_in_layers[3] - 2
            else:  # Take into account cyclicity
                # The node is on the last edge
                self._triangle_positions_in_layers[0] = t1 * 5 - 1
                self._triangle_positions_in_layers[1] = 0
                self._triangle_positions_in_layers[5] = t2 * 5 - 2
                self._triangle_positions_in_layers[4] = self._triangle_positions_in_layers[5] + 1
                self._triangle_positions_in_layers[3] = 0
                self._triangle_positions_in_layers[2] = 1

    def _set_adjacent_triangles_in_part1_pole(self):
        self._triangles_number = 5
        self._triangle_layers[0] = 0
        self._triangle_positions_in_layers[0]=0
        self._triangle_layers[1] = 0
        self._triangle_positions_in_layers[1] = 1
        self._triangle_layers[2] = 0
        self._triangle_positions_in_layers[2] = 2
        self._triangle_layers[3] = 0
        self._triangle_positions_in_layers[3] = 3
        self._triangle_layers[4] = 0
        self._triangle_positions_in_layers[4] = 4

    def _set_adjacent_triangles_in_part2_excluding_borders(self):
        self._triangles_number = 6
        # All adjacent triangles are of the form 3/3
        self._triangle_layers[0] = self._layer_up
        self._triangle_layers[1] = self._layer_up
        self._triangle_layers[2] = self._layer_up
        self._triangle_layers[3] = self._layer
        self._triangle_layers[4] = self._layer
        self._triangle_layers[5] = self._layer

        if self._position_in_layer != 0:
            self._triangle_positions_in_layers[0] = (self._position_in_layer - 1) * 2
            self._triangle_positions_in_layers[1] = self._triangle_positions_in_layers[0] + 1
            self._triangle_positions_in_layers[2] = self._triangle_positions_in_layers[0] + 2
            self._triangle_positions_in_layers[4] = self._triangle_positions_in_layers[2]
            self._triangle_positions_in_layers[5] = self._triangle_positions_in_layers[1]
            self._triangle_positions_in_layers[3] = self._triangle_positions_in_layers[2] + 1
        else:  # Take into account cyclicity
            self._triangle_positions_in_layers[0] = self._grid.LAST_NODE_POSITION_IN_LAYER_IN_PART2 * 2
            self._triangle_positions_in_layers[1] = self._triangle_positions_in_layers[0] + 1
            self._triangle_positions_in_layers[2] = 0
            self._triangle_positions_in_layers[3] = 1
            self._triangle_positions_in_layers[4] = 0
            self._triangle_positions_in_layers[5] = self._triangle_positions_in_layers[1]

    def _set_adjacent_triangles_in_part2_north_border(self):
        # This is the number of triangles in the 1/5 (i.e. sublayer) of the upper layer:
        t1 = self._layer_up + self._layer_up + 1
        # This is the number of triangles in 2 neighboring sublayers
        t2 = self._grid.PARTITION_X2
        n = self._position_in_layer // self._layer
        k = self._position_in_layer % self._layer

        self._triangle_layers[0] = self._layer_up
        self._triangle_layers[1] = self._layer_up
        self._triangle_layers[3] = self._layer
        self._triangle_layers[4] = self._layer

        if k != 0:  # 6 adjacent triangles are of the form 3/3
            self._triangles_number = 6
            self._triangle_layers[2] = self._layer_up
            self._triangle_layers[5] = self._layer

            self._triangle_positions_in_layers[0] = n * t1 + (k - 1) * 2
            self._triangle_positions_in_layers[1] = self._triangle_positions_in_layers[0] + 1
            self._triangle_positions_in_layers[2] = self._triangle_positions_in_layers[0] + 2
            self._triangle_positions_in_layers[5] = n * t2 + (k - 1) * 2 + 1
            self._triangle_positions_in_layers[4] = self._triangle_positions_in_layers[5] + 1
            self._triangle_positions_in_layers[3] = self._triangle_positions_in_layers[5] + 2
        else:  # 5 # Adjacent triangles are of the form 2/3
            self._triangles_number = 5
            self._triangle_layers[2] = self._layer
            if self._position_in_layer != 0:
                self._triangle_positions_in_layers[1] = n * t1
                self._triangle_positions_in_layers[0] = self._triangle_positions_in_layers[1] - 1
                self._triangle_positions_in_layers[3] = n * t2
                self._triangle_positions_in_layers[4] = self._triangle_positions_in_layers[3] - 1
                self._triangle_positions_in_layers[2] = self._triangle_positions_in_layers[3] + 1
            else:  # Take into account cyclicity
                self._triangle_positions_in_layers[0] = t1 * 5 - 1
                self._triangle_positions_in_layers[1] = 0
                self._triangle_positions_in_layers[4] = t2 * 5 - 1
                self._triangle_positions_in_layers[2] = 1
                self._triangle_positions_in_layers[3] = 0

    def _set_adjacent_triangles_in_part2_south_border(self):
        t1 = self._grid.PARTITION_X2
        k2 = self._grid.PARTITION_X3 - self._layer
        t2 = k2 * 2 - 1
        n = self._position_in_layer // k2
        k = self._position_in_layer % k2

        self._triangle_layers[0] = self._layer_up
        self._triangle_layers[1] = self._layer_up
        self._triangle_layers[2] = self._layer_up
        self._triangle_layers[3] = self._layer
        self._triangle_layers[4] = self._layer

        if k != 0:  # 6 adjacent triangles are of the form 3/3
            self._triangles_number = 6
            self._triangle_layers[5] = self._layer

            self._triangle_positions_in_layers[0] = n * t1 + (k - 1) * 2
            self._triangle_positions_in_layers[1] = self._triangle_positions_in_layers[0] + 1
            self._triangle_positions_in_layers[2] = self._triangle_positions_in_layers[0] + 2
            self._triangle_positions_in_layers[5] = n * t2 + (k - 1) * 2
            self._triangle_positions_in_layers[4] = self._triangle_positions_in_layers[5] + 1
            self._triangle_positions_in_layers[3] = self._triangle_positions_in_layers[5] + 2
        else:  # 5 adjacent triangles are of the form 2/3
            self._triangles_number = 5
            if self._position_in_layer != 0:
                self._triangle_positions_in_layers[2] = n * t1
                self._triangle_positions_in_layers[1] = self._triangle_positions_in_layers[2] - 1
                self._triangle_positions_in_layers[0] = self._triangle_positions_in_layers[2] - 2
                self._triangle_positions_in_layers[3] = n * t2
                self._triangle_positions_in_layers[4] = self._triangle_positions_in_layers[3] - 1
            else:  # Take into account cyclicity
                self._triangle_positions_in_layers[0] = t1 * 5 - 2
                self._triangle_positions_in_layers[1] = self._triangle_positions_in_layers[0] + 1
                self._triangle_positions_in_layers[2] = 0
                self._triangle_positions_in_layers[4] = t2 * 5 - 1
                self._triangle_positions_in_layers[3] = 0

    def _set_adjacent_triangles_in_part3_excluding_pole(self):
        self._triangles_number = 6
        t1 = (self._grid.LAST_TRIANGLE_LAYER - self._layer_up) * 2 + 1
        t2 = (self._grid.LAST_TRIANGLE_LAYER - self._layer) * 2 + 1
        n = self._position_in_layer // (self._grid.PARTITION_X3 - self._layer)
        k = self._position_in_layer % (self._grid.PARTITION_X3 - self._layer)

        self._triangle_layers[0] = self._layer_up
        self._triangle_layers[1] = self._layer_up
        self._triangle_layers[2] = self._layer_up
        self._triangle_layers[3] = self._layer
        self._triangle_layers[4] = self._layer

        if k != 0:  # Adjacent triangles are of the form 3/3
            self._triangle_layers[5] = self._layer

            self._triangle_positions_in_layers[0] = n * t1 + (k - 1) * 2 + 1
            self._triangle_positions_in_layers[1] = self._triangle_positions_in_layers[0] + 1
            self._triangle_positions_in_layers[2] = self._triangle_positions_in_layers[0] + 2
            self._triangle_positions_in_layers[3] = n * t2 + (k - 1) * 2 + 2
            self._triangle_positions_in_layers[4] = self._triangle_positions_in_layers[3] - 1
            self._triangle_positions_in_layers[5] = self._triangle_positions_in_layers[3] - 2
        else:  # Adjacent triangles are of the form 4/2
            self._triangle_layers[5] = self._layer_up

            if self._position_in_layer != 0:
                self._triangle_positions_in_layers[1] = n * t1
                self._triangle_positions_in_layers[0] = self._triangle_positions_in_layers[1] - 1
                self._triangle_positions_in_layers[5] = self._triangle_positions_in_layers[1] - 2
                self._triangle_positions_in_layers[2] = self._triangle_positions_in_layers[1] + 1
                self._triangle_positions_in_layers[3] = n * t2
                self._triangle_positions_in_layers[4] = self._triangle_positions_in_layers[3] - 1
            else:
                self._triangle_positions_in_layers[5] = t1 * 5 - 2
                self._triangle_positions_in_layers[0] = self._triangle_positions_in_layers[5] + 1
                self._triangle_positions_in_layers[1] = 0
                self._triangle_positions_in_layers[2] = 1
                self._triangle_positions_in_layers[3] = 0
                self._triangle_positions_in_layers[4] = t2 * 5 - 1

    def _set_adjacent_triangles_in_part3_pole(self):
        self._triangles_number = 5
        self._triangle_layers[0] = self._grid.LAST_TRIANGLE_LAYER
        self._triangle_positions_in_layers[0] = 0
        self._triangle_layers[1] = self._grid.LAST_TRIANGLE_LAYER
        self._triangle_positions_in_layers[1] = 1
        self._triangle_layers[2] = self._grid.LAST_TRIANGLE_LAYER
        self._triangle_positions_in_layers[2] = 2
        self._triangle_layers[3] = self._grid.LAST_TRIANGLE_LAYER
        self._triangle_positions_in_layers[3] = 3
        self._triangle_layers[4] = self._grid.LAST_TRIANGLE_LAYER
        self._triangle_positions_in_layers[4] = 4

    def _set_nearest_layer_edges_and_edge_nodes(self):
        if NodeLocation.is_layer_in_part2(self._grid, self._layer):
            self._set_nearest_layer_edges_and_edge_nodes_in_part2()
        elif NodeLocation.is_layer_in_part1(self._grid, self._layer):
            self._set_nearest_layer_edges_and_edge_nodes_in_part1()
        else:
            self._set_nearest_layer_edges_and_edge_nodes_in_part3()

        edge_names = [f'edge{i}' for i in range(0, self._edges_number)]
        Result = namedtuple('Edges', edge_names)
        self._nearest_layer_edges = Result(
            *(
                Edge(
                    grid=self._grid,
                    index=self._edge_indices[i]
                ) for i in range(0, self._edges_number)
            )
        )
        node_names = [f'node{i}' for i in range(0, self._edges_number)]
        Result = namedtuple('Nodes', node_names)
        self._nearest_layer_edge_nodes = Result(
            *(
                Node(
                    location_object=NodeLocation(
                        grid=self._grid,
                        layer=self._edge_node_layers[i],
                        position_in_layer=self._edge_node_positions_in_layers[i]
                    )
                ) for i in range(0, self._edges_number)
            )
        )

    def _set_nearest_layer_edges_and_edge_nodes_in_part1(self):
        self._edge_node_layers[0] = self._layer
        if self._layer != 0:  # This is not the north-pole case
            self._edge_indices[0] = self._position_in_layer // self._layer
            if self._position_in_layer % self._layer != 0:  # The node is not the edge node
                self._edges_number = 2
                self._edge_node_layers[1] = self._layer
                self._edge_node_positions_in_layers[0] = self._edge_indices[0] * self._layer
                self._edge_indices[1] = self._edge_indices[0] + 1
                self._edge_node_positions_in_layers[1] = self._edge_node_positions_in_layers[0] + self._layer
                if self._edge_indices[1] >= 5:  # Take into account cyclicity
                    self._edge_indices[1] = 0
                    self._edge_node_positions_in_layers[1] = 0
            else:  # The node itself is the edge node
                self._edges_number = 1
                self._edge_node_positions_in_layers[0] = self._position_in_layer
        else:  # This is the north-pole case
            self._edges_number = 1
            self._edge_indices[0] = 0
            self._edge_node_positions_in_layers[0] = self._position_in_layer

    def _set_nearest_layer_edges_and_edge_nodes_in_part2(self):
        n = self._position_in_layer // self._grid.PARTITION
        if self._layer != self._grid.FIRST_NODE_LAYER_IN_PART2:
            if self._layer != self._grid.LAST_NODE_LAYER_IN_PART2:
                self._edge_node_layers[0] = self._layer
                relative_layer = self._layer - self._grid.LAST_NODE_LAYER_IN_PART1
                nn = n * self._grid.PARTITION
                k = self._position_in_layer % self._grid.PARTITION
                if k != 0 and k != relative_layer:  # The node is not the edge node
                    self._edges_number = 2
                    self._edge_node_layers[1] = self._layer
                    if k < relative_layer:  # The node is in the first part of 2 neighboring sublayers
                        self._edge_indices[0] = 10 + n * 2
                        self._edge_node_positions_in_layers[0] = nn
                        self._edge_node_positions_in_layers[1] = self._edge_node_positions_in_layers[0] + relative_layer
                    else:  # The node is in the second part of 2 neighboring sublayers
                        self._edge_indices[0] = 11 + n * 2
                        self._edge_node_positions_in_layers[0] = nn + relative_layer
                        self._edge_node_positions_in_layers[1] = nn + self._grid.PARTITION
                    self._edge_indices[1] = self._edge_indices[0] + 1
                    if self._edge_node_positions_in_layers[1] >= self._grid.PARTITION_X5:  # Take into account cyclicity
                        self._edge_indices[1] = 10
                        self._edge_node_positions_in_layers[1] = 0
                else:  # The node itself is the edge node
                    self._edges_number = 1
                    if k == 0:  # The nose is on the edge '/'
                        self._edge_indices[0] = 10 + n * 2
                    else:  # The case: k == relative_layer.  The node is on the edge '\'
                        self._edge_indices[0] = 11 + n * 2
                    self._edge_node_positions_in_layers[0] = self._position_in_layer
            else:  # The node is on the horizontal edge with self._grid.LAST_NODE_LAYER_IN_PART2
                self._edges_number = 1
                self._edge_indices[0] = 20 + n
                self._edge_node_layers[0] = self._layer
                self._edge_node_positions_in_layers[0] = self._position_in_layer
        else:  # The node is on the horizontal edge with self._grid.FIRST_NODE_LAYER_IN_PART2
            self._edges_number = 1
            self._edge_indices[0] = 5 + n
            self._edge_node_layers[0] = self._layer
            self._edge_node_positions_in_layers[0] = self._position_in_layer

    def _set_nearest_layer_edges_and_edge_nodes_in_part3(self):
        self._edge_node_layers[0] = self._layer
        reverse_layer = self._grid.LAST_NODE_LAYER - self._layer
        if reverse_layer != 0:  # The node is not the south pole
            n = self._position_in_layer // reverse_layer
            self._edge_indices[0] = n + 25
            if self._position_in_layer % reverse_layer != 0:  # The node is not the edge node
                self._edges_number = 2
                self._edge_node_layers[1] = self._layer
                self._edge_node_positions_in_layers[0] = n * reverse_layer
                self._edge_indices[1] = self._edge_indices[0] + 1
                self._edge_node_positions_in_layers[1] = self._edge_node_positions_in_layers[0] + reverse_layer
                if self._edge_indices[1] >= 30:  # Take into account cyclicality
                    self._edge_indices[1] = 25
                    self._edge_node_positions_in_layers[1] = 0
            else:  # The node itself is the edge node
                self._edges_number = 1
                self._edge_node_positions_in_layers[0] = self._position_in_layer
        else:  # The node is the south-pole node
            self._edges_number = 1
            self._edge_indices[0] = 25
            self._edge_node_positions_in_layers[0] = self._position_in_layer

    def _set_neighboring_nodes(self):
        if NodeLocation.is_layer_in_part2_excluding_borders(self._grid, self._layer):
            self._set_neighboring_nodes_in_part2_excluding_borders()

        elif NodeLocation.is_layer_in_part1_excluding_pole(self._grid, self._layer):
            self._set_neighboring_nodes_in_part1_excluding_pole()

        elif NodeLocation.is_layer_in_part3_excluding_pole(self._grid, self._layer):
            self._set_neighboring_nodes_in_part3_excluding_pole()

        elif NodeLocation.is_layer_in_part2_north_border(self._grid, self._layer):
            self._set_neighboring_nodes_in_part2_north_border()

        elif NodeLocation.is_layer_in_part2_south_border(self._grid, self._layer):
            self._set_neighboring_nodes_in_part2_south_border()

        elif NodeLocation.is_layer_in_part1_pole(self._layer):
            self._set_neighboring_nodes_in_part1_pole()

        else:  # The part-3-pole case
            self._set_neighboring_nodes_in_part3_pole()

        node_names = [f'node{i}' for i in range(0, self._nodes_number)]
        Result = namedtuple('Nodes', node_names)
        self._neighboring_nodes = Result(
            *(
                Node(
                    location_object=NodeLocation(
                        grid=self._grid,
                        layer=self._node_layers[i],
                        position_in_layer=self._node_positions_in_layers[i]
                    )
                ) for i in range(0, self._nodes_number)
            )
        )

    def _set_neighboring_nodes_in_part1_excluding_pole(self):
        self._nodes_number = 6
        n = self._position_in_layer // self._layer
        k = self._position_in_layer % self._layer

        self._node_layers[0] = self._layer_up
        self._node_layers[3] = self._layer_down
        self._node_layers[4] = self._layer_down
        self._node_layers[5] = self._layer

        if k != 0:  # The node is not on the edge of the icosahedron
            self._node_layers[1] = self._layer_up
            self._node_layers[2] = self._layer

            self._node_positions_in_layers[4] = self._position_in_layer + n
            self._node_positions_in_layers[5] = self._position_in_layer - 1
            self._node_positions_in_layers[0] = self._node_positions_in_layers[5] - n
            self._node_positions_in_layers[3] = self._node_positions_in_layers[4] + 1

            if self._position_in_layer < self._layer * 5 - 1:
                self._node_positions_in_layers[1] = self._position_in_layer - n
                self._node_positions_in_layers[2] = self._position_in_layer + 1
            else:  # Two nodes are on the first (also the last) edge
                self._node_positions_in_layers[1] = 0
                self._node_positions_in_layers[2] = 0
        else:  # The node is on the edge of the icosahedron
            self._node_layers[1] = self._layer
            self._node_layers[2] = self._layer_down

            if self._position_in_layer != 0:  # The node is not on the first (also the last) edge
                self._node_positions_in_layers[3] = self._position_in_layer + n
                self._node_positions_in_layers[2] = self._node_positions_in_layers[3] + 1
                self._node_positions_in_layers[4] = self._node_positions_in_layers[3] - 1
                self._node_positions_in_layers[0] = self._position_in_layer - n
                if self._layer != 1 or self._position_in_layer != 4:
                    self._node_positions_in_layers[1] = self._position_in_layer + 1
                else:
                    # A special case when the right neighboring node with the same layer is on the first (last) edge
                    self._node_positions_in_layers[1] = 0
                self._node_positions_in_layers[5] = self._position_in_layer - 1
            else:  # The node is on the first (also the last) edge
                self._node_positions_in_layers[0] = 0
                self._node_positions_in_layers[1] = 1
                self._node_positions_in_layers[2] = 1
                self._node_positions_in_layers[3] = 0
                self._node_positions_in_layers[4] = self._layer_down * 5 - 1
                self._node_positions_in_layers[5] = self._layer * 5 - 1

    def _set_neighboring_nodes_in_part1_pole(self):
        self._nodes_number = 5
        self._node_layers[0] = 1
        self._node_positions_in_layers[0] = 0
        self._node_layers[1] = 1
        self._node_positions_in_layers[1] = 1
        self._node_layers[2] = 1
        self._node_positions_in_layers[2] = 2
        self._node_layers[3] = 1
        self._node_positions_in_layers[3] = 3
        self._node_layers[4] = 1
        self._node_positions_in_layers[4] = 4

    def _set_neighboring_nodes_in_part2_excluding_borders(self):
        self._nodes_number = 6
        self._node_layers[0] = self._layer_up
        self._node_layers[1] = self._layer_up
        self._node_layers[2] = self._layer
        self._node_layers[3] = self._layer_down
        self._node_layers[4] = self._layer_down
        self._node_layers[5] = self._layer

        if self._position_in_layer != 0:  # The node is not on the last edge
            self._node_positions_in_layers[0] = self._position_in_layer - 1
            self._node_positions_in_layers[1] = self._position_in_layer
            self._node_positions_in_layers[4] = self._position_in_layer
            self._node_positions_in_layers[5] = self._node_positions_in_layers[0]
            # The node is not in front of the last edge
            if self._position_in_layer < self._grid.LAST_NODE_POSITION_IN_LAYER_IN_PART2:
                self._node_positions_in_layers[2] = self._position_in_layer + 1
                self._node_positions_in_layers[3] = self._node_positions_in_layers[2]
            else:  # The node is in front of the last edge
                self._node_positions_in_layers[2] = 0
                self._node_positions_in_layers[3] = 0
        else:  # The node is on the last edge
            self._node_positions_in_layers[0] = self._grid.LAST_NODE_POSITION_IN_LAYER_IN_PART2
            self._node_positions_in_layers[1] = 0
            self._node_positions_in_layers[2] = 1
            self._node_positions_in_layers[3] = 1
            self._node_positions_in_layers[4] = 0
            self._node_positions_in_layers[5] = self._node_positions_in_layers[0]

    def _set_neighboring_nodes_in_part2_north_border(self):
        n = self._position_in_layer // self._layer
        k = self._position_in_layer % self._layer

        self._node_layers[0] = self._layer_up
        self._node_layers[3] = self._layer_down

        if k != 0:  # The node is not on the edge of the icosahedron
            self._nodes_number = 6
            self._node_layers[1] = self._layer_up
            self._node_layers[2] = self._layer
            self._node_layers[4] = self._layer_down
            self._node_layers[5] = self._layer

            self._node_positions_in_layers[5] = self._position_in_layer - 1
            self._node_positions_in_layers[0] = self._node_positions_in_layers[5] - n
            self._node_positions_in_layers[4] = self._position_in_layer
            if self._position_in_layer < self._layer * 5 - 1:
                self._node_positions_in_layers[1] = self._position_in_layer - n
                self._node_positions_in_layers[2] = self._position_in_layer + 1
                self._node_positions_in_layers[3] = self._node_positions_in_layers[2]
            else:  # Three nodes are on the last edge
                self._node_positions_in_layers[1] = 0
                self._node_positions_in_layers[2] = 0
                self._node_positions_in_layers[3] = 0
        else:  # The node is on the edge of the icosahedron
            self._nodes_number = 5
            self._node_layers[1] = self._layer
            self._node_layers[2] = self._layer_down
            self._node_layers[4] = self._layer

            if self._position_in_layer != 0:  # The node is not on the last edge
                self._node_positions_in_layers[0] = self._position_in_layer - n
                self._node_positions_in_layers[1] = self._position_in_layer + 1
                self._node_positions_in_layers[2] = self._node_positions_in_layers[1]
                self._node_positions_in_layers[3] = self._position_in_layer
                self._node_positions_in_layers[4] = self._position_in_layer - 1
            else:  # The node is on the last edge
                self._node_positions_in_layers[0] = 0
                self._node_positions_in_layers[1] = 1
                self._node_positions_in_layers[2] = 1
                self._node_positions_in_layers[3] = 0
                self._node_positions_in_layers[4] = self._layer * 5 - 1

    def _set_neighboring_nodes_in_part2_south_border(self):
        n = self._position_in_layer // (self._grid.LAST_NODE_LAYER - self._layer)
        k = self._position_in_layer % self._grid.PARTITION

        self._node_layers[0] = self._layer_up
        self._node_layers[1] = self._layer_up
        self._node_layers[2] = self._layer
        self._node_layers[3] = self._layer_down

        if k != 0:  # The node is not on the edge of the icosahedron
            self._nodes_number = 6
            self._node_layers[4] = self._layer_down
            self._node_layers[5] = self._layer

            self._node_positions_in_layers[0] = self._position_in_layer - 1
            self._node_positions_in_layers[1] = self._position_in_layer
            self._node_positions_in_layers[4] = self._node_positions_in_layers[0] - n
            self._node_positions_in_layers[5] = self._node_positions_in_layers[0]

            if self._position_in_layer < self._grid.LAST_NODE_POSITION_IN_LAYER_IN_PART2:
                self._node_positions_in_layers[2] = self._position_in_layer + 1
                self._node_positions_in_layers[3] = self._position_in_layer - n
            else:  # Two nodes are on the last edge.  The node is in front of the last edge.
                self._node_positions_in_layers[2] = 0
                self._node_positions_in_layers[3] = 0
        else:  # The node is on the edge of the icosahedron
            self._nodes_number = 5
            self._node_layers[4] = self._layer
            if self._position_in_layer != 0:  # The node is not on the last edge
                self._node_positions_in_layers[0] = self._position_in_layer - 1
                self._node_positions_in_layers[1] = self._position_in_layer
                self._node_positions_in_layers[2] = self._position_in_layer + 1
                self._node_positions_in_layers[3] = self._position_in_layer - n
                self._node_positions_in_layers[4] = self._node_positions_in_layers[0]
            else:  # The node is on the last edge
                self._node_positions_in_layers[0] = self._grid.LAST_NODE_POSITION_IN_LAYER_IN_PART2
                self._node_positions_in_layers[1] = 0
                self._node_positions_in_layers[2] = 1
                self._node_positions_in_layers[3] = 0
                self._node_positions_in_layers[4] = self._node_positions_in_layers[0]

    def _set_neighboring_nodes_in_part3_excluding_pole(self):
        self._nodes_number = 6
        diff = self._grid.LAST_NODE_LAYER - self._layer
        n = self._position_in_layer // diff
        k = self._position_in_layer % diff

        self._node_layers[0] = self._layer_up
        self._node_layers[1] = self._layer_up
        self._node_layers[2] = self._layer
        self._node_layers[3] = self._layer_down

        if k != 0:  # The node is not on the edge of the icosahedron
            self._node_layers[4] = self._layer_down
            self._node_layers[5] = self._layer

            self._node_positions_in_layers[0] = self._position_in_layer + n
            self._node_positions_in_layers[1] = self._node_positions_in_layers[0] + 1
            self._node_positions_in_layers[5] = self._position_in_layer - 1
            self._node_positions_in_layers[4] = self._node_positions_in_layers[5] - n

            if self._position_in_layer < diff * 5 - 1:
                self._node_positions_in_layers[2] = self._position_in_layer + 1
                self._node_positions_in_layers[3] = self._position_in_layer - n
            else:  # Two nodes fall on the first (also the last) edge
                self._node_positions_in_layers[2] = 0
                self._node_positions_in_layers[3] = 0

        else:  # The node is on the edge of the icosahedron
            self._node_layers[4] = self._layer
            self._node_layers[5] = self._layer_up

            if self._position_in_layer != 0:  # The node is not on the first (also the last) edge
                self._node_positions_in_layers[0] = self._position_in_layer + n
                self._node_positions_in_layers[5] = self._node_positions_in_layers[0] - 1
                self._node_positions_in_layers[1] = self._node_positions_in_layers[0] + 1
                if diff != 1 or self._position_in_layer != 4:
                    self._node_positions_in_layers[2] = self._position_in_layer + 1
                else:
                    self._node_positions_in_layers[2] = 0  # Take into account cyclicity
                self._node_positions_in_layers[3] = self._position_in_layer - n
                self._node_positions_in_layers[4] = self._position_in_layer - 1
            else:  # The node is on the last edge
                self._node_positions_in_layers[5] = (self._grid.LAST_NODE_LAYER - self._layer_up) * 5 - 1
                self._node_positions_in_layers[0] = 0
                self._node_positions_in_layers[1] = 1
                self._node_positions_in_layers[2] = 1
                self._node_positions_in_layers[3] = 0
                self._node_positions_in_layers[4] = diff * 5 - 1

    def _set_neighboring_nodes_in_part3_pole(self):
        self._nodes_number = 5
        self._node_layers[0] = self._grid.LAST_TRIANGLE_LAYER
        self._node_positions_in_layers[0] = 0
        self._node_layers[1] = self._grid.LAST_TRIANGLE_LAYER
        self._node_positions_in_layers[1] = 1
        self._node_layers[2] = self._grid.LAST_TRIANGLE_LAYER
        self._node_positions_in_layers[2] = 2
        self._node_layers[3] = self._grid.LAST_TRIANGLE_LAYER
        self._node_positions_in_layers[3] = 3
        self._node_layers[4] = self._grid.LAST_TRIANGLE_LAYER
        self._node_positions_in_layers[4] = 4
