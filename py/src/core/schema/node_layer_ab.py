class NodeLayerAB:
    def __init__(
            self,
            constants,  # type: "Constants"
    ):
        self.INDEX = constants.border_ab.node_layer.INDEX
        self.NUMBER_OF_NODES = constants.border_ab.nodes.NUMBER
        # lazy
        self._node_index_offset_for_layer: None | int = None

    @property
    def NODE_INDEX_OFFSET_FOR_LAYER(self) -> int:
        if self._node_index_offset_for_layer is None:
            index_offset_for_area_a = 1
            sum_of_previous_layer_indices = self.INDEX * (self.INDEX - 1) // 2
            self._node_index_offset_for_layer = sum_of_previous_layer_indices * 5 + index_offset_for_area_a
        return self._node_index_offset_for_layer
