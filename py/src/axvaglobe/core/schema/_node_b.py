from typing import Self

from axvaglobe.core.schema.partition import Partition
from axvaglobe.core.schema._base_node import _BaseNode


class _NodeB(_BaseNode):
    """
    The class is private because the constructor parameters are not validated.
    Instances of the class must only be created through the factory method, which performs validation.
    """

    @classmethod
    def create_node(
        cls,
        index: int,
        partition_obj: Partition,
    ) -> Self:
        """Creates a node instance by a node index."""
        number_of_nodes_in_layer: int = partition_obj.border_ab.nodes.NUMBER
        relative_layer_index: int = (
            index - partition_obj.area_b.nodes.START
        ) // number_of_nodes_in_layer
        layer_index: int = partition_obj.area_b.node_layers.START + relative_layer_index
        index_offset_for_layer: int = (
            partition_obj.area_b.nodes.START
            + relative_layer_index * number_of_nodes_in_layer
        )
        in_layer_index: int = index - index_offset_for_layer

        node = cls(
            layer_index=layer_index,
            in_layer_index=in_layer_index,
            partition_obj=partition_obj,
        )

        return node

    def get_positions_of_neighbor_nodes(
        self,
    ) -> tuple[
        # 6 neighboring nodes indices
        tuple[int, int],  # (layer_index, in_layer_index)
        tuple[int, int],
        tuple[int, int],
        tuple[int, int],
        tuple[int, int],
        tuple[int, int],
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

        if self.IN_LAYER_INDEX != 0:
            # The node is not on the last edge
            in_layer_index_0: int = in_layer_index_left  # left
            in_layer_index_1: int = self.IN_LAYER_INDEX
            in_layer_index_2: int = (
                in_layer_index_right
                # The node is not in front of the last edge
                if self.IN_LAYER_INDEX != self._layer_obj.LAST_IN_LAYER_INDEX
                else 0
            )
            in_layer_index_3: int = in_layer_index_2
            in_layer_index_4: int = self.IN_LAYER_INDEX
            in_layer_index_5: int = in_layer_index_left  # left

        else:
            # The node is on the last edge
            in_layer_index_0: int = self._layer_obj.LAST_IN_LAYER_INDEX
            in_layer_index_1: int = 0
            in_layer_index_2: int = 1
            in_layer_index_3: int = 1
            in_layer_index_4: int = 0
            in_layer_index_5: int = self._layer_obj.LAST_IN_LAYER_INDEX

        return (
            (layer_index_0, in_layer_index_0),
            (layer_index_1, in_layer_index_1),
            (layer_index_2, in_layer_index_2),
            (layer_index_3, in_layer_index_3),
            (layer_index_4, in_layer_index_4),
            (layer_index_5, in_layer_index_5),
        )
