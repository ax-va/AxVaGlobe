from typing import Self

from core.schema.base_node import BaseNode
from core.schema.constants import Constants


class NodeNP(BaseNode):
    """Class for the North Pole node."""
    @classmethod
    def create_node_by_index(
        cls,
        index: int,
        constants: Constants,
    ) -> Self:
        layer_index: int = constants.north_pole.node_layer.INDEX
        in_layer_index = 0
        return cls(layer_index, in_layer_index, constants)
