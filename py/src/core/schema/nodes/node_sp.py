from typing import Self

from core.schema.nodes.base_node import _BaseNode
from core.schema.constants import Constants


class _NodeSP(_BaseNode):
    """Class for the South Pole node."""
    @classmethod
    def create_node_by_index(
        cls,
        index: int,
        constants: Constants,
    ) -> Self:
        layer_index: int = constants.south_pole.node_layer.INDEX
        in_layer_index = 0
        return cls(layer_index, in_layer_index, constants)
