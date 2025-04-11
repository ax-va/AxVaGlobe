class PartitionValueError(Exception):
    def __init__(self, value: int):
        self.message = f"The partition value is not a positive integer greater than one: {value}."
        Exception.__init__(self, self.message)
