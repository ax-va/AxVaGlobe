from axvaglobe.core.schema.nodes._node_a import _NodeA
from axvaglobe.core.schema.nodes._node_ab import _NodeAB
from axvaglobe.core.schema.nodes._node_b import _NodeB
from axvaglobe.core.schema.nodes._node_bc import _NodeBC
from axvaglobe.core.schema.nodes._node_c import _NodeC
from axvaglobe.core.schema.nodes._node_np import _NodeNP
from axvaglobe.core.schema.nodes._node_sp import _NodeSP

# union alias
Node = _NodeNP | _NodeA | _NodeAB | _NodeB | _NodeBC | _NodeC | _NodeSP
