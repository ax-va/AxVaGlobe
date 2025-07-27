from typing import Dict

from core.schema.constants import Constants
from core.schema.nodes import Node
from core.schema.node_factory import NodeFactory


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
            node = NodeFactory.create_node_by_index(node_index, constants)
            # Add the new node instance to the registry
            p_registry[node_index] = node

        else:
            # Get the node instance from the registry
            node = p_registry[node_index]

        return node
