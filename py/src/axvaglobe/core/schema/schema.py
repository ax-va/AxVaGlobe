from axvaglobe.core.schema.errors import PartitionValueError
from axvaglobe.core.schema.nodes import Node
from axvaglobe.core.schema.nodes.node_factory import NodeFactory


class Schema:
    def __init__(self, partition: int):
        if not isinstance(partition, int) or partition < 2:
            raise PartitionValueError(partition)

        self._partition = partition

    @property
    def partition(self) -> int:
        return self._partition

    def get_node_by_index(self, node_index: int) -> Node:
        # cached creation
        node: Node = NodeFactory.create_node_by_index(
            partition=self._partition,
            node_index=node_index,
        )
        return node

    def __repr__(self):
        return f"Schema({self._partition})"
