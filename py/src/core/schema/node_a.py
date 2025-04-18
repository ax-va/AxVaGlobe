from math import sqrt
from typing import Tuple

from core.schema.base_node import BaseNode


class NodeA(BaseNode):
    @classmethod
    def create_node_by_index(
            cls,
            index: int,
            schema,  # type: "Schema"
    ):
        layer_index, index_offset_for_layer = cls._get_layer_index_and_index_offset_for_layer(index)
        in_layer_index: int = index - index_offset_for_layer
        return cls(layer_index, in_layer_index, schema)

    @staticmethod
    def _get_layer_index_and_index_offset_for_layer(index: int) -> Tuple[int, int]:
        index_offset_for_area_a = 1
        num: int = (index - index_offset_for_area_a) // 5
        layer_index_minus_one: int = int((sqrt(num * 8 + 1) - 1) / 2)
        layer_index: int = layer_index_minus_one + 1
        sum_of_previous_layer_indices: int = ((layer_index_minus_one + 1) * layer_index_minus_one) // 2
        index_offset_for_layer: int = sum_of_previous_layer_indices * 5 + index_offset_for_area_a
        return layer_index, index_offset_for_layer
