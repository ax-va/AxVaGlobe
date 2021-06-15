class LogicalError(Exception):
    pass


class EdgeIndexValueError(LogicalError):
    def __init__(self, index):
        self.message = f'The edge index must be in the range from 0 to 30 exclusive ' \
                       f'and the given index of {index} is outside this range'
        LogicalError.__init__(self, self.message)


class ElementIndexValueError(LogicalError):
    def __init__(self, element_name, grid, index):
        self.message = f'The {element_name} index of {index} does not match the grid {grid!r}'
        LogicalError.__init__(self, self.message)


class ElementLayerValueError(LogicalError):
    def __init__(self, element_name, grid, layer):
        self.message = f'The {element_name} layer of {layer} does not match the grid {grid!r}'
        LogicalError.__init__(self, self.message)


class ElementPositionInLayerValueError(LogicalError):
    def __init__(self, element_name, grid, layer, position_in_layer):
        self.message = f'The {element_name} position of {position_in_layer} in the layer of {layer} ' \
                       f'on the grid {grid!r} does not match the layer'
        LogicalError.__init__(self, self.message)


class PartitionValueError(LogicalError):
    def __init__(self):
        self.message = 'The partition of the icosahedron grid is not a positive integer'
        LogicalError.__init__(self, self.message)


class UncomparableElementsError(LogicalError):
    def __init__(self):
        self.message = 'The icosahedron elements cannot be compared'
        LogicalError.__init__(self, self.message)
