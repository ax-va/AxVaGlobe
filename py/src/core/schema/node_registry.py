from typing import Dict

from core.schema.constants import Constants
from core.schema.errors import NodeIndexError
from core.schema.node import Node
from core.schema.node_a import NodeA
from core.schema.node_ab import NodeAB
from core.schema.node_b import NodeB
from core.schema.node_bc import NodeBC
from core.schema.node_c import NodeC
from core.schema.node_np import NodeNP
from core.schema.node_sp import NodeSP


class NodeRegistry:
    _registry: Dict[int, Dict[int, Node]] = {}

    @classmethod
    def get_node_by_index(
        cls,
        node_index: int,
        constants: Constants,
    ) -> Node:

        if constants.PARTITION not in cls._registry:
            cls._registry[constants.PARTITION] = {}

        p_registry: Dict[int, Node] = cls._registry[constants.PARTITION]
        if node_index not in p_registry:
            # The node instance is not available in the registry.
            # Create a new node instance.
            node = cls._create_node_by_index(node_index, constants)
            # Add the new node instance to the registry
            p_registry[node_index] = node

        else:
            # Get the node instance from the registry
            node = p_registry[node_index]

        return node

    @classmethod
    def _create_node_by_index(
        cls,
        node_index: int,
        constants: Constants,
    ) -> Node:
        # Select the correct node class
        if constants.area_b.nodes.START <= node_index <= constants.area_b.nodes.END:
            node_cls = NodeB

        elif constants.area_a.nodes.START <= node_index <= constants.area_a.nodes.END:
            node_cls = NodeA

        elif constants.area_c.nodes.START <= node_index <= constants.area_c.nodes.END:
            node_cls = NodeC

        elif constants.border_ab.nodes.START <= node_index <= constants.border_ab.nodes.END:
            node_cls = NodeAB

        elif constants.border_bc.nodes.START <= node_index <= constants.border_bc.nodes.END:
            node_cls = NodeBC

        elif node_index == constants.north_pole.node.INDEX:
            node_cls = NodeNP

        elif node_index == constants.south_pole.node.INDEX:
            node_cls = NodeSP

        else:
            start_index: int = constants.north_pole.node.INDEX
            end_index: int = constants.south_pole.node.INDEX
            partition: int = constants.PARTITION
            raise NodeIndexError(node_index, start_index, end_index, partition)

        # Create a new node instance by using a selected class
        node = node_cls.create_node_by_index(node_index, constants)

        return node