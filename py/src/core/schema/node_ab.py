from core.schema.constants import Constants


class NodeAB:
    def __init__(self, index: int, c: Constants):
        self.INDEX: int = index
        self.LAYER_INDEX: int = c.border_ab.node_layer.INDEX
        self.NUMBER_OF_NODES_IN_LAYER = c.border_ab.nodes.NUMBER
        self.INDEX_OFFSET_FOR_LAYER = c.border_ab.nodes.START
        self.IN_LAYER_INDEX: int = self.INDEX - self.INDEX_OFFSET_FOR_LAYER
