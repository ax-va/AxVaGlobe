class PartitionValueError(Exception):
    def __init__(self, value: int):
        self.message = f"The partition value is not a positive integer: {value}."
        Exception.__init__(self, self.message)


class _Area:
    """There are three areas: "A", "B", and "C"."""
    def __init__(self, name: str):
        self.name: str = name
        # constants for node indices in area
        self.FIRST_NODE_INDEX: int | None = None
        self.LAST_NODE_INDEX: int | None = None
        self.NUMBER_OF_NODES: int | None = None
        # constants for node layer indices in area
        self.FIRST_NODE_LAYER_INDEX: int | None = None
        self.LAST_NODE_LAYER_INDEX: int | None = None
        self.NUMBER_OF_NODE_LAYERS: int | None = None
        # constants for triangle indices in area
        self.FIRST_TRIANGLE_INDEX: int | None = None
        self.LAST_TRIANGLE_INDEX: int | None = None
        self.NUMBER_OF_TRIANGLES: int | None = None
        # constants for triangle layer indices in layer in area
        self.FIRST_TRIANGLE_LAYER_INDEX: int | None = None
        self.LAST_TRIANGLE_LAYER_INDEX: int | None = None
        self.NUMBER_OF_TRIANGLE_LAYERS: int | None = None


class _NodeBorder:
    """There are two node borders between three areas: "AB" and "BC"."""
    def __init__(self, name: str):
        self.name: str = name
        # constants for node indices in node border
        self.FIRST_NODE_INDEX: int | None = None
        self.LAST_NODE_INDEX: int | None = None
        self.NUMBER_OF_NODES: int | None = None
        # constants for node layer indices in node border
        self.NODE_LAYER_INDEX: int | None = None


class _AreaA(_Area):
    def __init__(self):
        super().__init__("A")


class _AreaB(_Area):
    def __init__(self):
        # constant for all node layers
        self.NUMBER_OF_NODE_LAYER_NODES: int | None = None
        super().__init__("B")


class _AreaC(_Area):
    def __init__(self):
        super().__init__("C")


class _NodeBorderAB(_NodeBorder):
    def __init__(self):
        super().__init__("AB")


class _NodeBorderBC(_NodeBorder):
    def __init__(self):
        super().__init__("BC")


