from core.schema.constants import Constants
from core.schema.node_layer_a import NodeLayerA


class BaseSchema:
    def __init__(self, partition: int):
        self.constants = Constants(partition)
        self._registry = {
            "node_layers": {},
        }

    def get_node_layer_from_registry(
            self,
            node_layer_index: int,
            # optional
            node_index_offset_for_layer: int = None,
    ) -> NodeLayerA:
        if node_layer_index in self._registry["node_layers"]:
            node_layer = self._registry["node_layers"][node_layer_index]
        else:
            if self.constants.area_a.node_layers.START <= node_layer_index <= self.constants.area_a.node_layers.END:
                node_layer = NodeLayerA(node_layer_index, node_index_offset_for_layer)
                self._registry["node_layers"][node_layer_index] = node_layer
            else:
                raise NotImplemented()
        return node_layer
