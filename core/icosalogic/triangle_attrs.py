from math import sqrt

from pyglobe3d.core.icosalogic.element_attrs import ElementIndex, ElementLocation
from pyglobe3d.core.icosalogic.grid_consts import Grid


class TriangleIndex(ElementIndex):
    CONJUGATE_CLASS = {'ElementLocation': TriangleLocation}
    ELEMENT_NAME = {'element': 'triangle'} 
    
    def __init__(self, grid: Grid = Grid(), index: int = 0):
        ElementIndex.__init__(self, grid, index)

    @staticmethod
    def is_index_correct(grid, index):
        return 0 <= index <= grid.LAST_TRIANGLE_INDEX

    @staticmethod
    def is_index_in_part1(grid, index):
        return 0 <= index <= grid.LAST_TRIANGLE_INDEX_IN_PART1

    @staticmethod
    def is_index_in_part2(grid, index):
        return grid.FIRST_TRIANGLE_INDEX_IN_PART2 <= index <= grid.LAST_TRIANGLE_INDEX_IN_PART2

    @staticmethod
    def is_index_in_part3(grid, index):
        return grid.FIRST_TRIANGLE_INDEX_IN_PART3 <= index <= grid.LAST_TRIANGLE_INDEX

    def _get_location_in_part1(self):
        int_part = self.INDEX // 5
        remainder = self.INDEX % 5
        layer = int(sqrt(int_part))
        position_in_layer = (int_part - layer * layer) * 5 + remainder
        return layer, position_in_layer

    def _get_location_in_part2(self):
        layer \
            = (self.INDEX - self.GRID.FIRST_TRIANGLE_INDEX_IN_PART2) // self.GRID.PARTITION_X10 \
            + self.GRID.FIRST_TRIANGLE_LAYER_IN_PART2
        position_in_layer \
            = (self.INDEX - self.GRID.FIRST_TRIANGLE_INDEX_IN_PART2) % self.GRID.PARTITION_X10
        return layer, position_in_layer

    def _get_location_in_part3(self):
        int_part = (self.GRID.LAST_TRIANGLE_INDEX - self.INDEX) // 5
        remainder = (self.GRID.LAST_TRIANGLE_INDEX - self.INDEX) % 5
        reverse_layer = int(sqrt(int_part))
        layer = self.GRID.LAST_TRIANGLE_LAYER - reverse_layer
        position_in_layer \
            = ((reverse_layer + 1) * (reverse_layer + 1) - int_part) * 5 \
            - 1 - remainder
        return layer, position_in_layer


########################################################################################################################
########################################################################################################################


class TriangleLocation(ElementLocation):
    CONJUGATE_CLASS = {'ElementIndex': TriangleIndex}
    ELEMENT_NAME = {'element': 'triangle'}
    
    def __init__(self, grid=Grid(), layer=0, position_in_layer=0):
        ElementLocation.__init__(self, grid, layer, position_in_layer)

    @staticmethod
    def is_layer_correct(grid, layer):
        return 0 <= layer <= grid.LAST_TRIANGLE_LAYER

    @staticmethod
    def is_layer_in_part1(grid, layer):
        return 0 <= layer <= grid.LAST_TRIANGLE_LAYER_IN_PART1

    @staticmethod
    def is_layer_in_part2(grid, layer):
        return grid.FIRST_TRIANGLE_LAYER_IN_PART2 <= layer <= grid.LAST_TRIANGLE_LAYER_IN_PART2

    @staticmethod
    def is_layer_in_part3(grid, layer):
        return grid.FIRST_TRIANGLE_LAYER_IN_PART3 <= layer <= grid.LAST_TRIANGLE_LAYER

    @staticmethod
    def is_position_in_layer_in_part1_correct(layer, position_in_layer):
        last_position_in_layer_in_part1 = layer * 10 + 4
        return 0 <= position_in_layer <= last_position_in_layer_in_part1

    @staticmethod
    def is_position_in_layer_in_part2_correct(grid, position_in_layer):
        return 0 <= position_in_layer <= grid.LAST_TRIANGLE_POSITION_IN_LAYER_IN_PART2

    @staticmethod
    def is_position_in_layer_in_part3_correct(grid, layer, position_in_layer):
        last_position_in_layer_in_part3 \
            = (grid.LAST_TRIANGLE_LAYER - layer) * 10 + 4
        return 0 <= position_in_layer <= last_position_in_layer_in_part3

    @property
    def index_object(self):
        return TriangleIndex(
            grid=self.GRID,
            index=self.index
        )

    def _get_layer_index_increment_in_part1(self):
        return 5 * self.LAYER * self.LAYER

    def _get_layer_index_increment_in_part2(self):
        return self.GRID.FIRST_TRIANGLE_INDEX_IN_PART2 \
               + self.GRID.PARTITION_X10 * (self.LAYER - self.GRID.FIRST_TRIANGLE_LAYER_IN_PART2)

    def _get_layer_index_increment_in_part3(self):
        return self.GRID.SQUARED_PARTITION_X20 \
               - 5 * (self.GRID.PARTITION_X3 - self.LAYER) * (self.GRID.PARTITION_X3 - self.LAYER)
