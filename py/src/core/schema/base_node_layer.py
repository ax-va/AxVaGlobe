from abc import ABC, abstractmethod


class BaseNodeLayer(ABC):
    def __init__(
            self,
            index: int,
            schema,  # type: "Schema"
    ):
        self._index: int = index  # layer index
        self._schema = schema
        self._node_index_offset_for_layer: int | None = None
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

    def __repr__(self):
        return f"{self.__class__.__bases__[0].__name__}({self.INDEX})"
