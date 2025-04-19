from math import sqrt
from typing import Tuple

from core.schema.base_node import BaseNode


class NodeC(BaseNode):
    @classmethod
    def create_node_by_index(
            cls,
            index: int,
            schema,  # type: "Schema"
    ):
        layer_index, index_offset_for_layer = cls._get_layer_index_and_index_offset_for_layer(index, schema)
        in_layer_index: int = index - index_offset_for_layer
        return cls(layer_index, in_layer_index, schema)

    @staticmethod
    def _get_layer_index_and_index_offset_for_layer(
            index: int,
            schema,  # type: "Schema"
    ) -> Tuple[int, int]:
        end_index: int = schema.constants.south_pole.node.INDEX
        end_index_for_area_c: int = schema.constants.area_c.nodes.END
        inverse_index_offset_for_area_c: int = end_index - end_index_for_area_c
        inverse_index = end_index - index
        inverse_num: int = (inverse_index - inverse_index_offset_for_area_c) // 5
        inverse_layer_index_minus_one: int = int((sqrt(inverse_num * 8 + 1) - 1) / 2)
        inverse_layer_index: int = inverse_layer_index_minus_one + 1
        end_layer_index: int = schema.constants.south_pole.node_layer.INDEX
        layer_index: int = end_layer_index - inverse_layer_index
        inverse_sum_of_previous_layer_indices: int = (inverse_layer_index * inverse_layer_index_minus_one) // 2
        inverse_index_offset_for_layer: int = inverse_sum_of_previous_layer_indices * 5 + inverse_index_offset_for_area_c
        layer = schema.get_node_layer(layer_index)  # type: "node layer class"
        index_offset_for_layer: int = end_index - inverse_index_offset_for_layer - (layer.NUMBER_OF_NODES - 1)
        return layer_index, index_offset_for_layer
