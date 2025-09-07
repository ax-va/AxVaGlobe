from typing import Self

from axvaglobe.core.schema.constants import Constants
from axvaglobe.core.schema.nodes.base_node import _BaseNode


class _NodeBC(_BaseNode):
    @classmethod
    def create_node_by_index(
        cls,
        index: int,
        constants: Constants,
    ) -> Self:
        layer_index: int = constants.border_bc.node_layer.INDEX
        index_offset_for_layer: int = constants.border_bc.nodes.START
        in_layer_index: int = index - index_offset_for_layer
        return cls(layer_index, in_layer_index, constants)
