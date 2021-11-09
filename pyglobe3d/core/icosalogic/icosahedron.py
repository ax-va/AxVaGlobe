from collections import namedtuple

from pyglobe3d.core.icosalogic.grid_consts import Grid
from pyglobe3d.core.icosalogic.node import Node
from pyglobe3d.core.icosalogic.node_attrs import NodeIndex


class Icosahedron:
    def __init__(self, grid: Grid = Grid()):
        self._grid = grid
        self._icosahedron_node_indices = (
            0,
            grid.FIRST_NODE_INDEX_IN_PART2,
            grid.FIRST_NODE_INDEX_IN_PART2 + grid.PARTITION,
            grid.FIRST_NODE_INDEX_IN_PART2 + grid.PARTITION_X2,
            grid.FIRST_NODE_INDEX_IN_PART2 + grid.PARTITION_X3,
            grid.FIRST_NODE_INDEX_IN_PART2 + grid.PARTITION_X4,
            grid.FIRST_NODE_INDEX_IN_PART3 - grid.PARTITION_X5,
            grid.FIRST_NODE_INDEX_IN_PART3 - grid.PARTITION_X4,
            grid.FIRST_NODE_INDEX_IN_PART3 - grid.PARTITION_X3,
            grid.FIRST_NODE_INDEX_IN_PART3 - grid.PARTITION_X2,
            grid.FIRST_NODE_INDEX_IN_PART3 - grid.PARTITION,
            grid.LAST_NODE_INDEX
        )

    @property
    def icosahedron_nodes(self):
        Result = namedtuple('IcosahedronNodes', [f'icosahedron_node{i}' for i in range(12)])
        return Result._make(
            (
                Node(
                    index_object=NodeIndex(
                        grid=self._grid,
                        index=index
                    )
                ) for index in self._icosahedron_node_indices
            )
        )


if __name__ == '__main__':
    grd = Grid(4)
    ics = Icosahedron(grd)
    for node in ics.icosahedron_nodes:
        print(node)
