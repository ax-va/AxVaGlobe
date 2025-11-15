from typing import Self

from axvaglobe.core.schema.partition import Partition
from axvaglobe.core.schema._base_node import _BaseNode


class _NodeBC(_BaseNode):
    """
    The class is private because the constructor parameters are not validated.
    Instances of the class must only be created through the factory method, which performs validation.
    """

    @classmethod
    def create_node(
        cls,
        index: int,
        partition_obj: Partition,
    ) -> Self:
        layer_index: int = partition_obj.border_bc.node_layer.INDEX
        index_offset_for_layer: int = partition_obj.border_bc.nodes.START
        in_layer_index: int = index - index_offset_for_layer

        node = cls(
            layer_index=layer_index,
            in_layer_index=in_layer_index,
            partition_obj=partition_obj,
        )

        return node
