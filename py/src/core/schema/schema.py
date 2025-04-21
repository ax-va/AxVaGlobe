from core.schema.constants import Constants
from core.schema.errors import NodeLayerIndexError, NodeIndexError
from core.schema.node_a import _NodeA
from core.schema.node_ab import _NodeAB
from core.schema.node_b import _NodeB
from core.schema.node_bc import _NodeBC
from core.schema.node_c import _NodeC
from core.schema.node_layer_a import _NodeLayerA
from core.schema.node_layer_ab import _NodeLayerAB
from core.schema.node_layer_b import _NodeLayerB
from core.schema.node_layer_bc import _NodeLayerBC
from core.schema.node_layer_c import _NodeLayerC
from core.schema.node_layer_np import _NodeLayerNP
from core.schema.node_layer_sp import _NodeLayerSP
from core.schema.node_np import _NodeNP
from core.schema.node_sp import _NodeSP


class Schema:
    def __init__(self, partition: int):
        self.constants = Constants(partition)
        self._registry = {
            "nodes": {},
            "node_layers": {},
        }

    @property
    def registry(self) -> dict[str, dict]:
        return self._registry

    def get_node_layer(
            self,
            node_layer_index: int,
    ) -> _NodeLayerA | _NodeLayerAB | _NodeLayerB | _NodeLayerBC | _NodeLayerC:

        node_layer_dict = self._registry["node_layers"]
        if node_layer_index in node_layer_dict:
            # Get the node layer instance from the registry
            node_layer = node_layer_dict[node_layer_index]
        
        else:
            # The node layer instance is not available in the registry.
            # Create a new node layer instance.
            node_layer = self._create_node_layer(node_layer_index)
            # Add the new node layer instance to the registry
            node_layer_dict[node_layer_index] = node_layer

        return node_layer

    def get_node(
        self,
        node_index: int,
    ) -> _NodeNP | _NodeA | _NodeAB | _NodeB | _NodeBC | _NodeC | _NodeSP:

        node_dict = self._registry["nodes"]
        if node_index in node_dict:
            # Get the node instance from the registry
            node = node_dict[node_index]

        else:
            # The node instance is not available in the registry.
            # Create a new node instance.
            node = self._create_node(node_index)
            # Add the new node instance to the registry
            node_dict[node_index] = node

        return node

    def _create_node_layer(
            self,
            node_layer_index: int,
    ) -> _NodeLayerA | _NodeLayerAB | _NodeLayerB | _NodeLayerBC | _NodeLayerC:
        # Select the correct node layer class
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

    def _create_node(
            self,
            node_index: int,
    ) -> _NodeNP | _NodeA | _NodeAB | _NodeB | _NodeBC | _NodeC | _NodeSP:
        # Select the correct node class
        if self.constants.area_b.nodes.START <= node_index <= self.constants.area_b.nodes.END:
            node_cls = _NodeB

        elif self.constants.area_a.nodes.START <= node_index <= self.constants.area_a.nodes.END:
            node_cls = _NodeA

        elif self.constants.area_c.nodes.START <= node_index <= self.constants.area_c.nodes.END:
            node_cls = _NodeC

        elif self.constants.border_ab.nodes.START <= node_index <= self.constants.border_ab.nodes.END:
            node_cls = _NodeAB

        elif self.constants.border_bc.nodes.START <= node_index <= self.constants.border_bc.nodes.END:
            node_cls = _NodeBC

        elif node_index == self.constants.north_pole.node.INDEX:
            node_cls = _NodeNP

        elif node_index == self.constants.south_pole.node.INDEX:
            node_cls = _NodeSP

        else:
            raise NodeIndexError(node_index, self)

        # Create a new node instance by using a selected class
        node = node_cls.create_node_by_index(node_index, self)
        return node

    def __repr__(self):
        return f"Schema({self.constants.PARTITION})"
