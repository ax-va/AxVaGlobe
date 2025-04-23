from typing import Tuple, Self

from core.schema.base_node import BaseNode


class _NodeB(BaseNode):
    @classmethod
    def create_node_by_index(
            cls,
            index: int,
            schema,  # type: "Schema"
    ) -> Self:
        """Creates a node instance by a node index."""
        number_of_nodes_in_layer: int = schema.constants.border_ab.nodes.NUMBER
        relative_layer_index: int = (index - schema.constants.area_b.nodes.START) // number_of_nodes_in_layer
        layer_index: int = schema.constants.area_b.node_layers.START + relative_layer_index
        index_offset_for_layer: int = schema.constants.area_b.nodes.START + relative_layer_index * number_of_nodes_in_layer
        in_layer_index: int = index - index_offset_for_layer
        return cls(layer_index, in_layer_index, schema)

    def get_layer_and_in_layer_indices_of_neighboring_nodes(
            self,
    ) -> Tuple[
            # 6 neighboring nodes indices
            Tuple[int, int],  # (layer_index, in_layer_index)
            Tuple[int, int],
            Tuple[int, int],
            Tuple[int, int],
            Tuple[int, int],
            Tuple[int, int]
    ]:
        """Returns 6 neighboring nodes indices (layer_index, in_layer_index)."""
        layer_index_0: int = self.LAYER_INDEX - 1  # up
        layer_index_1: int = layer_index_0  # up
        layer_index_2: int = self.LAYER_INDEX
        layer_index_3: int = self.LAYER_INDEX + 1  # down
        layer_index_4: int = layer_index_3  # down
        layer_index_5: int = self.LAYER_INDEX

        end_node_in_layer_index = self._layer.END_NODE_IN_LAYER_INDEX
        if self.IN_LAYER_INDEX != 0:
            in_layer_index_0: int = self.IN_LAYER_INDEX - 1  # left
            in_layer_index_1: int = self.IN_LAYER_INDEX
            in_layer_index_2: int = self.IN_LAYER_INDEX + 1 if self.IN_LAYER_INDEX != end_node_in_layer_index else 0
            in_layer_index_3: int = in_layer_index_2
            in_layer_index_4: int = self.IN_LAYER_INDEX
            in_layer_index_5: int = in_layer_index_0  # left

        else:
            in_layer_index_0: int = end_node_in_layer_index
            in_layer_index_1: int = 0
            in_layer_index_2: int = 1
            in_layer_index_3: int = 1
            in_layer_index_4: int = 0
            in_layer_index_5: int = end_node_in_layer_index

        return (
            (layer_index_0, in_layer_index_0),
            (layer_index_1, in_layer_index_1),
            (layer_index_2, in_layer_index_2),
            (layer_index_3, in_layer_index_3),
            (layer_index_4, in_layer_index_4),
            (layer_index_5, in_layer_index_5),
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
