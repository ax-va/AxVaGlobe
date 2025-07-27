from typing import Self

from core.schema.nodes.base_node import _BaseNode
from core.schema.constants import Constants


class _NodeAB(_BaseNode):
    @classmethod
    def create_node_by_index(
        cls,
        index: int,
        constants: Constants,
    ) -> Self:
        layer_index: int = constants.border_ab.node_layer.INDEX
        index_offset_for_layer: int = constants.border_ab.nodes.START
        in_layer_index: int = index - index_offset_for_layer
        return cls(layer_index, in_layer_index, constants)
