from core.schema.constants import Constants
from core.schema.errors import NodeLayerIndexError
from core.schema.node_layer_a import _NodeLayerA
from core.schema.node_layer_ab import _NodeLayerAB
from core.schema.node_layer_b import _NodeLayerB
from core.schema.node_layer_bc import _NodeLayerBC
from core.schema.node_layer_c import _NodeLayerC
from core.schema.node_layer_np import _NodeLayerNP
from core.schema.node_layer_sp import _NodeLayerSP


class Schema:
    def __init__(self, partition: int):
        self.constants = Constants(partition)
        self._registry = {
            "node_layers": {},
        }

    def get_node_layer(
            self,
            node_layer_index: int,
    ) -> _NodeLayerA | _NodeLayerAB | _NodeLayerB | _NodeLayerBC | _NodeLayerC:

        if node_layer_index in self._registry["node_layers"]:
            # Get the node layer instance from the registry
            node_layer = self._registry["node_layers"][node_layer_index]
        
        else:
            # The node layer instance is not available in the registry.
            # Create a new node layer instance.
            node_layer = self._create_node_layer(node_layer_index)
            # Add the new node layer instance to the registry
            self._registry["node_layers"][node_layer_index] = node_layer

        return node_layer


    def _create_node_layer(
            self,
            node_layer_index: int,
    ) -> _NodeLayerA | _NodeLayerAB | _NodeLayerB | _NodeLayerBC | _NodeLayerC:
        # Select the correct node layer class.
        if self.constants.area_b.node_layers.START <= node_layer_index <= self.constants.area_b.node_layers.END:
            node_layer_cls = _NodeLayerB

        elif self.constants.area_a.node_layers.START <= node_layer_index <= self.constants.area_a.node_layers.END:
            node_layer_cls = _NodeLayerA

        elif self.constants.area_c.node_layers.START <= node_layer_index <= self.constants.area_c.node_layers.END:
            node_layer_cls = _NodeLayerC

        elif node_layer_index == self.constants.border_ab.node_layer.INDEX:
            node_layer_cls = _NodeLayerAB

        elif node_layer_index == self.constants.border_bc.node_layer.INDEX:
            node_layer_cls = _NodeLayerBC

        elif node_layer_index == self.constants.north_pole.node_layer.INDEX:
            node_layer_cls = _NodeLayerNP

        elif node_layer_index == self.constants.south_pole.node_layer.INDEX:
            node_layer_cls = _NodeLayerSP

        else:
            raise NodeLayerIndexError(node_layer_index, self)

        # Create a new node layer instance by using a selected class
        node_layer = node_layer_cls(node_layer_index, self)
        return node_layer


    def __repr__(self):
        return f"Schema({self.constants.PARTITION})"
