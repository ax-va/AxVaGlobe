from axvaglobe.core.schema._base_node_layer import _BaseNodeLayer


class _NodeLayerA(_BaseNodeLayer):
    """
    The class is private because the constructor parameters are not validated.
    Instances of the class must only be created through the factory method, which performs validation.
    """

    @property
    def NODE_INDEX_OFFSET_FOR_LAYER(self) -> int:
        if self._node_index_offset_for_layer is None:
            index_offset_for_area_a: int = self._partition_obj.area_a.node_layers.START
            sum_of_previous_layer_indices: int = self.INDEX * (self.INDEX - 1) // 2
            self._node_index_offset_for_layer: int = (
                sum_of_previous_layer_indices * 5 + index_offset_for_area_a
            )
        return self._node_index_offset_for_layer

    @property
    def NUMBER_OF_NODES(self) -> int:
        if self._number_of_nodes is None:
            self._number_of_nodes: int = self.INDEX * 5
        return self._number_of_nodes
