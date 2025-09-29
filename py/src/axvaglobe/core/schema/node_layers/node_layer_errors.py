from axvaglobe.core.schema.errors import SchemaError


class NodeLayerIndexError(SchemaError):
    def __init__(
        self,
        node_layer_index: int,
        start_index: int,
        end_index: int,
        partition: int,
    ):
        self.message = (
            f"The node layer index is out the range [{start_index}, {end_index}] "
            f"for partition {partition}: {node_layer_index}."
        )
        SchemaError.__init__(self, self.message)