from abc import ABC, abstractmethod


class BaseNodeLayer(ABC):
    def __init__(
            self,
            index: int,
    ):
        self._index = index  # layer index

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