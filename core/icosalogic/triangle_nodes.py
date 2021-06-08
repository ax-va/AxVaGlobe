from collections import namedtuple

from pyglobe3d.core.icosalogic.node import Node
from pyglobe3d.core.icosalogic.node_attrs import NodeLocation
from pyglobe3d.core.icosalogic.triangle import Triangle
from pyglobe3d.core.icosalogic.triangle_attrs import TriangleLocation


class TriangleNodes:
    def __init__(self, base_triangle: Triangle = Triangle()):
        self._base_triangle = base_triangle
        self._grid = base_triangle.grid
        self._layer = base_triangle.layer
        self._position_in_layer = base_triangle.position_in_layer
        self._node_layers = [None] * 3
        self._node_positions_in_layers = [None] * 3
        self._triangle_nodes = None
        self._node_layers[0] = self._layer
        self._node_layers[1] = self._layer + 1
        # This is the triangle orientation rule:
        # FALSE - one node top, two nodes bottom,
        # TRUE - two nodes top, one node bottom

    @property
    def triangle_nodes(self):
        if not self._triangle_nodes:
            self._set_triangle_nodes()
        return self._triangle_nodes

    def _set_triangle_nodes(self):
        if TriangleLocation.is_layer_in_part2(self._grid, self._layer):
            self._set_triangle_nodes_in_part2()

        elif TriangleLocation.is_layer_in_part1(self._grid, self._layer):
            self._set_triangle_nodes_in_part1()

        else:
            self._set_triangle_nodes_in_part3()

        Result = namedtuple('Nodes', ['node0', 'node1', 'node3'])
        self._triangle_nodes = Result(
            *(
                Node(
                    location_object=NodeLocation(
                        grid=self._grid,
                        layer=self._node_layers[i],
                        position_in_layer=self._node_positions_in_layers[i]
                    )
                ) for i in range(0, 3)
            )
        )

    def _set_triangle_nodes_in_part1(self):
        t = self._node_layers[1] + self._layer  # This is the number of triangles in one sublayer
        k = self._position_in_layer % t
        d = self._node_layers[0] * 5

        if k & 1 == 0:  # The triangle orientation is FALSE

            n = self._position_in_layer // t
            # This is the number of triangles with the orientation TRUE excluding the current sublayer:
            n_true = n * self._node_layers[0]
            # This is the number of triangles with the orientation FALSE excluding the current sublayer:
            n_false = n * self._node_layers[1]
            # this is the number of triangles with the orientation TRUE
            # only in the current sublayer up to (not including) the current triangle:
            k_true = k // 2
            # This is the number of triangles with the orientation FALSE
            # only in the current sublayer up to (not including) the current triangle:
            k_false = k_true

            self._node_layers[2] = self._node_layers[1]
            self._node_positions_in_layers[0] = n_true + k_true
            self._node_positions_in_layers[1] = n_false + k_false
            self._node_positions_in_layers[2] = self._node_positions_in_layers[1] + 1
            # Take into account out of range and zeroing the position:
            if self._node_positions_in_layers[2] >= d + 5:
                self._node_positions_in_layers[0] = 0
                self._node_positions_in_layers[2] = 0
        else:    # The triangle orientation is TRUE
            # This is the number of triangles with the orientation TRUE excluding the current sublayer:
            n_true = (self._position_in_layer // t) * self._node_layers[0]
            # This is the number of triangles with the orientation TRUE
            # only in the current sublayer up to (not including) the current triangle:
            k_true = (k - 1) // 2

            self._node_layers[2] = self._node_layers[0]
            self._node_positions_in_layers[0] = n_true + k_true
            self._node_positions_in_layers[2] = self._node_positions_in_layers[0] + 1
            self._node_positions_in_layers[1] = self._position_in_layer - self._node_positions_in_layers[0]
            # Take into account out of range and zeroing the position:
            if self._node_positions_in_layers[2] >= d:
                self._node_positions_in_layers[2] = 0

    def _set_triangle_nodes_in_part2(self):
        self._node_positions_in_layers[0] = self._position_in_layer // 2
        if self._position_in_layer & 1 == 0:  # The triangle orientation is FALSE
            self._node_layers[2] = self._node_layers[1]
            self._node_positions_in_layers[1] = self._node_positions_in_layers[0]
            self._node_positions_in_layers[2] = self._node_positions_in_layers[1] + 1
            # Take into account out of range and zeroing the position:
            if self._node_positions_in_layers[2] > self._grid.LAST_NODE_POSITION_IN_LAYER_IN_PART2:
                self._node_positions_in_layers[2] = 0
        else:  # The triangle orientation is TRUE
            self._node_layers[2] = self._node_layers[0]
            self._node_positions_in_layers[2] = self._node_positions_in_layers[0] + 1
            self._node_positions_in_layers[1] = self._node_positions_in_layers[2]
            # Take into account out of range and zeroing the position:
            if self._node_positions_in_layers[2] > self._grid.LAST_NODE_POSITION_IN_LAYER_IN_PART2:
                self._node_positions_in_layers[1] = 0
                self._node_positions_in_layers[2] = 0

    def _set_triangle_nodes_in_part3(self):
        last_node_layer_minus_node_layer0 = self._grid.LAST_NODE_LAYER - self._node_layers[0]
        last_node_layer_minus_node_layer1 = self._grid.LAST_NODE_LAYER - self._node_layers[1]
        # this is the number of triangles in one sublayer:
        t = last_node_layer_minus_node_layer0 + (self._grid.LAST_TRIANGLE_LAYER - self._layer)
        k = self._position_in_layer % t
        d = last_node_layer_minus_node_layer1 * 5

        if k & 1 == 0:  # The triangle orientation is TRUE
            n = self._position_in_layer // t
            n_true = n * last_node_layer_minus_node_layer1
            n_false = n * last_node_layer_minus_node_layer0
            k_true = k // 2
            k_false = k_true

            self._node_layers[2] = self._node_layers[0]
            self._node_positions_in_layers[1] = n_true + k_true
            self._node_positions_in_layers[0] = n_false + k_false
            self._node_positions_in_layers[2] = self._node_positions_in_layers[0] + 1
            # Take into account out of range and zeroing the position:
            if self._node_positions_in_layers[2] >= d + 5:
                self._node_positions_in_layers[1] = 0
                self._node_positions_in_layers[2] = 0
        else:  # The triangle orientation is FALSE
            n_true = (self._position_in_layer // t) * last_node_layer_minus_node_layer1
            k_true = (k - 1) // 2

            self._node_layers[2] = self._node_layers[1]
            self._node_positions_in_layers[1] = n_true + k_true
            self._node_positions_in_layers[2] = self._node_positions_in_layers[1] + 1
            self._node_positions_in_layers[0] = self._position_in_layer - self._node_positions_in_layers[1]
            # Take into account out of range and zeroing the position:
            if self._node_positions_in_layers[2] >= d:
                self._node_positions_in_layers[2] = 0
