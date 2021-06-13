class LogicalError(Exception):
    pass


class ElementLayerValueError(LogicalError):
    def __init__(self, element, grid, layer):
        self.message = f'The {element} layer of {layer} does not match the grid {grid!r}'
        LogicalError.__init__(self, self.message)


class PartitionValueError(LogicalError):
    def __init__(self):
        self.message = 'The partition of the icosahedron grid is not a positive integer'
        LogicalError.__init__(self, self.message)


class UncomparableElementsError(LogicalError):
    def __init__(self):
        self.message = 'The icosahedron elements cannot be compared'
        LogicalError.__init__(self, self.message)
