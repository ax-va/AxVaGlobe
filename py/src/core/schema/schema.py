from core.schema.constants import Constants
from core.schema.nodes import Node
from core.schema.node_registry import NodeRegistry


class Schema:
    def __init__(self, partition: int):
        self.constants = Constants(partition)

    def get_node_by_index(self, node_index: int) -> Node:
        node: Node = NodeRegistry.get_node_by_index(node_index, self.constants)
        return node

    def __repr__(self):
        return f"Schema({self.constants.PARTITION})"
