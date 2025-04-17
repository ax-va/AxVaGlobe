from core.schema.node_layer import NodeLayer


class NodeLayerA(NodeLayer):
    @property
    def NODE_INDEX_OFFSET_FOR_LAYER(self) -> int:
        index_offset_for_area_a = 1
        sum_of_previous_layer_indices = self.INDEX * (self.INDEX - 1) // 2
        node_index_offset_for_layer = sum_of_previous_layer_indices * 5 + index_offset_for_area_a
        return node_index_offset_for_layer

    @property
    def NUMBER_OF_NODES(self) -> int:
        return self.INDEX * 5
