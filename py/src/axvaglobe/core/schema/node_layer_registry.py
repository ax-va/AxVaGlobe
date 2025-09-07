
from axvaglobe.core.schema.constants import Constants
from axvaglobe.core.schema.node_layer_factory import NodeLayerFactory
from axvaglobe.core.schema.node_layers import NodeLayer


class NodeLayerRegistry:
    _registry: dict[int, dict[int, NodeLayer]] = {}

    @classmethod
    def get_node_layer_by_layer_index(
        cls,
        node_layer_index: int,
        constants: Constants,
    ) -> NodeLayer:
        if constants.PARTITION not in cls._registry:
            cls._registry[constants.PARTITION] = {}

        partition_registry: dict[int, NodeLayer] = cls._registry[constants.PARTITION]
        if node_layer_index not in partition_registry:
            # The node layer instance is not available in the registry.
            # Create a new node layer instance.
            node_layer: NodeLayer = NodeLayerFactory.create_node_layer_by_index(
                node_layer_index, constants
            )
            # Add the new node layer instance to the registry
            partition_registry[node_layer_index] = node_layer

        else:
            # Get the node layer instance from the registry
            node_layer: NodeLayer = partition_registry[node_layer_index]

        return node_layer
