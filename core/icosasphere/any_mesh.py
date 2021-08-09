from pyglobe3d.core.icosalogic import Mesh as LogicMesh
from pyglobe3d.core.icosasphere.icosahedron import Icosahedron


class AnyMesh:
    def __init__(self, partition: int = 1, radius: float = 1.0):
        self._logic_mesh = LogicMesh(partition=partition)
        self._icosahedron = Icosahedron(radius=radius)
        self._partition = partition
        self._radius = radius

    @property
    def logic_mesh(self):
        return self._logic_mesh

    @property
    def icosahedron(self):
        return self._icosahedron
