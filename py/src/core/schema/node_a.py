from math import sqrt
from typing import Tuple


class NodeA:
    def __init__(self, index: int):
        self.INDEX: int = index
        self.LAYER_INDEX, self.IN_LAYER_INDEX = self._get_layer_index_and_in_layer_index()
        self.NUMBER_OF_NODES_IN_LAYER = self.LAYER_INDEX * 5
        self.INDEX_OFFSET_FOR_LAYER = ((self.LAYER_INDEX - 1) * self.LAYER_INDEX) // 2 * 5 + 1

    def _get_layer_index_and_in_layer_index(self) -> Tuple[int, int]:
        integer_part: int = self.INDEX // 5
        remainder: int = self.INDEX % 5
        # This value is in the interval [layer_index - 1, layer_index].
        # It is equal to layer_index - 1 for the first four nodes in layer
        # and to layer_index for the last node in layer.
        # It is in (layer_index - 1, layer_index) for the other nodes in layer.
        num_: float = (sqrt(integer_part * 8 + 1) - 1) / 2
        # We have the equality
        # (num_ * 2 + 1)^2 = num_^2 * 4 + num_ * 4 + 1 = (num_ + 1) * num_ * 4 + 1 == integer_part * 8 + 1
        # and inequality
        # layer_index * (layer_index - 1) <= integer_part * 2 <= (layer_index + 1) * layer_index.
        num: int = int(num_)
        sum_up_to_num: int = ((num + 1) * num) // 2
        if integer_part != sum_up_to_num or remainder != 0:
            # case 1: not the last node in layer
            layer_index: int = num + 1
            # sum_up_to_num * 5 + 1 is the index offset for this layer
            in_layer_index: int = self.INDEX - sum_up_to_num * 5 - 1
        else:
            # case 2: the last node in layer
            layer_index: int = num
            # (sum_up_to_num - num) * 5 + 1 is the index offset for this layer
            in_layer_index: int = self.INDEX - (sum_up_to_num - num) * 5 - 1
        return layer_index, in_layer_index
