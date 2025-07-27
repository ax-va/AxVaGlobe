from typing import Union

from core.schema.node_layers.node_layer_a import _NodeLayerA
from core.schema.node_layers.node_layer_ab import _NodeLayerAB
from core.schema.node_layers.node_layer_b import _NodeLayerB
from core.schema.node_layers.node_layer_bc import _NodeLayerBC
from core.schema.node_layers.node_layer_c import _NodeLayerC
from core.schema.node_layers.node_layer_np import _NodeLayerNP
from core.schema.node_layers.node_layer_sp import _NodeLayerSP

# union alias
NodeLayer = Union[
    _NodeLayerNP,
    _NodeLayerA,
    _NodeLayerAB,
    _NodeLayerB,
    _NodeLayerBC,
    _NodeLayerC,
    _NodeLayerSP,
]