from typing import Dict

from core.schema.constants import Constants
from core.schema.errors import NodeLayerIndexError
from core.schema.node_layer import NodeLayer
from core.schema.node_layer_a import NodeLayerA
from core.schema.node_layer_ab import NodeLayerAB
from core.schema.node_layer_b import NodeLayerB
from core.schema.node_layer_bc import NodeLayerBC
from core.schema.node_layer_c import NodeLayerC
from core.schema.node_layer_np import NodeLayerNP
from core.schema.node_layer_sp import NodeLayerSP


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
            node_layer: NodeLayer = cls._create_node_layer(node_layer_index, constants)
            # Add the new node layer instance to the registry
            p_registry[node_layer_index] = node_layer

        else:
            # Get the node layer instance from the registry
            node_layer: NodeLayer = p_registry[node_layer_index]

        return node_layer

    @classmethod
    def _create_node_layer(
        cls,
        node_layer_index: int,
        constants: Constants,
    ) -> NodeLayer:
        # Select the correct node layer class
        if constants.area_b.node_layers.START <= node_layer_index <= constants.area_b.node_layers.END:
            node_layer_cls = NodeLayerB

        elif constants.area_a.node_layers.START <= node_layer_index <= constants.area_a.node_layers.END:
            node_layer_cls = NodeLayerA

        elif constants.area_c.node_layers.START <= node_layer_index <= constants.area_c.node_layers.END:
            node_layer_cls = NodeLayerC

        elif node_layer_index == constants.border_ab.node_layer.INDEX:
            node_layer_cls = NodeLayerAB

        elif node_layer_index == constants.border_bc.node_layer.INDEX:
            node_layer_cls = NodeLayerBC

        elif node_layer_index == constants.north_pole.node_layer.INDEX:
            node_layer_cls = NodeLayerNP

        elif node_layer_index == constants.south_pole.node_layer.INDEX:
            node_layer_cls = NodeLayerSP

        else:
            start_index: int = constants.north_pole.node_layer.INDEX
            end_index: int = constants.south_pole.node_layer.INDEX
            partition: int = constants.PARTITION
            raise NodeLayerIndexError(node_layer_index, start_index, end_index, partition)

        # Create a new node layer instance by using a selected class
        node_layer: NodeLayer = node_layer_cls(node_layer_index, constants)

        return node_layer