from typing import Union

from core.schema.node_a import NodeA
from core.schema.node_ab import NodeAB
from core.schema.node_b import NodeB
from core.schema.node_bc import NodeBC
from core.schema.node_c import NodeC
from core.schema.node_np import NodeNP
from core.schema.node_sp import NodeSP

# union alias
Node = Union[
    NodeNP,
    NodeA,
    NodeAB,
    NodeB,
    NodeBC,
    NodeC,
    NodeSP,
]