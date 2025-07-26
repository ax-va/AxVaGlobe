from core.schema.errors import PartitionValueError


class _Indices:
    def __init__(self):
        self.START: int | None = None
        self.END: int | None = None
        self.NUMBER: int | None = None


class _Index:
    def __init__(self):
        self.INDEX: int | None = None


class _AreaNodes(_Indices):
    pass


class _AreaTriangles(_Indices):
    pass


class _AreaNodeLayers(_Indices):
    pass


class _AreaTriangleLayers(_Indices):
    pass


class _Area:
    """There are three areas: "A", "B", and "C"."""
    def __init__(self, name: str):
        self.name: str = name
        self.nodes = _AreaNodes()
        self.triangles = _AreaTriangles()
        self.node_layers = _AreaNodeLayers()
        self.triangle_layers = _AreaTriangleLayers()


class _BorderNodes(_Indices):
    pass


class _BorderNodeLayer(_Index):
    pass


class _Border:
    """There are two node borders between three areas: "AB" and "BC"."""
    def __init__(self, name: str):
        self.name: str = name
        self.nodes = _BorderNodes()
        self.node_layer = _BorderNodeLayer()


class _PoleNode(_Index):
    pass


class _PoleNodeLayer(_Index):
    pass


class _Pole:
    """There are two poles: "NP" and "SP"."""
    def __init__(self, name: str):
        self.name = name
        self.node = _PoleNode()
        self.node_layer = _PoleNodeLayer()


class _AreaA(_Area):
    def __init__(self):
        super().__init__("A")


class _AreaB(_Area):
    def __init__(self):
        super().__init__("B")


class _AreaC(_Area):
    def __init__(self):
        super().__init__("C")


class _BorderAB(_Border):
    def __init__(self):
        super().__init__("AB")


class _BorderBC(_Border):
    def __init__(self):
        super().__init__("BC")


class _NorthPole(_Pole):
    def __init__(self):
        super().__init__("NP")


class _SouthPole(_Pole):
    def __init__(self):
        super().__init__("SP")


class Constants:
    """
    This class contains all necessary constants that depend on a partition value.
    - The partition value determines how many parts an edge of the icosahedron must be divided into.
    - The partition must be greater than one.
    """
    def __init__(self, partition: int = 1):
        if not isinstance(partition, int) or partition < 2:
            raise PartitionValueError(partition)

        # Set auxiliary constants
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

        # for nodes: "NP"-"A"-"AB"-"B"-"BC"-"C"-"SP"
        # for triangles: "A"-"B"-"C"
        self.north_pole = _NorthPole()
        self.area_a = _AreaA()
        self.border_ab = _BorderAB()
        self.area_b = _AreaB()
        self.border_bc = _BorderBC()
        self.area_c = _AreaC()
        self.south_pole = _SouthPole()

        # Set constants for node indices
        self.north_pole.node.INDEX = 0
        self.area_a.nodes.START = self.north_pole.node.INDEX + 1
        self.area_a.nodes.NUMBER = (self.PARTITION_SQUARE_TIMES_FIVE - self.PARTITION_TIMES_FIVE) // 2
        self.border_ab.nodes.START = self.area_a.nodes.START + self.area_a.nodes.NUMBER
        self.area_a.nodes.END = self.border_ab.nodes.START - 1
        self.border_ab.nodes.NUMBER = self.PARTITION_TIMES_FIVE
        self.area_b.nodes.START = self.border_ab.nodes.START + self.border_ab.nodes.NUMBER
        self.border_ab.nodes.END = self.area_b.nodes.START - 1
        self.area_b.nodes.NUMBER = self.PARTITION_MINUS_ONE * self.border_ab.nodes.NUMBER
        self.border_bc.nodes.START = self.area_b.nodes.START + self.area_b.nodes.NUMBER
        self.area_b.nodes.END = self.border_bc.nodes.START - 1
        self.border_bc.nodes.NUMBER = self.border_ab.nodes.NUMBER
        self.area_c.nodes.START = self.border_bc.nodes.START + self.border_bc.nodes.NUMBER
        self.border_bc.nodes.END = self.area_c.nodes.START - 1
        self.area_c.nodes.NUMBER = self.area_a.nodes.NUMBER
        self.south_pole.node.INDEX = self.NUMBER_OF_NODES - 1
        self.area_c.nodes.END = self.south_pole.node.INDEX - 1

        # Set constants for node layer indices
        self.north_pole.node_layer.INDEX = 0
        self.area_a.node_layers.START = self.north_pole.node_layer.INDEX + 1
        self.area_a.node_layers.NUMBER = self.PARTITION_MINUS_ONE
        self.border_ab.node_layer.INDEX = self.area_a.node_layers.START + self.area_a.node_layers.NUMBER
        self.area_a.node_layers.END = self.border_ab.node_layer.INDEX - 1
        self.area_b.node_layers.START = self.border_ab.node_layer.INDEX + 1
        self.area_b.node_layers.NUMBER = self.PARTITION_MINUS_ONE
        self.border_bc.node_layer.INDEX = self.area_b.node_layers.START + self.area_b.node_layers.NUMBER
        self.area_b.node_layers.END = self.border_bc.node_layer.INDEX - 1
        self.area_c.node_layers.START = self.border_bc.node_layer.INDEX + 1
        self.area_c.node_layers.NUMBER = self.area_a.node_layers.NUMBER
        self.south_pole.node_layer.INDEX = self.NUMBER_OF_NODE_LAYERS - 1
        self.area_c.node_layers.END = self.south_pole.node_layer.INDEX - 1

        # Set constants for triangle indices
        self.area_a.triangles.START = 0
        self.area_a.triangles.NUMBER = self.PARTITION_SQUARE_TIMES_FIVE
        self.area_b.triangles.START = self.area_a.triangles.START + self.area_a.triangles.NUMBER
        self.area_a.triangles.END = self.area_b.triangles.START - 1
        self.area_b.triangles.NUMBER = self.area_a.triangles.NUMBER * 2
        self.area_c.triangles.START = self.area_b.triangles.START + self.area_b.triangles.NUMBER
        self.area_b.triangles.END = self.area_c.triangles.START - 1
        self.area_c.triangles.NUMBER = self.area_a.triangles.NUMBER
        self.area_c.triangles.END = self.NUMBER_OF_TRIANGLES - 1

        # Set constants for triangle layer indices
        self.area_a.triangle_layers.START = 0
        self.area_a.triangle_layers.NUMBER = self.PARTITION
        self.area_b.triangle_layers.START = self.area_a.triangle_layers.START + self.area_a.triangle_layers.NUMBER
        self.area_a.triangle_layers.END = self.area_b.triangle_layers.START - 1
        self.area_b.triangle_layers.NUMBER = self.area_a.triangle_layers.NUMBER
        self.area_c.triangle_layers.START = self.area_b.triangle_layers.START + self.area_b.triangle_layers.NUMBER
        self.area_b.triangle_layers.END = self.area_c.triangle_layers.START - 1
        self.area_c.triangle_layers.NUMBER = self.area_b.triangle_layers.NUMBER
        self.area_c.triangle_layers.END = self.NUMBER_OF_TRIANGLE_LAYERS - 1


    def __repr__(self):
        return f"{type(self)}({self.PARTITION})"
