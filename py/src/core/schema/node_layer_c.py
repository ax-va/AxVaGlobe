from core.schema.base_node_layer import BaseNodeLayer


class NodeLayerC(BaseNodeLayer):
    @property
    def NODE_INDEX_OFFSET_FOR_LAYER(self) -> int:
        if self._node_index_offset_for_layer is None:
            end_index: int = self._schema.constants.south_pole.node_layer.INDEX
            end_index_for_area_c: int = self._schema.constants.area_c.node_layers.END
            inverse_index_offset_for_area_c = end_index - end_index_for_area_c
            inverse_index = end_index - self.INDEX
            inverse_sum_of_previous_layer_indices = inverse_index * (inverse_index - 1) // 2
            inverse_node_index_offset_for_layer = inverse_sum_of_previous_layer_indices * 5 + inverse_index_offset_for_area_c
            end_node_index: int = self._schema.constants.south_pole.node.INDEX
            self._node_index_offset_for_layer = end_node_index - inverse_node_index_offset_for_layer - (self.NUMBER_OF_NODES - 1)
        return self._node_index_offset_for_layer

    @property
    def NUMBER_OF_NODES(self) -> int:
        if self._number_of_nodes is None:
            end_index = self._schema.constants.south_pole.node_layer.INDEX
            inverse_index = end_index - self.INDEX
            self._number_of_nodes = inverse_index * 5
        return self._number_of_nodes
