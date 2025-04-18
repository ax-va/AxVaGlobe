from core.schema.constants import Constants
from core.schema.node_layer_a import NodeLayerA
from core.schema.node_layer_ab import NodeLayerAB
from core.schema.node_layer_b import NodeLayerB


class Schema:
    def __init__(self, partition: int):
        self.constants = Constants(partition)
        self._registry = {
            "node_layers": {},
        }

    def get_node_layer_from_registry(
            self,
            node_layer_index: int,
    ) -> NodeLayerA | NodeLayerAB | NodeLayerB:

        if node_layer_index in self._registry["node_layers"]:
            # Get the node layer instance from the registry
            node_layer = self._registry["node_layers"][node_layer_index]
        
        else:
            # The node layer instance is not available in the registry.
            # Select the correct node layer class.
            if self.constants.area_b.node_layers.START <= node_layer_index <= self.constants.area_b.node_layers.END:
                node_layer_cls = NodeLayerB

            elif self.constants.area_a.node_layers.START <= node_layer_index <= self.constants.area_a.node_layers.END:
                node_layer_cls = NodeLayerA

            elif node_layer_index == self.constants.border_ab.node_layer.INDEX:
                node_layer_cls = NodeLayerAB

            else:
                raise NotImplementedError()

            # Create a new node layer instance
            node_layer = node_layer_cls(node_layer_index, self)
            # Add the new node layer instance to the registry
            self._registry["node_layers"][node_layer_index] = node_layer

        return node_layer

    def __repr__(self):
        return f"Schema({self.constants.PARTITION})"
