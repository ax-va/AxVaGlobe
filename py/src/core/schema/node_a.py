from math import sqrt
from typing import Tuple


class NodeA:
    def __init__(self, index: int):
        self.INDEX: int = index
        layer_and_in_layer_indices: Tuple[int, int] = self._get_layer_and_in_layer_indices()
        self.LAYER_INDEX: int = layer_and_in_layer_indices[0]
        self.IN_LAYER_INDEX: int = layer_and_in_layer_indices[1]

    @property
    def number_of_nodes_in_layer(self) -> int:
        return self.LAYER_INDEX * 5

    def _get_layer_and_in_layer_indices(self) -> Tuple[int, int]:
        integer_part = self.INDEX // 5
        remainder = self.INDEX % 5
        # This is exactly equal to the layer index of the penultimate node in layer
        to_layer = (sqrt(integer_part * 8 + 1) - 1) / 2
        num = int(to_layer)
        sum_up_to_num = ((num + 1) * num) // 2
        if integer_part != sum_up_to_num or remainder != 0:
            # non-penultimate node in layer
            layer_index = num + 1
            in_layer_index = self.INDEX - sum_up_to_num * 5 - 1
        else:
            # penultimate node in layer
            layer_index = num
            in_layer_index = self.INDEX - (sum_up_to_num - num) * 5 - 1
        return layer_index, in_layer_index
