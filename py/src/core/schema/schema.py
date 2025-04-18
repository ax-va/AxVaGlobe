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
            # Get the stored item from the registry
            node_layer: NodeLayerA | NodeLayerAB | NodeLayerB = self._registry["node_layers"][node_layer_index]
        
        else:
            if self.constants.area_b.node_layers.START <= node_layer_index <= self.constants.area_b.node_layers.END:
                node_layer = NodeLayerB(node_layer_index, self)

            elif self.constants.area_a.node_layers.START <= node_layer_index <= self.constants.area_a.node_layers.END:
                node_layer = NodeLayerA(node_layer_index, self)

            elif node_layer_index == self.constants.border_ab.node_layer.INDEX:
                node_layer = NodeLayerAB(node_layer_index, self)

            else:
                raise NotImplementedError()

            # Add the new item to the registry
            self._registry["node_layers"][node_layer_index] = node_layer

        return node_layer

    def __repr__(self):
        return f"Schema({self.constants.PARTITION})"
