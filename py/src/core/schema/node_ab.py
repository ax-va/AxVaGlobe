from typing import Self

from core.schema.base_node import BaseNode
from core.schema.constants import Constants


class NodeAB(BaseNode):
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
