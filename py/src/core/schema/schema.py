from core.schema.constants import Constants
from core.schema.node import Node
from core.schema.node_layer import NodeLayer
from core.schema.node_layer_registry import NodeLayerRegistry
from core.schema.node_registry import NodeRegistry


class Schema:
    def __init__(self, partition: int):
        self.constants = Constants(partition)

    def get_node_layer(self, node_layer_index: int) -> NodeLayer:
        node_layer: NodeLayer = NodeLayerRegistry.get_node_layer(node_layer_index, self.constants)
        return node_layer

    def get_node_by_index(self, node_index: int) -> Node:
        node: Node = NodeRegistry.get_node(node_index, self.constants)
        return node

    def __repr__(self):
        return f"Schema({self.constants.PARTITION})"
