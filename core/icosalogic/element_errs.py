from pyglobe3d.core.core_errs import CoreError


class ElementError(CoreError):
    pass


class EdgeIndexValueError(ElementError):
    def __init__(self, index):
        self.message = f'The edge index must be in the range from 0 to 30 exclusive ' \
                       f'and the given index of {index} is outside this range'
        super().__init__(self, self.message)


class ElementIndexValueError(ElementError):
    def __init__(self, element_name, grid, index):
        self.message = f'The {element_name} index of {index} does not match the grid {grid!r}'
        super().__init__(self, self.message)


class ElementLayerValueError(ElementError):
    def __init__(self, element_name, grid, layer):
        self.message = f'The {element_name} layer of {layer} does not match the grid {grid!r}'
        super().__init__(self, self.message)


class ElementPositionInLayerValueError(ElementError):
    def __init__(self, element_name, grid, layer, position_in_layer):
        self.message = f'The {element_name} position of {position_in_layer} in the layer of {layer} ' \
                       f'on the grid {grid!r} does not match the layer'
        super().__init__(self, self.message)


class PartitionValueError(ElementError):
    def __init__(self):
        self.message = 'The partition of the icosahedron grid is not a positive integer'
        super().__init__(self, self.message)


class UncomparableElementsError(ElementError):
    def __init__(self):
        self.message = 'The icosahedron elements cannot be compared'
        super().__init__(self, self.message)
