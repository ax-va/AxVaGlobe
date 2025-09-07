from axvaglobe.core.schema.constants import Constants
from axvaglobe.core.schema.errors import NodeIndexError
from axvaglobe.core.schema.nodes import Node
from axvaglobe.core.schema.nodes.node_a import _NodeA
from axvaglobe.core.schema.nodes.node_ab import _NodeAB
from axvaglobe.core.schema.nodes.node_b import _NodeB
from axvaglobe.core.schema.nodes.node_bc import _NodeBC
from axvaglobe.core.schema.nodes.node_c import _NodeC
from axvaglobe.core.schema.nodes.node_np import _NodeNP
from axvaglobe.core.schema.nodes.node_sp import _NodeSP


class NodeFactory:
    @classmethod
    def create_node_by_index(
        cls,
        node_index: int,
        constants: Constants,
    ) -> Node:
        # Select the correct node class
        if constants.area_b.nodes.START <= node_index <= constants.area_b.nodes.END:
            node_cls = _NodeB

        elif constants.area_a.nodes.START <= node_index <= constants.area_a.nodes.END:
            node_cls = _NodeA

        elif constants.area_c.nodes.START <= node_index <= constants.area_c.nodes.END:
            node_cls = _NodeC

        elif (
            constants.border_ab.nodes.START
            <= node_index
            <= constants.border_ab.nodes.END
        ):
            node_cls = _NodeAB

        elif (
            constants.border_bc.nodes.START
            <= node_index
            <= constants.border_bc.nodes.END
        ):
            node_cls = _NodeBC

        elif node_index == constants.north_pole.node.INDEX:
            node_cls = _NodeNP

        elif node_index == constants.south_pole.node.INDEX:
            node_cls = _NodeSP

        else:
            start_index: int = constants.north_pole.node.INDEX
            end_index: int = constants.south_pole.node.INDEX
            partition: int = constants.PARTITION
            raise NodeIndexError(node_index, start_index, end_index, partition)

        # Create a new node instance by using a selected class
        node = node_cls.create_node_by_index(node_index, constants)

        return node
