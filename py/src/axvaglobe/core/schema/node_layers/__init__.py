from axvaglobe.core.schema.node_layers._node_layer_a import _NodeLayerA
from axvaglobe.core.schema.node_layers._node_layer_ab import _NodeLayerAB
from axvaglobe.core.schema.node_layers._node_layer_b import _NodeLayerB
from axvaglobe.core.schema.node_layers._node_layer_bc import _NodeLayerBC
from axvaglobe.core.schema.node_layers._node_layer_c import _NodeLayerC
from axvaglobe.core.schema.node_layers._node_layer_np import _NodeLayerNP
from axvaglobe.core.schema.node_layers._node_layer_sp import _NodeLayerSP

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
