from core.schema.base_node import BaseNode


class _NodeSP(BaseNode):
    """Class for the South Pole node."""
    @classmethod
    def create_node_by_index(
            cls,
            index: int,
            schema,  # type: "Schema"
    ):
        layer_index: int = schema.constants.south_pole.node_layer.INDEX
        in_layer_index = 0
        return cls(layer_index, in_layer_index, schema)
