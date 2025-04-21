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
            schema,  # type: "Schema"
    ):
        start_index: int = schema.constants.north_pole.node_layer.INDEX
        end_index: int = schema.constants.south_pole.node_layer.INDEX
        self.message = (
            f"The node layer index is out the range [{start_index}, {end_index}] for `{schema}`: {node_layer_index}."
        )
        SchemaError.__init__(self, self.message)


class NodeIndexError(SchemaError):
    def __init__(
            self,
            node_index: int,
            schema,  # type: "Schema"
    ):
        start_index: int = schema.constants.north_pole.node.INDEX
        end_index: int = schema.constants.south_pole.node.INDEX
        self.message = f"The node index is out the range [{start_index}, {end_index}] for `{schema}`: {node_index}."
        SchemaError.__init__(self, self.message)
