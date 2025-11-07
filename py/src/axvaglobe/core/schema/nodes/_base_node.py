from abc import ABC, abstractmethod
from typing import Self

from axvaglobe.core.schema.constants import Constants
from axvaglobe.core.schema.node_layers import NodeLayer
from axvaglobe.core.schema.node_layers.node_layer_factory import NodeLayerFactory


class _BaseNode(ABC):
    """
    The class is private because the constructor parameters are not validated.
    """

    def __init__(
        self,
        partition: int,
        layer_index: int,
        in_layer_index: int,
    ):
        self._partition: int = partition
        # cached creation
        self._layer: NodeLayer = NodeLayerFactory.create_node_layer_by_layer_index(
            partition=self._partition,
            layer_index=layer_index,
        )
        self._in_layer_index: int = in_layer_index
        # lazy
        self._index: int | None = None

    @property
    def PARTITION(self) -> int:
        return self._partition

    @property
    def LAYER_INDEX(self) -> int:
        return self._layer.INDEX

    @property
    def IN_LAYER_INDEX(self) -> int:
        return self._in_layer_index

    @property
    def INDEX(self) -> int:
        if self._index is None:
            self._index = self._layer.NODE_INDEX_OFFSET_FOR_LAYER + self.IN_LAYER_INDEX
        return self._index

    @property
    def layer(self) -> NodeLayer:
        return self._layer

    @property
    def constants(self) -> Constants:
        # cached constants
        return Constants.get_constants(partition=self._partition)

    @classmethod
    @abstractmethod
    def create_node_by_index(
        cls,
        index: int,
        constants: Constants,
    ) -> Self:
        pass

    # @abstractmethod
    # def get_layer_and_in_layer_indices_of_neighboring_nodes(self):
    #     pass

    def __repr__(self):
        return f"{type(self).__name__}({self.PARTITION}, {self.LAYER_INDEX}, {self.IN_LAYER_INDEX})"
