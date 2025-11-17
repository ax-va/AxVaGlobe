from functools import lru_cache
from typing import Self

from axvaglobe.core.schema.partition import Partition
from axvaglobe.core.schema.errors import PartitionValueError
from axvaglobe.core.schema.node_factory import NodeFactory, Node


class Schema:
    def __init__(self, partition: int):
        if not isinstance(partition, int) or partition < 2:
            raise PartitionValueError(partition)

        # cached object
        self._partition_obj: Partition = Partition.get_partition_obj(partition=partition)

    @property
    def partition(self) -> int:
        return self._partition_obj.PARTITION

    @classmethod
    @lru_cache(maxsize=None)
    def get_schema(
        cls,
        partition: int,
    ) -> Self:
        return Schema(partition=partition)

    def get_node(self, index: int) -> Node:
        # cached object
        node: Node = NodeFactory.get_node(
            index=index,
            partition_obj=self._partition_obj,
        )
        return node

    def __repr__(self):
        return f"{type(self).__name__}(partition={self._partition_obj.PARTITION})"
