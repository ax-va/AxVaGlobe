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
        layer_index_up: int = self.LAYER_INDEX - 1
        layer_index_down: int = self.LAYER_INDEX + 1
        in_layer_index_left: int = self.IN_LAYER_INDEX - 1
        in_layer_index_right: int = self.IN_LAYER_INDEX + 1

        layer_index_0: int = layer_index_up  # up
        layer_index_1: int = layer_index_up  # up
        layer_index_2: int = self.LAYER_INDEX
        layer_index_3: int = layer_index_down  # down
        layer_index_4: int = layer_index_down  # down
        layer_index_5: int = self.LAYER_INDEX

        end_node_in_layer_index = self._layer.END_NODE_IN_LAYER_INDEX
        if self.IN_LAYER_INDEX != 0:
            in_layer_index_0: int = in_layer_index_left  # left
            in_layer_index_1: int = self.IN_LAYER_INDEX
            in_layer_index_2: int = in_layer_index_right if self.IN_LAYER_INDEX != end_node_in_layer_index else 0
            in_layer_index_3: int = in_layer_index_2
            in_layer_index_4: int = self.IN_LAYER_INDEX
            in_layer_index_5: int = in_layer_index_left  # left

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
