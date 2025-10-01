from typing import Self

from axvaglobe.core.schema.constants import Constants
from axvaglobe.core.schema.nodes._base_node import _BaseNode


class _NodeAB(_BaseNode):
    """
    The class is private because the constructor parameters are not validated.
    Instances of the class must only be created through the factory method, which performs validation.
    """

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
