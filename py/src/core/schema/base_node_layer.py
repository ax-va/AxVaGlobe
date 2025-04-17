from abc import ABC, abstractmethod


class BaseNodeLayer(ABC):
    def __init__(
            self,
            index: int,
    ):
        self._index: int = index  # layer index
        self._node_offset_for_layer: int | None = None
        self._number_of_nodes: int | None = None

    @property
    def INDEX(self) -> int:
        return self._index

    @property
    @abstractmethod
    def NODE_INDEX_OFFSET_FOR_LAYER(self) -> int:
        pass

    @property
    @abstractmethod
    def NUMBER_OF_NODES(self) -> int:
        pass