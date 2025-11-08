from functools import lru_cache

from axvaglobe.core.schema.constants import Constants
from axvaglobe.core.schema._node_a import _NodeA
from axvaglobe.core.schema._node_ab import _NodeAB
from axvaglobe.core.schema._node_b import _NodeB
from axvaglobe.core.schema._node_bc import _NodeBC
from axvaglobe.core.schema._node_c import _NodeC
from axvaglobe.core.schema._node_np import _NodeNP
from axvaglobe.core.schema._node_sp import _NodeSP
from axvaglobe.core.schema.node_errors import NodeIndexError

# union alias
Node = _NodeNP | _NodeA | _NodeAB | _NodeB | _NodeBC | _NodeC | _NodeSP


class NodeFactory:
    @classmethod
    @lru_cache(maxsize=None)
    def create_node_by_index(
        cls,
        partition: int,
        index: int,
    ) -> Node:

        # cached constants
        constants: Constants = Constants.get_constants(partition=partition)

        # Select the correct node class
        if constants.area_b.nodes.START <= index <= constants.area_b.nodes.END:
            node_cls = _NodeB

        elif constants.area_a.nodes.START <= index <= constants.area_a.nodes.END:
            node_cls = _NodeA

        elif constants.area_c.nodes.START <= index <= constants.area_c.nodes.END:
            node_cls = _NodeC

        elif (
            constants.border_ab.nodes.START
            <= index
            <= constants.border_ab.nodes.END
        ):
            node_cls = _NodeAB

        elif (
            constants.border_bc.nodes.START
            <= index
            <= constants.border_bc.nodes.END
        ):
            node_cls = _NodeBC

        elif index == constants.north_pole.node.INDEX:
            node_cls = _NodeNP

        elif index == constants.south_pole.node.INDEX:
            node_cls = _NodeSP

        else:
            start_index: int = constants.north_pole.node.INDEX
            end_index: int = constants.south_pole.node.INDEX
            partition: int = constants.PARTITION
            raise NodeIndexError(index, start_index, end_index, partition)

        # Create a new node instance by using a selected class
        node = node_cls.create_node_by_index(
            partition=partition,
            index=index,
        )

        return node
