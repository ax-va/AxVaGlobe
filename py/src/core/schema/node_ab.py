from core.schema.constants import Constants


class NodeAB:
    def __init__(self, index: int, c: Constants):
        self.INDEX: int = index
        self.LAYER_INDEX: int = c.border_ab.node_layer.INDEX
        self.INDEX_OFFSET_FOR_LAYER: int = c.border_ab.nodes.START
        self.IN_LAYER_INDEX: int = self.INDEX - self.INDEX_OFFSET_FOR_LAYER
        self.NUMBER_OF_NODES_IN_LAYER: int = c.border_ab.nodes.NUMBER
