from core.schema.base_node_layer import BaseNodeLayer


class NodeLayerB(BaseNodeLayer):
    @property
    def NODE_INDEX_OFFSET_FOR_LAYER(self) -> int:
        if self._node_index_offset_for_layer is None:
            # -2 comes from the node "NP" and the border "AB"
            relative_layer_index: int = self.INDEX - self._constants.area_a.node_layers.NUMBER - 2
            self._node_index_offset_for_layer: int = (
                self._constants.area_b.nodes.START + relative_layer_index * self.NUMBER_OF_NODES
            )
        return self._node_index_offset_for_layer

    @property
    def NUMBER_OF_NODES(self) -> int:
        if self._number_of_nodes is None:
            self._number_of_nodes: int = self._constants.border_ab.nodes.NUMBER
        return self._number_of_nodes
