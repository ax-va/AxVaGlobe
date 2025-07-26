from abc import ABC, abstractmethod
from typing import Self

from core.schema.constants import Constants
from core.schema.node_layer import NodeLayer
from core.schema.node_layer_registry import NodeLayerRegistry

class BaseNode(ABC):
    def __init__(
        self,
        layer_index: int,
        in_layer_index: int,
        constants: Constants,
    ):
        self._constants: Constants = constants
        self._layer: NodeLayer = NodeLayerRegistry.get_node_layer(layer_index, constants)
        self._in_layer_index: int = in_layer_index
        # lazy
        self._index: int | None = None

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
        return f"{type(self).__name__}({self.LAYER_INDEX}, {self.IN_LAYER_INDEX}, {self._constants})"
