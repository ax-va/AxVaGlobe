from pyglobe3d.core.common.const_attrs import ConstantAttributes
from pyglobe3d.core.icosalogic.element_errs import PartitionValueError


class Grid(ConstantAttributes):
    def __init__(self, partition=1):
        # The partition's value of 1 corresponds to the icosahedron
        if not isinstance(partition, int) or partition < 1:
            raise PartitionValueError()
        self.PARTITION = partition
        self.PARTITION_MINUS_1 = self.PARTITION - 1
        self.PARTITION_PLUS_1 = self.PARTITION + 1
        self.PARTITION_X2 = self.PARTITION + self.PARTITION
        self.PARTITION_X2_MINUS_1 = self.PARTITION_X2 - 1
        self.PARTITION_X3 = self.PARTITION_X2 + self.PARTITION
        self.PARTITION_X4 = self.PARTITION_X2 + self.PARTITION_X2
        self.PARTITION_X5 = self.PARTITION_X3 + self.PARTITION_X2
        self.PARTITION_X10 = self.PARTITION_X5 + self.PARTITION_X5
        self.PARTITION_X10_MINUS_1 = self.PARTITION_X10 - 1
        self.SQUARED_PARTITION = self.PARTITION * self.PARTITION
        self.SQUARED_PARTITION_MINUS_PARTITION = self.SQUARED_PARTITION - self.PARTITION
        self.SQUARED_PARTITION_MINUS_PARTITION_X2_5 = self.SQUARED_PARTITION_MINUS_PARTITION * 5 // 2
        self.SQUARED_PARTITION_X5 = self.SQUARED_PARTITION * 5
        self.SQUARED_PARTITION_MINUS_PARTITION_X2_5_PLUS_SQUARED_PARTITION_X5_PLUS_PARTITION_X5 \
            = self.SQUARED_PARTITION_MINUS_PARTITION_X2_5 \
              + self.SQUARED_PARTITION_X5 \
              + self.PARTITION_X5
        self.SQUARED_PARTITION_X10 = self.SQUARED_PARTITION_X5 + self.SQUARED_PARTITION_X5
        self.SQUARED_PARTITION_X15 = self.SQUARED_PARTITION_X5 * 3
        self.SQUARED_PARTITION_X15_MINUS_1 = self.SQUARED_PARTITION_X15 - 1
        self.SQUARED_PARTITION_X20 = self.SQUARED_PARTITION_X10 + self.SQUARED_PARTITION_X10

        self.FIRST_NODE_INDEX_IN_PART2 = self.SQUARED_PARTITION_MINUS_PARTITION_X2_5 + 1
        self.FIRST_NODE_INDEX_IN_PART3 \
            = self.SQUARED_PARTITION_MINUS_PARTITION_X2_5_PLUS_SQUARED_PARTITION_X5_PLUS_PARTITION_X5 + 1
        self.FIRST_NODE_LAYER_IN_PART2 = self.PARTITION
        self.FIRST_TRIANGLE_INDEX_IN_PART2 = self.SQUARED_PARTITION_X5
        self.FIRST_TRIANGLE_INDEX_IN_PART3 = self.SQUARED_PARTITION_X15
        self.FIRST_TRIANGLE_LAYER_IN_PART2 = self.PARTITION
        self.FIRST_TRIANGLE_LAYER_IN_PART3 = self.PARTITION_X2
        self.LAST_NODE_INDEX = self.SQUARED_PARTITION_X10 + 1
        self.LAST_NODE_INDEX_IN_PART1 = self.SQUARED_PARTITION_MINUS_PARTITION_X2_5
        self.LAST_NODE_INDEX_IN_PART2 \
            = self.SQUARED_PARTITION_MINUS_PARTITION_X2_5_PLUS_SQUARED_PARTITION_X5_PLUS_PARTITION_X5
        self.LAST_NODE_LAYER = self.PARTITION_X3
        self.LAST_NODE_LAYER_IN_PART1 = self.PARTITION
        self.LAST_NODE_LAYER_IN_PART2 = self.PARTITION_X2
        self.LAST_NODE_POSITION_IN_LAYER_IN_PART2 = self.PARTITION_X5 - 1
        self.LAST_TRIANGLE_INDEX = self.SQUARED_PARTITION_X20 - 1
        self.LAST_TRIANGLE_INDEX_IN_PART1 = self.SQUARED_PARTITION_X5 - 1
        self.LAST_TRIANGLE_INDEX_IN_PART2 = self.SQUARED_PARTITION_X15_MINUS_1
        self.LAST_TRIANGLE_LAYER = self.PARTITION_X3 - 1
        self.LAST_TRIANGLE_LAYER_IN_PART1 = self.PARTITION_MINUS_1
        self.LAST_TRIANGLE_LAYER_IN_PART2 = self.PARTITION_X2_MINUS_1
        self.LAST_TRIANGLE_POSITION_IN_LAYER_IN_PART2 = self.PARTITION_X10_MINUS_1

        self.NUMBER_OF_EDGES = 30
        self.NUMBER_OF_NODES = self.SQUARED_PARTITION_X10 + 2
        self.NUMBER_OF_NODES_IN_EDGE = self.PARTITION_PLUS_1
        self.NUMBER_OF_TRIANGLES = self.SQUARED_PARTITION_X20

    def __repr__(self):
        return f'{self.__class__.__name__}(partition={self.PARTITION})'


if __name__ == '__main__':
    gd = Grid(10)
    print(gd)
    print(gd.LAST_NODE_INDEX_IN_PART2)
    # gd.PARTITION = 20
