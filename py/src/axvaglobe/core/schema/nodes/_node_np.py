from typing import Self

from axvaglobe.core.schema.constants import Constants
from axvaglobe.core.schema.nodes._base_node import _BaseNode


class _NodeNP(_BaseNode):
    """
    Class for the North Pole node.
    The class is private because the constructor parameters are not validated.
    Instances of the class must only be created through the factory method, which performs validation.
    """

    @classmethod
    def create_node_by_index(
        cls,
        partition: int,
        index: int,
    ) -> Self:
        constants: Constants = Constants.get_constants(partition=partition)
        layer_index: int = constants.north_pole.node_layer.INDEX
        in_layer_index = 0

        node = cls(
            partition=partition,
            layer_index=layer_index,
            in_layer_index=in_layer_index,
        )

        return node
