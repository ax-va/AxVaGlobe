from pyglobe3d.core.icosalogic.logical_errors import UncomparableElementsError


class ElementWithIndexObject:
    def __eq__(self, other):
        return other is not None \
               and self.__class__ == other.__class__ \
               and self.grid.PARTITION == other.grid.PARTITION \
               and self.index == other.index

    def __ge__(self, other):
        if other is None \
                or self.__class__ != other.__class__ \
                or self.grid.PARTITION != other.grid.PARTITION:
            raise UncomparableElementsError()
        return self.index >= other.index

    def __gt__(self, other):
        if other is None \
                or self.__class__ != other.__class__ \
                or self.grid.PARTITION != other.grid.PARTITION:
            raise UncomparableElementsError()
        return self.index > other.index

    def __le__(self, other):
        if other is None \
                or self.__class__ != other.__class__ \
                or self.grid.PARTITION != other.grid.PARTITION:
            raise UncomparableElementsError()
        return self.index <= other.index

    def __lt__(self, other):
        if other is None \
                or self.__class__ != other.__class__ \
                or self.grid.PARTITION != other.grid.PARTITION:
            raise UncomparableElementsError()
        return self.index < other.index

    def __ne__(self, other):
        return other is None \
               or self.__class__ != other.__class__ \
               or self.grid.PARTITION != other.grid.PARTITION \
               or self.index != other.index

    def __repr__(self):
        return f'{self.__class__.__name__}(index_object={self._index_object})'

    @property
    def grid(self):
        return self._index_object.GRID

    @property
    def index(self):
        return self._index_object.INDEX


class ElementWithLocationObject:
    @property
    def grid(self):
        return self._location_object.GRID

    @property
    def layer(self):
        return self._location_object.LAYER

    @property
    def position_in_layer(self):
        return self._location_object.POSITION_IN_LAYER


class ElementWithIndexAndLocationObjects(ElementWithIndexObject, ElementWithLocationObject):
    def _set_attributes(self, index_object, location_object):
        if location_object:
            self._location_object = location_object
            self._index_object = self._location_object.index_object
        elif index_object:
            self._index_object = index_object
            self._location_object = self._index_object.location_object
        else:
            self._index_object = self.__init__.__annotations__['index_object']()
            self._location_object = self.__init__.__annotations__['location_object']()

