from abc import ABC, abstractmethod
from typing import Self

from axvaglobe.core.schema.partition import Partition
from axvaglobe.core.schema.node_layer_factory import NodeLayerFactory, NodeLayer


class _BaseNode(ABC):
    """
    The class is private because the constructor parameters are not validated.
    """

    def __init__(
        self,
        layer_index: int,
        in_layer_index: int,
        partition_obj: Partition,
    ):
        self._partition_obj = partition_obj
        # cached creation
        self._layer_obj: NodeLayer = NodeLayerFactory.get_node_layer(
            layer_index=layer_index,
            partition_obj=self._partition_obj,
        )
        self._in_layer_index: int = in_layer_index
        # lazy
        self._index: int | None = None

    @property
    def LAYER_INDEX(self) -> int:
        return self._layer_obj.INDEX

    @property
    def IN_LAYER_INDEX(self) -> int:
        return self._in_layer_index

    @property
    def INDEX(self) -> int:
        if self._index is None:
            self._index = self._layer_obj.NODE_INDEX_OFFSET + self.IN_LAYER_INDEX
        return self._index

    @property
    def layer_obj(self) -> NodeLayer:
        return self._layer_obj

    # @abstractmethod
    # def get_positions_of_neighbor_nodes(self):
    #     pass

    def __repr__(self):
        return (f"{type(self).__name__}"
                f"(layer_index={self.LAYER_INDEX}, "
                f"in_layer_index={self.IN_LAYER_INDEX}, "
                f"partition_obj={self._partition_obj})")
