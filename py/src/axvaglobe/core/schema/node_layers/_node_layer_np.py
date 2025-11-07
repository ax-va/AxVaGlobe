from axvaglobe.core.schema.constants import Constants
from axvaglobe.core.schema.node_layers._base_node_layer import _BaseNodeLayer


class _NodeLayerNP(_BaseNodeLayer):
    """
    The class is private because the constructor parameters are not validated.
    Instances of the class must only be created through the factory method, which performs validation.
    """

    @property
    def NODE_INDEX_OFFSET_FOR_LAYER(self) -> int:
        if self._node_index_offset_for_layer is None:
            self._node_index_offset_for_layer: int = self.constants.north_pole.node.INDEX
        return self._node_index_offset_for_layer

    @property
    def NUMBER_OF_NODES(self) -> int:
        if self._number_of_nodes is None:
            self._number_of_nodes = 1
        return self._number_of_nodes
