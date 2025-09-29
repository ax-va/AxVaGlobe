class SchemaError(Exception):
    pass


class PartitionValueError(SchemaError):
    def __init__(self, partition: int):
        self.message = f"The partition value is not a positive integer greater than one: {partition}."
        SchemaError.__init__(self, self.message)
