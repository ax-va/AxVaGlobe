from axvaglobe.core.schema.constants import Constants
from axvaglobe.core.schema.node_registry import NodeRegistry
from axvaglobe.core.schema.nodes import Node


class Schema:
    def __init__(self, partition: int):
        self.constants = Constants(partition)

    def get_node_by_its_index(self, node_index: int) -> Node:
        node: Node = NodeRegistry.get_node_by_its_index(node_index, self.constants)
        return node

    def __repr__(self):
        return f"Schema({self.constants.PARTITION})"
