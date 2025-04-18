from core.schema.base_node import BaseNode


class NodeAB(BaseNode):
    @classmethod
    def create_node_by_index(
            cls,
            index: int,
            schema,  # type: "Schema"
    ):
        layer_index: int = schema.constants.border_ab.node_layer.INDEX
        index_offset_for_layer: int = schema.constants.border_ab.nodes.START
        in_layer_index: int = index - index_offset_for_layer
        return cls(layer_index, in_layer_index, schema)
