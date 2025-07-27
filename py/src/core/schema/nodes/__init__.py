from typing import Union

from core.schema.nodes.node_a import _NodeA
from core.schema.nodes.node_ab import _NodeAB
from core.schema.nodes.node_b import _NodeB
from core.schema.nodes.node_bc import _NodeBC
from core.schema.nodes.node_c import _NodeC
from core.schema.nodes.node_np import _NodeNP
from core.schema.nodes.node_sp import _NodeSP

# union alias
Node = Union[
    _NodeNP,
    _NodeA,
    _NodeAB,
    _NodeB,
    _NodeBC,
    _NodeC,
    _NodeSP,
]