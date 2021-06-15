import functools

from pyglobe3d.core.common.const_attrs import ConstantAttributes
from pyglobe3d.core.icosalogic.grid_consts import Grid
from pyglobe3d.core.icosalogic.logical_errors import ElementIndexValueError, \
    ElementLayerValueError, ElementPositionInLayerValueError


def _check_index(setter):
    """
    The decorator function checks the node index or triangle index before setting it.
    Checking is required only for debugging and can be disabled in the release.

    """
    @functools.wraps(setter)
    def checker(index_object, index):
        if not index_object.__class__.is_index_correct(index_object.GRID, index):
            raise ElementIndexValueError(
                element_name=index_object.ELEMENT_NAME["element"],
                grid=index_object.GRID,
                index=index
            )
        setter(index_object, index)
    return checker


def _check_layer(setter):
    """
    The decorator function checks the node layer or triangle layer before setting it.
    Checking is required only for debugging and can be disabled in the release.

    """
    @functools.wraps(setter)
    def checker(location_object, layer):
        grid = location_object.GRID
        if not location_object.__class__.is_layer_correct(grid, layer):
            raise ElementLayerValueError(
                element_name=location_object.ELEMENT_NAME["element"],
                grid=grid,
                layer=layer
            )
        setter(location_object, layer)
    return checker


def _check_position_in_layer(setter):
    """
    The decorator function checks the node position in the layer or triangle position
    in the layer before setting it.
    Checking is required only for debugging and can be disabled in the release.

    """
    @functools.wraps(setter)
    def checker(location_object, position_in_layer):
        grid = location_object.GRID
        layer = location_object.LAYER
        position_in_layer_error = ElementPositionInLayerValueError(
            element_name=location_object.ELEMENT_NAME["element"],
            grid=grid,
            layer=layer,
            position_in_layer=position_in_layer
        )
        if location_object.__class__.is_layer_in_part2(grid, layer):
            if not location_object.__class__.is_position_in_layer_in_part2_correct(grid, position_in_layer):
                raise position_in_layer_error
        elif location_object.__class__.is_layer_in_part1(grid, layer):
            if not location_object.__class__.is_position_in_layer_in_part1_correct(layer, position_in_layer):
                raise position_in_layer_error
        else:  # The layer is in the 3rd part
            if not location_object.__class__.is_position_in_layer_in_part3_correct(grid, layer, position_in_layer):
                raise position_in_layer_error
        setter(location_object, position_in_layer)
    return checker


class ElementIndex(ConstantAttributes):
    def __init__(self, grid=Grid(), index=0):
        self.GRID = grid
        self._set_index(index)

    def __repr__(self):
        return f'{self.__class__.__name__}(grid={self.GRID}, index={self.INDEX})'

    @property
    def location_object(self):
        if self.__class__.is_index_in_part2(self.GRID, self.INDEX):
            layer, position_in_layer = self._get_location_in_part2()

        elif self.__class__.is_index_in_part1(self.GRID, self.INDEX):
            layer, position_in_layer = self._get_location_in_part1()

        else:  # The node index is in the 3rd part
            layer, position_in_layer = self._get_location_in_part3()

        return self.CONJUGATE_CLASS['ElementLocation'](
            grid=self.GRID,
            layer=layer,
            position_in_layer=position_in_layer
        )

    @_check_index
    def _set_index(self, index):
        self.INDEX = index


########################################################################################################################
########################################################################################################################


class ElementLocation(ConstantAttributes):
    def __init__(self, grid=Grid(), layer=0, position_in_layer=0):
        self.GRID = grid
        self._set_layer(layer)
        self._set_position_in_layer(position_in_layer)

    def __repr__(self):
        return f'{self.__class__.__name__}(grid={self.GRID}, layer={self.LAYER}, ' \
               f'position_in_layer={self.POSITION_IN_LAYER})'

    @property
    def index(self):
        return self._get_layer_index_increment() + self.POSITION_IN_LAYER

    @property
    def index_object(self):
        return self.CONJUGATE_CLASS['ElementIndex'](
            grid=self.GRID,
            index=self.index
        )

    def _get_layer_index_increment(self):
        if self.__class__.is_layer_in_part2(self.GRID, self.LAYER):
            return self._get_layer_index_increment_in_part2()
        elif self.__class__.is_layer_in_part1(self.GRID, self.LAYER):
            return self._get_layer_index_increment_in_part1()
        else:  # in the part 3
            return self._get_layer_index_increment_in_part3()

    @_check_layer
    def _set_layer(self, layer):
        self.LAYER = layer

    @_check_position_in_layer
    def _set_position_in_layer(self, position_in_layer):
        self.POSITION_IN_LAYER = position_in_layer
