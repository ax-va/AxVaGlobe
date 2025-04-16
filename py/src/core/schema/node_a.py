from math import sqrt
from typing import Tuple


class NodeA:
    def __init__(
            self,
            layer_index: int,
            in_layer_index: int,
            base_schema,  # type: "BaseSchema"
            # optional
            index: int = None,
            index_offset_for_layer: int = None,
    ):
        self.IN_LAYER_INDEX: int = in_layer_index
        self._base_schema = base_schema  # type: "BaseSchema"
        self._layer = self._base_schema.get_node_layer_from_registry(layer_index, index_offset_for_layer)  # type: "NodeLayerA"
        self._index: int | None = index

    @property
    def LAYER_INDEX(self) -> int:
        return self._layer.INDEX

    @property
    def INDEX(self) -> int:
        if self._index is None:
            self._index = self._layer.NODE_INDEX_OFFSET_FOR_LAYER + self.IN_LAYER_INDEX
        return self._index

    @classmethod
    def create_node_by_index(
            cls,
            index: int,
            base_schema,  # type: "BaseSchema"
    ):
        layer_index, index_offset_for_layer = cls._get_layer_index_and_index_offset_for_layer_by_index(index)
        in_layer_index = index - index_offset_for_layer
        return cls(layer_index, in_layer_index, base_schema, index, index_offset_for_layer)

    @staticmethod
    def _get_layer_index_and_index_offset_for_layer_by_index(index: int) -> Tuple[int, int]:
        integer_part_of_relative_index: int = (index - 1) // 5
        num_: float = (sqrt(integer_part_of_relative_index * 8 + 1) - 1) / 2
        num: int = int(num_)
        layer_index: int = num + 1
        sum_up_to_num: int = ((num + 1) * num) // 2
        index_offset_for_layer = sum_up_to_num * 5 + 1
        return layer_index, index_offset_for_layer
