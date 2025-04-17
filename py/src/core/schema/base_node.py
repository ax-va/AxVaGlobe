from abc import ABC, abstractmethod


class BaseNode(ABC):
    def __init__(
            self,
            layer_index: int,
            in_layer_index: int,
            schema,  # type: "Schema"
    ):
        self._in_layer_index: int = in_layer_index
        self._schema = schema  # type: "Schema"
        self._layer = self._schema.get_node_layer_from_registry(layer_index)  # type: "NodeLayerA"

    @property
    def LAYER_INDEX(self) -> int:
        return self._layer.INDEX

    @property
    def IN_LAYER_INDEX(self) -> int:
        return self._in_layer_index

    @property
    def INDEX(self) -> int:
        return self._layer.NODE_INDEX_OFFSET_FOR_LAYER + self.IN_LAYER_INDEX

    @classmethod
    @abstractmethod
    def create_node_by_index(
            cls,
            index: int,
            schema,  # type: "Schema"
    ):
        pass