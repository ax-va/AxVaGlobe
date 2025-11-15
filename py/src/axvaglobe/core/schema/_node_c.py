from math import sqrt
from typing import Self

from axvaglobe.core.schema.partition import Partition
from axvaglobe.core.schema._node_layer_c import _NodeLayerC
from axvaglobe.core.schema._base_node import _BaseNode


class _NodeC(_BaseNode):
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
        layer_index, index_offset_for_layer = (
            cls._get_layer_index_and_index_offset_for_layer(
                index=index,
                partition_obj=partition_obj,
            )
        )
        in_layer_index: int = index - index_offset_for_layer

        node = cls(
            layer_index=layer_index,
            in_layer_index=in_layer_index,
            partition_obj=partition_obj,
        )

        return node

    @staticmethod
    def _get_layer_index_and_index_offset_for_layer(
        index: int,
        partition_obj: Partition,
    ) -> tuple[int, int]:
        end_index: int = partition_obj.south_pole.node.INDEX
        end_index_for_area_c: int = partition_obj.area_c.nodes.END
        inverse_index_offset_for_area_c: int = end_index - end_index_for_area_c
        inverse_index: int = end_index - index
        inverse_num: int = (inverse_index - inverse_index_offset_for_area_c) // 5
        inverse_layer_index_minus_one: int = int((sqrt(inverse_num * 8 + 1) - 1) / 2)
        inverse_layer_index: int = inverse_layer_index_minus_one + 1
        end_layer_index: int = partition_obj.south_pole.node_layer.INDEX
        layer_index: int = end_layer_index - inverse_layer_index
        inverse_sum_of_previous_layer_indices: int = (
            inverse_layer_index * inverse_layer_index_minus_one
        ) // 2
        inverse_index_offset_for_layer: int = (
            inverse_sum_of_previous_layer_indices * 5 + inverse_index_offset_for_area_c
        )
        layer_obj: _NodeLayerC = _NodeLayerC(layer_index, partition_obj)
        index_offset_for_layer: int = (
            end_index
            - inverse_index_offset_for_layer
            - (layer_obj.NUMBER_OF_NODES - 1)
        )

        return layer_index, index_offset_for_layer
