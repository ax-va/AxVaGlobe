from abc import ABC, abstractmethod

from axvaglobe.core.schema.partition import Partition


class _BaseNodeLayer(ABC):
    """
    The class is private because the constructor parameters are not validated.
    """

    def __init__(
        self,
        index: int,
        partition_obj: Partition,
    ):
        self._partition_obj: Partition = partition_obj
        self._index: int = index  # node layer index
        # lazy
        self._node_index_offset: int | None = None
        self._number_of_nodes: int | None = None
        self._last_in_layer_index: int | None = None

    @property
    def INDEX(self) -> int:
        return self._index

    @property
    @abstractmethod
    def NODE_INDEX_OFFSET(self) -> int:
        pass

    @property
    @abstractmethod
    def NUMBER_OF_NODES(self) -> int:
        pass

    @property
    def LAST_IN_LAYER_INDEX(self) -> int:
        if self._last_in_layer_index is None:
            self._last_in_layer_index = self.NUMBER_OF_NODES - 1
        return self._last_in_layer_index

    def __repr__(self):
        return f"{type(self).__name__}(index={self.INDEX}, partition_obj={self._partition_obj})"
