class PartitionValueError(Exception):
    def __init__(self, value: int):
        self.message = f"The `partition`'s value is not a positive integer: {value}."
        Exception.__init__(self, self.message)


class _Area:
    """There are three areas: "A", "B", and "C"."""
    def __init__(self, name: str):
        self.name: str = name
        self.FIRST_NODE_INDEX: int | None = None
        self.LAST_NODE_INDEX: int | None = None
        self.NUMBER_OF_NODES: int | None = None


class _NodeBorder:
    """There are two node borders between three areas: "AB" and "BC"."""
    def __init__(self, name: str):
        self.name: str = name
        self.FIRST_NODE_INDEX: int | None = None
        self.LAST_NODE_INDEX: int | None = None
        self.NUMBER_OF_NODES: int | None = None


class Partition:
    """
    This class contains all necessary constants that depend on a partition value.
    The partition value determines how many parts an edge of the icosahedron must be divided into.
    The partitiob of 1 corresponds to the icosahedron itself.
    """
    def __init__(self, partition: int = 1):
        if partition < 1:
            raise PartitionValueError(partition)

        # Set common constants
        self.PARTITION: int = partition
        self.PARTITION_SQUARE: int = self.PARTITION * self.PARTITION
        self.NUMBER_OF_NODES: int = self.PARTITION_SQUARE * 10 + 2

        # Create schematic *disjoint* areas and node borders: 
        # "A"-"AB"-"B"-"BC"-"C"
        self.area_a = _Area("A")
        self.node_border_ab = _NodeBorder("AB")
        self.area_b = _Area("B")
        self.node_border_bc = _NodeBorder("BC")
        self.area_c = _Area("C")

        # Set constants for nodes
        self.area_a.FIRST_NODE_INDEX = 0
        self.area_a.LAST_NODE_INDEX = (self.PARTITION_SQUARE - self.PARTITION) * 5 // 2
        self.area_a.NUMBER_OF_NODES = self.area_a.LAST_NODE_INDEX + 1
        self.node_border_ab.FIRST_NODE_INDEX = self.area_a.NUMBER_OF_NODES
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
    print("prt.area_a.FIRST_NODE_INDEX:", prt.area_a.FIRST_NODE_INDEX)
    print("prt.area_a.LAST_NODE_INDEX:", prt.area_a.LAST_NODE_INDEX)
    print("prt.area_a.NUMBER_OF_NODES:", prt.area_a.NUMBER_OF_NODES)
    print("prt.node_border_ab.FIRST_NODE_INDEX:", prt.node_border_ab.FIRST_NODE_INDEX)
    print("prt.node_border_ab.LAST_NODE_INDEX:", prt.node_border_ab.LAST_NODE_INDEX)
    print("prt.node_border_ab.NUMBER_OF_NODES:", prt.node_border_ab.NUMBER_OF_NODES)
    print("prt.area_b.FIRST_NODE_INDEX:", prt.area_b.FIRST_NODE_INDEX)
    print("prt.area_b.LAST_NODE_INDEX:", prt.area_b.LAST_NODE_INDEX)
    print("prt.area_b.NUMBER_OF_NODES:", prt.area_b.NUMBER_OF_NODES)
    print("prt.node_border_bc.FIRST_NODE_INDEX:", prt.node_border_bc.FIRST_NODE_INDEX)
    print("prt.node_border_bc.LAST_NODE_INDEX:", prt.node_border_bc.LAST_NODE_INDEX)
    print("prt.node_border_bc.NUMBER_OF_NODES:", prt.node_border_bc.NUMBER_OF_NODES)
    print("prt.area_c.FIRST_NODE_INDEX:", prt.area_c.FIRST_NODE_INDEX)
    print("prt.area_c.LAST_NODE_INDEX:", prt.area_c.LAST_NODE_INDEX)
    print("prt.area_c.NUMBER_OF_NODES:", prt.area_c.NUMBER_OF_NODES)
