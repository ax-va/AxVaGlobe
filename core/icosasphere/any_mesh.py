from pyglobe3d.core.icosalogic import Mesh as LogicMesh
from pyglobe3d.core.icosasphere.icosahedron import Icosahedron


class AnyMesh:
    def __init__(self, partition: int = 1, radius: float = 1.0):
        self._logic_mesh = LogicMesh(partition=partition)
        self._icosahedron = Icosahedron(radius=radius)
        self._index_offset = self._logic_mesh.GRID.NUMBER_OF_NODES
        self._theta_factor = self.icosahedron.theta / self._logic_mesh.partition
        
    @property
    def logic_mesh(self):
        return self._logic_mesh

    @property
    def icosahedron(self):
        return self._icosahedron
    
    @property
    def radius(self):
        return self._icosahedron.radius
    
    @property
    def partition(self):
        return self._logic_mesh.partition
