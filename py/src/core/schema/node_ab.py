from typing import Tuple


class NodeAB:
    def __init__(
            self,
            in_layer_index: int,
            schema,  # type: "Schema"
            # optional
            index: int = None,
    ):
        self.IN_LAYER_INDEX: int = in_layer_index
        self._schema = schema  # type: "Schema"
        layer_index = self._schema.constants.border_ab.node_layer.INDEX
        self._layer = self._schema.get_node_layer_from_registry(layer_index)  # type: "NodeLayerAB"
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
        schema,  # type: "Schema"
    ):
        layer_index, index_offset_for_layer = cls._get_layer_index_and_index_offset_for_layer(schema)
        in_layer_index = index - index_offset_for_layer
        return cls(in_layer_index, schema, index)

    @staticmethod
    def _get_layer_index_and_index_offset_for_layer(
        schema,  # type: "Schema"
    ) -> Tuple[int, int]:
        index_offset_for_area_a = 1
        layer_index: int = schema.constants.border_ab.node_layer.INDEX
        sum_of_previous_layer_indices: int = (layer_index * (layer_index - 1)) // 2
        index_offset_for_layer = sum_of_previous_layer_indices * 5 + index_offset_for_area_a
        return layer_index, index_offset_for_layer