class Partition:
    """
    This class contains all necessary constants that depend on a partition value.
    The partition value determines how many parts an edge of the icosahedron must be divided into.
    The partition of 1 corresponds to the icosahedron itself.
    """
    def __init__(self, partition: int = 1):
        if partition < 1:
            raise PartitionValueError(partition)

        self.PARTITION: int = partition
        self.PARTITION_MINUS_ONE: int = self.PARTITION - 1
        self.PARTITION_TIMES_FIVE: int = self.PARTITION * 5
        self.PARTITION_SQUARE: int = self.PARTITION * self.PARTITION
        self.PARTITION_SQUARE_TIMES_FIVE: int = self.PARTITION_SQUARE * 5
        # Set common constants
        self.NUMBER_OF_NODES: int = self.PARTITION_SQUARE_TIMES_FIVE * 2 + 2
        self.NUMBER_OF_TRIANGLES: int = self.PARTITION_SQUARE * 20
        self.NUMBER_OF_TRIANGLE_LAYERS: int = self.PARTITION * 3
        self.NUMBER_OF_NODE_LAYERS: int = self.NUMBER_OF_TRIANGLE_LAYERS + 1
        self.NUMBER_OF_EDGE_NODES: int = self.PARTITION + 1

        # Create schematic areas and node borders: "A"-"AB"-"B"-"BC"-"C"
        self.area_a = _AreaA()
        self.node_border_ab = _NodeBorderAB()
        self.area_b = _AreaB()
        self.node_border_bc = _NodeBorderBC()
        self.area_c = _AreaC()

        # Set constants for node indices
        self.area_a.FIRST_NODE_INDEX = 0
        self.area_a.NUMBER_OF_NODES = (self.PARTITION_SQUARE_TIMES_FIVE - self.PARTITION_TIMES_FIVE) // 2 + 1
        self.node_border_ab.FIRST_NODE_INDEX = self.area_a.FIRST_NODE_INDEX + self.area_a.NUMBER_OF_NODES
        self.area_a.LAST_NODE_INDEX = self.node_border_ab.FIRST_NODE_INDEX - 1
        self.node_border_ab.NUMBER_OF_NODES = self.PARTITION_TIMES_FIVE
        self.area_b.FIRST_NODE_INDEX = self.node_border_ab.FIRST_NODE_INDEX + self.node_border_ab.NUMBER_OF_NODES
        self.node_border_ab.LAST_NODE_INDEX = self.area_b.FIRST_NODE_INDEX - 1
        self.area_b.NUMBER_OF_NODES = self.PARTITION_MINUS_ONE * self.node_border_ab.NUMBER_OF_NODES
        self.node_border_bc.FIRST_NODE_INDEX = self.area_b.FIRST_NODE_INDEX + self.area_b.NUMBER_OF_NODES
        self.area_b.LAST_NODE_INDEX = self.node_border_bc.FIRST_NODE_INDEX - 1
        self.node_border_bc.NUMBER_OF_NODES = self.node_border_ab.NUMBER_OF_NODES
        self.area_c.FIRST_NODE_INDEX = self.node_border_bc.FIRST_NODE_INDEX + self.node_border_bc.NUMBER_OF_NODES
        self.node_border_bc.LAST_NODE_INDEX = self.area_c.FIRST_NODE_INDEX - 1
        self.area_c.NUMBER_OF_NODES = self.area_a.NUMBER_OF_NODES
        self.area_c.LAST_NODE_INDEX = self.NUMBER_OF_NODES - 1

        # Set constants for node layer indices
        self.area_a.FIRST_NODE_LAYER_INDEX = 0
        self.area_a.NUMBER_OF_NODE_LAYERS = self.PARTITION
        self.node_border_ab.NODE_LAYER_INDEX = self.area_a.FIRST_NODE_LAYER_INDEX + self.area_a.NUMBER_OF_NODE_LAYERS
        self.area_a.LAST_NODE_LAYER_INDEX = self.node_border_ab.NODE_LAYER_INDEX - 1
        self.area_b.FIRST_NODE_LAYER_INDEX = self.node_border_ab.NODE_LAYER_INDEX + 1
        self.area_b.NUMBER_OF_NODE_LAYERS = self.PARTITION_MINUS_ONE
        self.area_b.NUMBER_OF_NODE_LAYER_NODES = self.PARTITION_TIMES_FIVE
        self.node_border_bc.NODE_LAYER_INDEX = self.area_b.FIRST_NODE_LAYER_INDEX + self.area_b.NUMBER_OF_NODE_LAYERS
        self.area_b.LAST_NODE_LAYER_INDEX = self.node_border_bc.NODE_LAYER_INDEX - 1
        self.area_c.FIRST_NODE_LAYER_INDEX = self.node_border_bc.NODE_LAYER_INDEX + 1
        self.area_c.NUMBER_OF_NODE_LAYERS = self.area_a.NUMBER_OF_NODE_LAYERS
        self.area_c.LAST_NODE_LAYER_INDEX = self.NUMBER_OF_NODE_LAYERS - 1

        # Set constants for triangle indices
        self.area_a.FIRST_TRIANGLE_INDEX = 0
        self.area_a.NUMBER_OF_TRIANGLES = self.PARTITION_SQUARE_TIMES_FIVE
        self.area_b.FIRST_TRIANGLE_INDEX = self.area_a.FIRST_TRIANGLE_INDEX + self.area_a.NUMBER_OF_TRIANGLES
        self.area_a.LAST_TRIANGLE_INDEX = self.area_b.FIRST_TRIANGLE_INDEX - 1
        self.area_b.NUMBER_OF_TRIANGLES = self.area_a.NUMBER_OF_TRIANGLES * 2
        self.area_c.FIRST_TRIANGLE_INDEX = self.area_b.FIRST_TRIANGLE_INDEX + self.area_b.NUMBER_OF_TRIANGLES
        self.area_b.LAST_TRIANGLE_INDEX = self.area_c.FIRST_TRIANGLE_INDEX - 1
        self.area_c.NUMBER_OF_TRIANGLES = self.area_a.NUMBER_OF_TRIANGLES
        self.area_c.LAST_TRIANGLE_INDEX = self.NUMBER_OF_TRIANGLES - 1

        # Set constants for triangle layer indices
        self.area_a.FIRST_TRIANGLE_LAYER_INDEX = 0
        self.area_a.NUMBER_OF_TRIANGLE_LAYERS = self.PARTITION
        self.area_b.FIRST_TRIANGLE_LAYER_INDEX = self.area_a.FIRST_TRIANGLE_LAYER_INDEX + self.area_a.NUMBER_OF_TRIANGLE_LAYERS
        self.area_a.LAST_TRIANGLE_LAYER_INDEX = self.area_b.FIRST_TRIANGLE_LAYER_INDEX - 1
        self.area_b.NUMBER_OF_TRIANGLE_LAYERS = self.area_a.NUMBER_OF_TRIANGLE_LAYERS
        self.area_c.FIRST_TRIANGLE_LAYER_INDEX = self.area_b.FIRST_TRIANGLE_LAYER_INDEX + self.area_b.NUMBER_OF_TRIANGLE_LAYERS
        self.area_b.LAST_TRIANGLE_LAYER_INDEX = self.area_c.FIRST_TRIANGLE_LAYER_INDEX - 1
        self.area_c.NUMBER_OF_TRIANGLE_LAYERS = self.area_b.NUMBER_OF_TRIANGLE_LAYERS
        self.area_c.LAST_TRIANGLE_LAYER_INDEX = self.NUMBER_OF_TRIANGLE_LAYERS - 1


    def __repr__(self):
        return f"Partition({self.PARTITION})"


if __name__ == "__main__":
    prt = Partition(4)
    print("prt.PARTITION:", prt.PARTITION)
    print("prt.NUMBER_OF_NODES:", prt.NUMBER_OF_NODES)
    print("prt.NUMBER_OF_TRIANGLES:", prt.NUMBER_OF_TRIANGLES)
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
    print("prt.area_a.FIRST_TRIANGLE_INDEX:", prt.area_a.FIRST_TRIANGLE_INDEX)
    print("prt.area_a.LAST_TRIANGLE_INDEX:", prt.area_a.LAST_TRIANGLE_INDEX)
    print("prt.area_a.NUMBER_OF_TRIANGLES:", prt.area_a.NUMBER_OF_TRIANGLES)
    print("prt.area_b.FIRST_TRIANGLE_INDEX:", prt.area_b.FIRST_TRIANGLE_INDEX)
    print("prt.area_b.LAST_TRIANGLE_INDEX:", prt.area_b.LAST_TRIANGLE_INDEX)
    print("prt.area_b.NUMBER_OF_TRIANGLES:", prt.area_b.NUMBER_OF_TRIANGLES)
    print("prt.area_c.FIRST_TRIANGLE_INDEX:", prt.area_c.FIRST_TRIANGLE_INDEX)
    print("prt.area_c.LAST_TRIANGLE_INDEX:", prt.area_c.LAST_TRIANGLE_INDEX)
    print("prt.area_c.NUMBER_OF_TRIANGLES:", prt.area_c.NUMBER_OF_TRIANGLES)
