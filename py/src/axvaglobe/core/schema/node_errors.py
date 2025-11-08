from axvaglobe.core.schema.errors import SchemaError


class NodeError(SchemaError):
    pass


class NodeIndexError(NodeError):
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
