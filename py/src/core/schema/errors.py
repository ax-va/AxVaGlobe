class SchemaError(Exception):
    pass


class PartitionValueError(SchemaError):
    def __init__(self, partition: int):
        self.message = f"The partition value is not a positive integer greater than one: {partition}."
        SchemaError.__init__(self, self.message)


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


class NodeIndexError(SchemaError):
    def __init__(
        self,
        node_index: int,
        start_index: int,
        end_index: int,
        partition: int,
    ):
        self.message = (
            f"The node index is out the range [{start_index}, {end_index}] "
            f"for partition '{partition}': {node_index}."
        )
        SchemaError.__init__(self, self.message)
