from axvaglobe.core.schema.node_layers.base_node_layer import _BaseNodeLayer


class _NodeLayerAB(_BaseNodeLayer):
    @property
    def NODE_INDEX_OFFSET_FOR_LAYER(self) -> int:
        if self._node_index_offset_for_layer is None:
            self._node_index_offset_for_layer: int = (
                self._constants.border_ab.nodes.START
            )
        return self._node_index_offset_for_layer

    @property
    def NUMBER_OF_NODES(self) -> int:
        if self._number_of_nodes is None:
            self._number_of_nodes: int = self._constants.border_ab.nodes.NUMBER
        return self._number_of_nodes
