from typing import Union

from axvaglobe.core.schema.nodes.node_a import _NodeA
from axvaglobe.core.schema.nodes.node_ab import _NodeAB
from axvaglobe.core.schema.nodes.node_b import _NodeB
from axvaglobe.core.schema.nodes.node_bc import _NodeBC
from axvaglobe.core.schema.nodes.node_c import _NodeC
from axvaglobe.core.schema.nodes.node_np import _NodeNP
from axvaglobe.core.schema.nodes.node_sp import _NodeSP

# union alias
Node = _NodeNP | _NodeA | _NodeAB | _NodeB | _NodeBC | _NodeC | _NodeSP
