from core.schema.base_node_layer import BaseNodeLayer


class NodeLayerA(BaseNodeLayer):
    @property
    def NODE_INDEX_OFFSET_FOR_LAYER(self) -> int:
        if self._node_offset_for_layer is None:
            index_offset_for_area_a = 1
            sum_of_previous_layer_indices = self.INDEX * (self.INDEX - 1) // 2
            self._node_offset_for_layer = sum_of_previous_layer_indices * 5 + index_offset_for_area_a
        return self._node_offset_for_layer

    @property
    def NUMBER_OF_NODES(self) -> int:
        if self._number_of_nodes is None:
            self._number_of_nodes = self.INDEX * 5
        return self._number_of_nodes
