from typing import Self

from axvaglobe.core.schema.constants import Constants
from axvaglobe.core.schema.nodes._base_node import _BaseNode


class _NodeSP(_BaseNode):
    """
    Class for the South Pole node.
    The class is private because the constructor parameters are not validated.
    Instances of the class must only be created through the factory method, which performs validation.
    """

    @classmethod
    def create_node_by_index(
        cls,
        index: int,
        constants: Constants,
    ) -> Self:
        layer_index: int = constants.south_pole.node_layer.INDEX
        in_layer_index = 0
        return cls(layer_index, in_layer_index, constants)
