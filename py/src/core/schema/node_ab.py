from core.schema.base_node import BaseNode


class NodeAB(BaseNode):
    @classmethod
    def create_node_by_index(
            cls,
            index: int,
            schema,  # type: "Schema"
    ):
        layer_index: int = schema.constants.border_ab.node_layer.INDEX
        index_offset_for_layer: int = cls._get_index_offset_for_layer(layer_index)
        in_layer_index: int = index - index_offset_for_layer
        return cls(layer_index, in_layer_index, schema)

    @staticmethod
    def _get_index_offset_for_layer(layer_index: int) -> int:
        index_offset_for_area_a = 1
        sum_of_previous_layer_indices: int = (layer_index * (layer_index - 1)) // 2
        index_offset_for_layer: int = sum_of_previous_layer_indices * 5 + index_offset_for_area_a
        return index_offset_for_layer
