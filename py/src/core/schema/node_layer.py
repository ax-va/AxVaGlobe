from typing import Union

from core.schema.node_layer_a import NodeLayerA
from core.schema.node_layer_ab import NodeLayerAB
from core.schema.node_layer_b import NodeLayerB
from core.schema.node_layer_bc import NodeLayerBC
from core.schema.node_layer_c import NodeLayerC
from core.schema.node_layer_np import NodeLayerNP
from core.schema.node_layer_sp import NodeLayerSP

# union alias
NodeLayer = Union[
    NodeLayerNP,
    NodeLayerA,
    NodeLayerAB,
    NodeLayerB,
    NodeLayerBC,
    NodeLayerC,
    NodeLayerSP,
]