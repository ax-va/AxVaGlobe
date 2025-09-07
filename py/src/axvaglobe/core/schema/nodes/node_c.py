from math import sqrt
from typing import Self

from axvaglobe.core.schema.constants import Constants
from axvaglobe.core.schema.node_layers.node_layer_c import _NodeLayerC
from axvaglobe.core.schema.nodes.base_node import _BaseNode


class _NodeC(_BaseNode):
    @classmethod
    def create_node_by_index(
        cls,
        index: int,
        constants: Constants,
    ) -> Self:
        layer_index, index_offset_for_layer = (
            cls._get_layer_index_and_index_offset_for_layer(index, constants)
        )
        in_layer_index: int = index - index_offset_for_layer
        return cls(layer_index, in_layer_index, constants)

    @staticmethod
    def _get_layer_index_and_index_offset_for_layer(
        index: int,
        constants: Constants,
    ) -> tuple[int, int]:
        end_index: int = constants.south_pole.node.INDEX
        end_index_for_area_c: int = constants.area_c.nodes.END
        inverse_index_offset_for_area_c: int = end_index - end_index_for_area_c
        inverse_index: int = end_index - index
        inverse_num: int = (inverse_index - inverse_index_offset_for_area_c) // 5
        inverse_layer_index_minus_one: int = int((sqrt(inverse_num * 8 + 1) - 1) / 2)
        inverse_layer_index: int = inverse_layer_index_minus_one + 1
        end_layer_index: int = constants.south_pole.node_layer.INDEX
        layer_index: int = end_layer_index - inverse_layer_index
        inverse_sum_of_previous_layer_indices: int = (
            inverse_layer_index * inverse_layer_index_minus_one
        ) // 2
        inverse_index_offset_for_layer: int = (
            inverse_sum_of_previous_layer_indices * 5 + inverse_index_offset_for_area_c
        )
        node_layer_c: _NodeLayerC = _NodeLayerC(layer_index, constants)
        index_offset_for_layer: int = (
            end_index
            - inverse_index_offset_for_layer
            - (node_layer_c.NUMBER_OF_NODES - 1)
        )
        return layer_index, index_offset_for_layer
