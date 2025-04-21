from abc import ABC, abstractmethod


class BaseNodeLayer(ABC):
    def __init__(
            self,
            index: int,
            schema,  # type: "Schema"
    ):
        self._index: int = index  # layer index
        self._schema = schema
        # lazy
        self._node_index_offset_for_layer: int | None = None
        self._number_of_nodes: int | None = None
        self._end_node_in_layer_index: int | None = None

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

    @property
    def END_NODE_IN_LAYER_INDEX(self) -> int:
        if self._end_node_in_layer_index is None:
            self._end_node_in_layer_index = self.NUMBER_OF_NODES - 1
        return self._end_node_in_layer_index

    def __repr__(self):
        return f"{self.__class__.__bases__[0].__name__}({self.INDEX})"
