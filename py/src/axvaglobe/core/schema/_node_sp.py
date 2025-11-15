from typing import Self

from axvaglobe.core.schema.partition import Partition
from axvaglobe.core.schema._base_node import _BaseNode


class _NodeSP(_BaseNode):
    """
    Class for the South Pole node.
    The class is private because the constructor parameters are not validated.
    Instances of the class must only be created through the factory method, which performs validation.
    """

    @classmethod
    def create_node_sp(
        cls,
        partition_obj: Partition,
    ) -> Self:
        layer_index: int = partition_obj.south_pole.node_layer.INDEX
        node = cls(
            layer_index=layer_index,
            in_layer_index=0,
            partition_obj=partition_obj,
        )

        return node
