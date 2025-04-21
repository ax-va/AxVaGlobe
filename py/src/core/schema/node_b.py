from typing import Tuple, Self

from core.schema.base_node import BaseNode


class _NodeB(BaseNode):
    @classmethod
    def create_node_by_index(
            cls,
            index: int,
            schema,  # type: "Schema"
    ) -> Self:
        number_of_nodes_in_layer = schema.constants.border_ab.nodes.NUMBER
        relative_layer_index = (index - schema.constants.area_b.nodes.START) // number_of_nodes_in_layer
        layer_index = schema.constants.area_b.node_layers.START + relative_layer_index
        index_offset_for_layer = schema.constants.area_b.nodes.START + relative_layer_index * number_of_nodes_in_layer
        in_layer_index: int = index - index_offset_for_layer
        return cls(layer_index, in_layer_index, schema)

    def get_layer_and_in_layer_indices_of_neighboring_nodes(
            self,
    ) -> Tuple[
            Tuple[int, int],
            Tuple[int, int],
            Tuple[int, int],
            Tuple[int, int],
            Tuple[int, int],
            Tuple[int, int]
    ]:

        layer_index0 = self.LAYER_INDEX - 1  # layer index up
        layer_index1 = self.LAYER_INDEX - 1  # layer index up
        layer_index2 = self.LAYER_INDEX
        layer_index3 = self.LAYER_INDEX + 1  # layer index down
        layer_index4 = self.LAYER_INDEX + 1  # layer index down
        layer_index5 = self.LAYER_INDEX

        end_node_in_layer_index = self._layer.END_NODE_IN_LAYER_INDEX
        if self.IN_LAYER_INDEX != 0:
            in_layer_index0 = self.IN_LAYER_INDEX - 1
            in_layer_index1 = self.IN_LAYER_INDEX
            in_layer_index2 = self.IN_LAYER_INDEX + 1 if self.IN_LAYER_INDEX != end_node_in_layer_index else 0
            in_layer_index3 = in_layer_index2
            in_layer_index4 = self.IN_LAYER_INDEX
            in_layer_index5 = in_layer_index0

        else:
            in_layer_index0 = end_node_in_layer_index
            in_layer_index1 = 0
            in_layer_index2 = 1
            in_layer_index3 = 1
            in_layer_index4 = 0
            in_layer_index5 = end_node_in_layer_index

        return (
            (layer_index0, in_layer_index0),
            (layer_index1, in_layer_index1),
            (layer_index2, in_layer_index2),
            (layer_index3, in_layer_index3),
            (layer_index4, in_layer_index4),
            (layer_index5, in_layer_index5),
        )


if __name__ == "__main__":
    from core.schema.schema import Schema
    schema = Schema(4)
    for index in range(schema.constants.area_b.nodes.START, schema.constants.area_b.nodes.END + 1):
        node = _NodeB.create_node_by_index(index, schema)
        print("-" * 20)
        print(node.INDEX)
        print("neighbors:")
        for layer_index, in_layer_index in node.get_layer_and_in_layer_indices_of_neighboring_nodes():
            nn = _NodeB(layer_index, in_layer_index, schema)
            print(nn.INDEX)
