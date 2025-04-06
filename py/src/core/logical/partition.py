class PartitionValueError(Exception):
    def __init__(self, value):
        self.message = f"The partition value is not a positive integer: {value}."
        Exception.__init__(self, self.message)


class Area:
    def __init__(self, name):
        self.name = name
        self.FIRST_NODE_INDEX = None
        self.LAST_NODE_INDEX = None
        self.NUMBER_OF_NODES = None


class NodeBorder:
    def __init__(self, name):
        self.name = name
        self.FIRST_NODE_INDEX = None
        self.LAST_NODE_INDEX = None
        self.NUMBER_OF_NODES = None


class Partition:
    def __init__(self, partition=1):
        # The partition's value of 1 corresponds to the icosahedron
        if not isinstance(partition, int) or partition < 1:
            raise PartitionValueError(partition)

        self.PARTITION = partition
        self.NUMBER_OF_NODES = self.PARTITION * self.PARTITION * 10 + 2

        # areas and node borders
        self.area_a = Area("A")
        self.node_border_ab = NodeBorder("AB")
        self.area_b = Area("B")
        self.node_border_bc = NodeBorder("BC")
        self.area_c = Area("C")

        # node constants
        self.area_a.FIRST_NODE_INDEX = 0
        self.area_a.LAST_NODE_INDEX = ((self.PARTITION - 1) * self.PARTITION) * 5 // 2
        self.area_a.NUMBER_OF_NODES = self.area_a.LAST_NODE_INDEX + 1
        self.node_border_ab.FIRST_NODE_INDEX = self.area_a.LAST_NODE_INDEX + 1
        self.node_border_ab.NUMBER_OF_NODES = self.PARTITION * 5
        self.area_b.FIRST_NODE_INDEX = self.node_border_ab.FIRST_NODE_INDEX + self.node_border_ab.NUMBER_OF_NODES
        self.node_border_ab.LAST_NODE_INDEX = self.area_b.FIRST_NODE_INDEX - 1
        self.area_b.NUMBER_OF_NODES = (self.PARTITION - 1) * self.node_border_ab.NUMBER_OF_NODES
        self.node_border_bc.FIRST_NODE_INDEX = self.area_b.FIRST_NODE_INDEX + self.area_b.NUMBER_OF_NODES
        self.area_b.LAST_NODE_INDEX = self.node_border_bc.FIRST_NODE_INDEX - 1
        self.node_border_bc.NUMBER_OF_NODES = self.node_border_ab.NUMBER_OF_NODES
        self.area_c.FIRST_NODE_INDEX = self.node_border_bc.FIRST_NODE_INDEX + self.node_border_bc.NUMBER_OF_NODES
        self.node_border_bc.LAST_NODE_INDEX = self.area_c.FIRST_NODE_INDEX - 1
        self.area_c.LAST_NODE_INDEX = self.NUMBER_OF_NODES - 1
        self.area_c.NUMBER_OF_NODES = self.area_a.NUMBER_OF_NODES

    #     # self.PARTITION_MINUS_1 = self.PARTITION - 1
    #     self.PARTITION_MINUS_ONE = self.PARTITION - 1
    #     # self.PARTITION_PLUS_1 = self.PARTITION + 1
    #     self.PARTITION_PLUS_ONE = self.PARTITION + 1
    #
    #     self.PARTITION_X2 = self.PARTITION + self.PARTITION
    #     self.PARTITION_X2_MINUS_1 = self.PARTITION_X2 - 1
    #     self.PARTITION_X3 = self.PARTITION_X2 + self.PARTITION
    #     self.PARTITION_X4 = self.PARTITION_X2 + self.PARTITION_X2
    #     self.PARTITION_X5 = self.PARTITION_X3 + self.PARTITION_X2
    #     self.PARTITION_X10 = self.PARTITION_X5 + self.PARTITION_X5
    #     self.PARTITION_X10_MINUS_1 = self.PARTITION_X10 - 1
    #     self.SQUARED_PARTITION = self.PARTITION * self.PARTITION
    #     self.SQUARED_PARTITION_MINUS_PARTITION = self.SQUARED_PARTITION - self.PARTITION
    #     self.SQUARED_PARTITION_MINUS_PARTITION_X2_5 = self.SQUARED_PARTITION_MINUS_PARTITION * 5 // 2
    #     self.SQUARED_PARTITION_X5 = self.SQUARED_PARTITION * 5
    #     self.SQUARED_PARTITION_MINUS_PARTITION_X2_5_PLUS_SQUARED_PARTITION_X5_PLUS_PARTITION_X5 \
    #         = self.SQUARED_PARTITION_MINUS_PARTITION_X2_5 \
    #           + self.SQUARED_PARTITION_X5 \
    #           + self.PARTITION_X5
    #     self.SQUARED_PARTITION_X10 = self.SQUARED_PARTITION_X5 + self.SQUARED_PARTITION_X5
    #     self.SQUARED_PARTITION_X15 = self.SQUARED_PARTITION_X5 * 3
    #     self.SQUARED_PARTITION_X15_MINUS_1 = self.SQUARED_PARTITION_X15 - 1
    #     self.SQUARED_PARTITION_X20 = self.SQUARED_PARTITION_X10 + self.SQUARED_PARTITION_X10
    #
    #     self.FIRST_NODE_INDEX_IN_PART2 = self.SQUARED_PARTITION_MINUS_PARTITION_X2_5 + 1
    #     self.FIRST_NODE_INDEX_IN_PART3 \
    #         = self.SQUARED_PARTITION_MINUS_PARTITION_X2_5_PLUS_SQUARED_PARTITION_X5_PLUS_PARTITION_X5 + 1
    #     self.FIRST_NODE_LAYER_IN_PART2 = self.PARTITION
    #     self.FIRST_NODE_LAYER_IN_PART3 = self.PARTITION_X2
    #     self.FIRST_TRIANGLE_INDEX_IN_PART2 = self.SQUARED_PARTITION_X5
    #     self.FIRST_TRIANGLE_INDEX_IN_PART3 = self.SQUARED_PARTITION_X15
    #     self.FIRST_TRIANGLE_LAYER_IN_PART2 = self.PARTITION
    #     self.FIRST_TRIANGLE_LAYER_IN_PART3 = self.PARTITION_X2
    #     self.LAST_NODE_INDEX  self.SQUARED_PARTITION_X10 + 1
    #     self.LAST_NODE_INDEX_IN_PART1 = self.SQUARED_PARTITION_MINUS_PARTITION_X2_5
    #     self.LAST_NODE_INDEX_IN_PART2 \
    #         = self.SQUARED_PARTITION_MINUS_PARTITION_X2_5_PLUS_SQUARED_PARTITION_X5_PLUS_PARTITION_X5
    #     self.LAST_NODE_LAYER = self.PARTITION_X3
    #     self.LAST_NODE_LAYER_IN_PART1 = self.PARTITION
    #     self.LAST_NODE_LAYER_IN_PART2 = self.PARTITION_X2
    #     self.LAST_NODE_POSITION_IN_LAYER_IN_PART2 = self.PARTITION_X5 - 1
    #     self.LAST_TRIANGLE_INDEX = self.SQUARED_PARTITION_X20 - 1
    #     self.LAST_TRIANGLE_INDEX_IN_PART1 = self.SQUARED_PARTITION_X5 - 1
    #     self.LAST_TRIANGLE_INDEX_IN_PART2 = self.SQUARED_PARTITION_X15_MINUS_1
    #     self.LAST_TRIANGLE_LAYER = self.PARTITION_X3 - 1
    #     self.LAST_TRIANGLE_LAYER_IN_PART1 = self.PARTITION_MINUS_1
    #     self.LAST_TRIANGLE_LAYER_IN_PART2 = self.PARTITION_X2_MINUS_1
    #     self.LAST_TRIANGLE_POSITION_IN_LAYER_IN_PART2 = self.PARTITION_X10_MINUS_1
    #
    #     self.NUMBER_OF_EDGES = 30
    #     self.NUMBER_OF_NODES = self.SQUARED_PARTITION_X10 + 2
    #     self.NUMBER_OF_NODES_IN_EDGE = self.PARTITION_PLUS_1
    #     self.NUMBER_OF_TRIANGLES = self.SQUARED_PARTITION_X20
    #
    # def __repr__(self):
    #     return f'{self.__class__.__name__}(partition={self.PARTITION})'


if __name__ == "__main__":
    prt = Partition(4)
    print(prt.area_a.FIRST_NODE_INDEX)
    print(prt.area_a.LAST_NODE_INDEX)
    print(prt.node_border_ab.FIRST_NODE_INDEX)
    print(prt.node_border_ab.LAST_NODE_INDEX)
    print(prt.area_b.FIRST_NODE_INDEX)
    print(prt.area_b.LAST_NODE_INDEX)
    print(prt.node_border_bc.FIRST_NODE_INDEX)
    print(prt.node_border_bc.LAST_NODE_INDEX)
    print(prt.area_c.FIRST_NODE_INDEX)
    print(prt.area_c.LAST_NODE_INDEX)
