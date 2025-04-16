class NodeLayerA:
    def __init__(
            self,
            index: int,
            # optional
            node_index_offset_for_layer: int = None,
    ):
        self.INDEX = index  # layer index
        self._node_index_offset_for_layer: None | int = node_index_offset_for_layer
        self._number_of_nodes: None | int = None

    @property
    def NODE_INDEX_OFFSET_FOR_LAYER(self) -> int:
        if self._node_index_offset_for_layer is None:
            self._node_index_offset_for_layer = self.INDEX * (self.INDEX - 1) // 2 * 5 + 1
        return self._node_index_offset_for_layer

    @property
    def NUMBER_OF_NODES(self) -> int:
        if self._number_of_nodes is None:
            self._number_of_nodes = self.INDEX * 5
        return self._number_of_nodes
