from typing import Dict

from core.schema.constants import Constants
from core.schema.node_layers.node_layer import NodeLayer
from core.schema.node_layer_factory import NodeLayerFactory


class NodeLayerRegistry:
    _registry: Dict[int, Dict[int, NodeLayer]] = {}

    @classmethod
    def get_node_layer(
        cls,
        node_layer_index: int,
        constants: Constants,
    ) -> NodeLayer:

        if constants.PARTITION not in cls._registry:
            cls._registry[constants.PARTITION] = {}

        p_registry: Dict[int, NodeLayer] = cls._registry[constants.PARTITION]
        if node_layer_index not in p_registry:
            # The node layer instance is not available in the registry.
            # Create a new node layer instance.
            node_layer: NodeLayer = NodeLayerFactory.create_node_layer_by_index(node_layer_index, constants)
            # Add the new node layer instance to the registry
            p_registry[node_layer_index] = node_layer

        else:
            # Get the node layer instance from the registry
            node_layer: NodeLayer = p_registry[node_layer_index]

        return node_layer
