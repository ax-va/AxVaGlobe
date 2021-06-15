from pyglobe3d.core.icosalogic.grid_consts import Grid
from pyglobe3d.core.icosalogic.elements import ElementWithIndexAndLocationObjects
from pyglobe3d.core.icosalogic.triangle_attrs import TriangleIndex, TriangleLocation


class Triangle(ElementWithIndexAndLocationObjects):
    """
    Describes a logical node located on the icosahedron.

    """
    def __init__(self,
                 index_object: TriangleIndex = None,
                 location_object: TriangleLocation = None
                 ):
        ElementWithIndexAndLocationObjects.__init__(self, index_object, location_object)
        self._triangle_nodes = None

    @classmethod
    def create_triangle(cls, grid=Grid(), index=0):
        return cls(
            index_object=TriangleIndex(
                grid=grid,
                index=index
            )
        )

    @property
    def triangle_nodes(self):
        if not self._triangle_nodes:
            from pyglobe3d.core.icosalogic.triangle_nodes import TriangleNodes
            self._triangle_nodes = TriangleNodes(base_triangle=self).triangle_nodes
        return self._triangle_nodes


if __name__ == '__main__':
    from pyglobe3d.core.icosalogic.grid_consts import Grid
    tr45 = Triangle(
        index_object=TriangleIndex(
            grid=Grid(4),
            index=45
        )
    )

    for nd in tr45.triangle_nodes:
        print(nd.index)