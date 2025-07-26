from math import sqrt
from typing import Tuple, Self

from core.schema.base_node import BaseNode
from core.schema.constants import Constants


class NodeA(BaseNode):
    @classmethod
    def create_node_by_index(
        cls,
        index: int,
        constants: Constants,
    ) -> Self:
        layer_index, index_offset_for_layer = cls._get_layer_index_and_index_offset_for_layer(index, constants)
        in_layer_index: int = index - index_offset_for_layer
        return cls(layer_index, in_layer_index, constants)

    def get_layer_and_in_layer_indices_of_neighboring_nodes(
            self,
    ) -> Tuple[
            # 6 neighboring nodes indices
            Tuple[int, int],  # (layer_index, in_layer_index)
            Tuple[int, int],
            Tuple[int, int],
            Tuple[int, int],
            Tuple[int, int],
            Tuple[int, int]
    ]:
        """Returns 6 neighboring nodes indices (layer_index, in_layer_index)."""
        layer_index_up: int = self.LAYER_INDEX - 1
        layer_index_down: int = self.LAYER_INDEX + 1
        in_layer_index_left: int = self.IN_LAYER_INDEX - 1
        in_layer_index_right: int = self.IN_LAYER_INDEX + 1

        num: int = self.IN_LAYER_INDEX // self.LAYER_INDEX
        rem: int = self.IN_LAYER_INDEX % self.LAYER_INDEX

        layer_index_0: int = layer_index_up  # up
        layer_index_3: int = layer_index_down  # down
        layer_index_4: int = layer_index_down  # down
        layer_index_5: int = self.LAYER_INDEX

        end_node_in_layer_index = self._layer.END_NODE_IN_LAYER_INDEX
        if rem != 0:  # This node is not on the edge of the icosahedron
            layer_index_1: int = layer_index_up  # up
            layer_index_2: int = self.LAYER_INDEX

            in_layer_index_4: int = self.IN_LAYER_INDEX + num
            in_layer_index_5: int = in_layer_index_left
            in_layer_index_0: int = in_layer_index_left - num
            in_layer_index_3: int = in_layer_index_4 + 1

            if self.IN_LAYER_INDEX < end_node_in_layer_index:  # This node is not the last node in the layer
                in_layer_index_1: int = self.IN_LAYER_INDEX - num
                in_layer_index_2: int = in_layer_index_right

            else:  # This node is the last node in the layer
                in_layer_index_1: int = 0
                in_layer_index_2: int = 0

        else:  # This node is on the edge of the icosahedron
            layer_index_1: int = self.LAYER_INDEX
            layer_index_2: int = layer_index_down  # down

            if self.IN_LAYER_INDEX != 0:  # This node is not the first node in the layer
                in_layer_index_3: int = self.IN_LAYER_INDEX + num
                in_layer_index_2: int = in_layer_index_3 + 1
                in_layer_index_4: int = in_layer_index_3 - 1
                in_layer_index_0: int = self.IN_LAYER_INDEX - num
                in_layer_index_1: int = in_layer_index_right if self.IN_LAYER_INDEX != end_node_in_layer_index else 0
                in_layer_index_5: int = in_layer_index_left

            else:  # This node is the first node in the layer
                in_layer_index_0: int = 0
                in_layer_index_1: int = 1
                in_layer_index_2: int = 1
                in_layer_index_3: int = 0
                in_layer_index_4: int = layer_index_down * 5 - 1
                in_layer_index_5: int = self._layer.END_NODE_IN_LAYER_INDEX

        return (
            (layer_index_0, in_layer_index_0),
            (layer_index_1, in_layer_index_1),
            (layer_index_2, in_layer_index_2),
            (layer_index_3, in_layer_index_3),
            (layer_index_4, in_layer_index_4),
            (layer_index_5, in_layer_index_5),
        )

    @staticmethod
    def _get_layer_index_and_index_offset_for_layer(
        index: int,
        constants: Constants,
    ) -> Tuple[int, int]:
        index_offset_for_area_a: int = constants.area_a.nodes.START
        num: int = (index - index_offset_for_area_a) // 5
        layer_index_minus_one: int = int((sqrt(num * 8 + 1) - 1) / 2)
        layer_index: int = layer_index_minus_one + 1
        sum_of_previous_layer_indices: int = (layer_index * layer_index_minus_one) // 2
        index_offset_for_layer: int = sum_of_previous_layer_indices * 5 + index_offset_for_area_a
        return layer_index, index_offset_for_layer
