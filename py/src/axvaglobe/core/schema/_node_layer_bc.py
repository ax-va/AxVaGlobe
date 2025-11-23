from axvaglobe.core.schema._base_node_layer import _BaseNodeLayer


class _NodeLayerBC(_BaseNodeLayer):
    """
    The class is private because the constructor parameters are not validated.
    Instances of the class must only be created through the factory method, which performs validation.
    """

    @property
    def NODE_INDEX_OFFSET(self) -> int:
        if self._node_index_offset is None:
            self._node_index_offset: int = self._partition_obj.border_bc.nodes.START
        return self._node_index_offset

    @property
    def NUMBER_OF_NODES(self) -> int:
        if self._number_of_nodes is None:
            self._number_of_nodes: int = self._partition_obj.border_bc.nodes.NUMBER
        return self._number_of_nodes
