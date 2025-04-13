from math import sqrt


class NodeA:
    def __init__(self, index: int):
        self.INDEX: int = index
        self.LAYER_INDEX: int | None = None
        self.IN_LAYER_INDEX: int | None = None
        self._set_layer_and_in_layer_indices()

    @property
    def NUMBER_OF_NODES_IN_LAYER(self) -> int:
        return self.LAYER_INDEX * 5

    @property
    def INDEX_OFFSET_FOR_LAYER(self) -> int:
        return ((self.LAYER_INDEX - 1) * self.LAYER_INDEX) // 2 * 5 + 1

    def _set_layer_and_in_layer_indices(self) -> None:
        integer_part: int = self.INDEX // 5
        remainder: int = self.INDEX % 5
        # This lies between layer_index - 1 and layer_index
        # and is exactly equal to layer_index of the penultimate node in layer.
        to_layer: float = (sqrt(integer_part * 8 + 1) - 1) / 2
        num: int = int(to_layer)
        sum_up_to_num: int = ((num + 1) * num) // 2
        if integer_part != sum_up_to_num or remainder != 0:
            # case 1: a non-penultimate node in layer
            self.LAYER_INDEX: int = num + 1
            # sum_up_to_num * 5 + 1 is the index offset for this layer
            self.IN_LAYER_INDEX: int = self.INDEX - sum_up_to_num * 5 - 1
        else:
            # case 2: the penultimate node in layer
            self.LAYER_INDEX: int = num
            # (sum_up_to_num - num) * 5 + 1 is the index offset for this layer
            self.IN_LAYER_INDEX: int = self.INDEX - (sum_up_to_num - num) * 5 - 1
