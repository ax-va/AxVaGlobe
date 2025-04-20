from core.schema.base_node import BaseNode


class _NodeB(BaseNode):
    @classmethod
    def create_node_by_index(
            cls,
            index: int,
            schema,  # type: "Schema"
    ):
        number_of_nodes_in_layer = schema.constants.border_ab.nodes.NUMBER
        relative_layer_index = (index - schema.constants.area_b.nodes.START) // number_of_nodes_in_layer
        layer_index = schema.constants.area_b.node_layers.START + relative_layer_index
        index_offset_for_layer = schema.constants.area_b.nodes.START + relative_layer_index * number_of_nodes_in_layer
        in_layer_index: int = index - index_offset_for_layer
        return cls(layer_index, in_layer_index, schema)
