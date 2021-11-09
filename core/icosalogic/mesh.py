from pyglobe3d.core.common.const_attrs import ConstantAttributes
from pyglobe3d.core.icosalogic.edge import Edge
from pyglobe3d.core.icosalogic.grid_consts import Grid
from pyglobe3d.core.icosalogic.icosahedron import Icosahedron
from pyglobe3d.core.icosalogic.node import Node
from pyglobe3d.core.icosalogic.triangle import Triangle


class Mesh(ConstantAttributes):
    def __init__(self, partition: int = 1):
        self.GRID = Grid(partition=partition)
        # 30 edges of the icosahedron:
        self.EDGES = tuple(Edge(grid=self.GRID, index=index) for index in range(0, self.GRID.NUMBER_OF_EDGES))
        # 12 icosahedron nodes:
        self.ICOSAHEDRON_NODES = Icosahedron(grid=self.GRID).icosahedron_nodes

    @property
    def partition(self):
        return self.GRID.PARTITION

    def create_node(self, index=0):
        return Node.create_node(grid=self.GRID, index=index)

    def create_triangle(self, index=0):
        return Triangle.create_triangle(grid=self.GRID, index=index)


if __name__ == '__main__':
    ms = Mesh(partition=4)
    nd31 = ms.create_node(index=31)
    print('-'*10)
    for ns in nd31.neighboring_nodes:
        print(ns)
    print('-' * 10)
    for ts in nd31.adjacent_triangles:
        print(ts)
    print('-' * 10)
    tr31 = ms.create_triangle(index=31)
    print('-' * 10)
    for ns in tr31.triangle_nodes:
        print(ns)

    # grd = Grid(-10)
