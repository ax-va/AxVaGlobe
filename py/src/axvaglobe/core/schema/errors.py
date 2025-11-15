class SchemaError(Exception):
    pass


class PartitionValueError(SchemaError):
    def __init__(self, partition: int):
        self.message = f"The partition value {partition} is not a positive integer greater than one."
        SchemaError.__init__(self, self.message)
