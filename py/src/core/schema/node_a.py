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
        integer_part: int = self.INDEX // 5
        remainder: int = self.INDEX % 5
        # This lies between layer_index - 1 and layer_index
        # and is exactly equal to layer_index of the penultimate node in layer.
        to_layer: float = (sqrt(integer_part * 8 + 1) - 1) / 2
        num: int = int(to_layer)
        sum_up_to_num: int = ((num + 1) * num) // 2
        if integer_part != sum_up_to_num or remainder != 0:
            # case 1: a non-penultimate node in layer
            layer_index: int = num + 1
            # sum_up_to_num * 5 is the offset relative to previous layers
            in_layer_index: int = self.INDEX - sum_up_to_num * 5 - 1
        else:
            # case 2: the penultimate node in layer
            layer_index: int = num
            in_layer_index: int = self.INDEX - (sum_up_to_num - num) * 5 - 1
        return layer_index, in_layer_index
