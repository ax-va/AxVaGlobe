from functools import lru_cache

from axvaglobe.core.schema.constants import Constants
from axvaglobe.core.schema._node_layer_a import _NodeLayerA
from axvaglobe.core.schema._node_layer_ab import _NodeLayerAB
from axvaglobe.core.schema._node_layer_b import _NodeLayerB
from axvaglobe.core.schema._node_layer_bc import _NodeLayerBC
from axvaglobe.core.schema._node_layer_c import _NodeLayerC
from axvaglobe.core.schema._node_layer_np import _NodeLayerNP
from axvaglobe.core.schema._node_layer_sp import _NodeLayerSP
from axvaglobe.core.schema.node_layer_errors import NodeLayerIndexError

# union alias
NodeLayer = (
    _NodeLayerNP
    | _NodeLayerA
    | _NodeLayerAB
    | _NodeLayerB
    | _NodeLayerBC
    | _NodeLayerC
    | _NodeLayerSP
)


class NodeLayerFactory:
    @classmethod
    @lru_cache(maxsize=None)
    def create_node_layer_by_layer_index(
        cls,
        partition: int,
        layer_index: int,
    ) -> NodeLayer:

        # cached constants
        constants: Constants = Constants.get_constants(partition=partition)

        # Select the correct node layer class
        if (
            constants.area_b.node_layers.START
            <= layer_index
            <= constants.area_b.node_layers.END
        ):
            node_layer_cls = _NodeLayerB

        elif (
            constants.area_a.node_layers.START
            <= layer_index
            <= constants.area_a.node_layers.END
        ):
            node_layer_cls = _NodeLayerA

        elif (
            constants.area_c.node_layers.START
            <= layer_index
            <= constants.area_c.node_layers.END
        ):
            node_layer_cls = _NodeLayerC

        elif layer_index == constants.border_ab.node_layer.INDEX:
            node_layer_cls = _NodeLayerAB

        elif layer_index == constants.border_bc.node_layer.INDEX:
            node_layer_cls = _NodeLayerBC

        elif layer_index == constants.north_pole.node_layer.INDEX:
            node_layer_cls = _NodeLayerNP

        elif layer_index == constants.south_pole.node_layer.INDEX:
            node_layer_cls = _NodeLayerSP

        else:
            start_index: int = constants.north_pole.node_layer.INDEX
            end_index: int = constants.south_pole.node_layer.INDEX
            partition: int = constants.PARTITION
            raise NodeLayerIndexError(
                layer_index, start_index, end_index, partition
            )

        # Create a new node layer instance by using a selected class
        node_layer: NodeLayer = node_layer_cls(
            partition=partition,
            index=layer_index,
        )

        return node_layer
