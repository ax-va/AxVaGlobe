from functools import lru_cache

from axvaglobe.core.schema.partition import Partition
from axvaglobe.core.schema._node_a import _NodeA
from axvaglobe.core.schema._node_ab import _NodeAB
from axvaglobe.core.schema._node_b import _NodeB
from axvaglobe.core.schema._node_bc import _NodeBC
from axvaglobe.core.schema._node_c import _NodeC
from axvaglobe.core.schema._node_np import _NodeNP
from axvaglobe.core.schema._node_sp import _NodeSP
from axvaglobe.core.schema.node_errors import NodeIndexError

# union alias
Node = _NodeNP | _NodeA | _NodeAB | _NodeB | _NodeBC | _NodeC | _NodeSP


class NodeFactory:
    @classmethod
    @lru_cache(maxsize=None)
    def get_node(
        cls,
        index: int,
        partition_obj: Partition,
    ) -> Node:
        return cls.create_node(index=index, partition_obj=partition_obj)

    @classmethod
    def create_node(
        cls,
        index: int,
        partition_obj: Partition,
    ) -> Node:

        # nodes between poles
        if (
            partition_obj.north_pole.node.INDEX
            < index
            < partition_obj.south_pole.node.INDEX
        ):
            # Select the correct node class
            if (
                partition_obj.area_b.nodes.START
                <= index
                <= partition_obj.area_b.nodes.END
            ):
                node_cls = _NodeB

            elif (
                partition_obj.area_a.nodes.START
                <= index
                <= partition_obj.area_a.nodes.END
            ):
                node_cls = _NodeA

            elif (
                partition_obj.area_c.nodes.START
                <= index <=
                partition_obj.area_c.nodes.END
            ):
                node_cls = _NodeC

            elif (
                partition_obj.border_ab.nodes.START
                <= index
                <= partition_obj.border_ab.nodes.END
            ):
                node_cls = _NodeAB

            else:
                node_cls = _NodeBC

            # Create a new node instance by using a selected class
            node = node_cls.create_node(
                index=index,
                partition_obj=partition_obj,
            )

        # poles
        else:
            if index == partition_obj.north_pole.node.INDEX:
                node_cls = _NodeNP

            elif index == partition_obj.south_pole.node.INDEX:
                node_cls = _NodeSP

            else:
                start_index: int = partition_obj.north_pole.node.INDEX
                end_index: int = partition_obj.south_pole.node.INDEX
                partition: int = partition_obj.PARTITION
                raise NodeIndexError(index, start_index, end_index, partition)

            node = node_cls.create_node(
                partition_obj=partition_obj,
            )

        return node
