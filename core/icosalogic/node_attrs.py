from math import sqrt

from pyglobe3d.core.icosalogic.element_attrs import ElementIndex, ElementLocation
from pyglobe3d.core.icosalogic.grid_consts import Grid


class NodeAttributes:
    ELEMENT_NAME = {'element': 'node'}


########################################################################################################################
########################################################################################################################


class NodeIndex(ElementIndex, NodeAttributes):
    def __init__(self, grid: Grid = Grid(), index: int = 0):
        ElementIndex.__init__(self, grid, index)

    @staticmethod
    def is_index_correct(grid, index):
        return 0 <= index <= grid.LAST_NODE_INDEX

    @staticmethod
    def is_index_in_part1(grid, index):
        return 0 <= index <= grid.LAST_NODE_INDEX_IN_PART1

    @staticmethod
    def is_index_in_part2(grid, index):
        return grid.FIRST_NODE_INDEX_IN_PART2 <= index <= grid.LAST_NODE_INDEX_IN_PART2

    @staticmethod
    def is_index_in_part3(grid, index):
        return grid.FIRST_NODE_INDEX_IN_PART3 <= index <= grid.LAST_NODE_INDEX

    def _get_location_in_part1(self):
        int_part = self.INDEX // 5
        remainder = self.INDEX % 5
        n = int((sqrt(1 + int_part * 8) - 1) / 2)
        sum_n = ((n + 1) * n) // 2
        if int_part != sum_n or remainder != 0:
            layer = n + 1
            position_in_layer = self.INDEX - sum_n * 5 - 1
        elif n == 0:
            layer = 0
            position_in_layer = 0
        else:
            layer = n
            position_in_layer = self.INDEX - (sum_n - n) * 5 - 1
        return layer, position_in_layer

    def _get_location_in_part2(self):
        layer = (self.INDEX - self.GRID.FIRST_NODE_INDEX_IN_PART2) // self.GRID.PARTITION_X5 + self.GRID.PARTITION
        position_in_layer = (self.INDEX - self.GRID.FIRST_NODE_INDEX_IN_PART2) % self.GRID.PARTITION_X5
        return layer, position_in_layer

    def _get_location_in_part3(self):
        int_part = (self.GRID.LAST_NODE_INDEX - self.INDEX) // 5
        remainder = (self.GRID.LAST_NODE_INDEX - self.INDEX) % 5
        n = int((sqrt(1 + int_part * 8) - 1) / 2)
        sum_n = ((n + 1) * n) // 2
        if int_part != sum_n or remainder != 0:
            layer = self.GRID.LAST_NODE_LAYER - (n + 1)
            position_in_layer = \
                (self.GRID.LAST_NODE_LAYER - layer + sum_n) * 5 \
                - self.GRID.LAST_NODE_INDEX \
                + self.INDEX
        elif n == 0:
            layer = self.GRID.LAST_NODE_LAYER
            position_in_layer = 0
        else:
            layer = self.GRID.LAST_NODE_LAYER - n
            position_in_layer = \
                (self.GRID.LAST_NODE_LAYER - layer + sum_n - n) * 5 \
                - self.GRID.LAST_NODE_INDEX \
                + self.INDEX
        return layer, position_in_layer


########################################################################################################################
########################################################################################################################


class NodeLocation(ElementLocation, NodeAttributes):
    def __init__(self, grid: Grid = Grid(), layer: int = 0, position_in_layer: int = 0):
        ElementLocation.__init__(self, grid, layer, position_in_layer)

    @staticmethod
    def is_layer_correct(grid, layer):
        return 0 <= layer <= grid.LAST_NODE_LAYER

    @staticmethod
    def is_layer_in_part1(grid, layer):
        return 0 <= layer < grid.FIRST_NODE_LAYER_IN_PART2

    @staticmethod
    def is_layer_in_part1_excluding_pole(grid, layer):
        return 0 < layer < grid.FIRST_NODE_LAYER_IN_PART2

    @staticmethod
    def is_layer_in_part1_pole(layer):
        return layer == 0

    @staticmethod
    def is_layer_in_part2(grid, layer):
        return grid.FIRST_NODE_LAYER_IN_PART2 <= layer <= grid.LAST_NODE_LAYER_IN_PART2

    @staticmethod
    def is_layer_in_part2_excluding_borders(grid, layer):
        return grid.FIRST_NODE_LAYER_IN_PART2 < layer < grid.LAST_NODE_LAYER_IN_PART2

    @staticmethod
    def is_layer_in_part2_north_border(grid, layer):
        return layer == grid.FIRST_NODE_LAYER_IN_PART2

    @staticmethod
    def is_layer_in_part2_south_border(grid, layer):
        return layer == grid.LAST_NODE_LAYER_IN_PART2

    @staticmethod
    def is_layer_in_part3(grid, layer):
        return grid.LAST_NODE_LAYER_IN_PART2 < layer <= grid.LAST_NODE_LAYER

    @staticmethod
    def is_layer_in_part3_excluding_pole(grid, layer):
        return grid.LAST_NODE_LAYER_IN_PART2 < layer < grid.LAST_NODE_LAYER

    @staticmethod
    def is_layer_in_part3_pole(grid, layer):
        return layer == grid.LAST_NODE_LAYER

    @staticmethod
    def is_position_in_layer_in_part1_correct(layer, position_in_layer):
        last_position_in_layer_in_part1 = layer * 5 - 1 if layer > 0 else 0
        return 0 <= position_in_layer <= last_position_in_layer_in_part1

    @staticmethod
    def is_position_in_layer_in_part2_correct(grid, position_in_layer):
        return 0 <= position_in_layer <= grid.LAST_NODE_POSITION_IN_LAYER_IN_PART2

    @staticmethod
    def is_position_in_layer_in_part3_correct(grid, layer, position_in_layer):
        last_position_in_layer_in_part3 \
            = (grid.LAST_NODE_LAYER - layer) * 5 - 1 \
            if (grid.LAST_NODE_LAYER - layer) > 0 else 0
        return 0 <= position_in_layer <= last_position_in_layer_in_part3

    def _get_layer_index_increment_in_part1(self):
        return (5 * (self.LAYER - 1) * self.LAYER) // 2 + 1 if self.LAYER > 0 else 0

    def _get_layer_index_increment_in_part2(self):
        return self.GRID.FIRST_NODE_INDEX_IN_PART2 + (self.LAYER - self.GRID.PARTITION)*self.GRID.PARTITION_X5

    def _get_layer_index_increment_in_part3(self):
        return self.GRID.LAST_NODE_INDEX \
               - (5 * (self.GRID.LAST_NODE_LAYER - self.LAYER + 1) * (self.GRID.LAST_NODE_LAYER - self.LAYER)) // 2


########################################################################################################################
########################################################################################################################


NodeIndex.CONJUGATE_CLASS = {'ElementLocation': NodeLocation}
NodeLocation.CONJUGATE_CLASS = {'ElementIndex': NodeIndex}
