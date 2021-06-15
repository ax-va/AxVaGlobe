import functools

from collections import namedtuple
from typing import Generator

from pyglobe3d.core.icosalogic.grid_consts import Grid
from pyglobe3d.core.icosalogic.element_errs import EdgeIndexValueError
from pyglobe3d.core.icosalogic.node import Node
from pyglobe3d.core.icosalogic.node_attrs import NodeLocation


def _check_edge_index(setter):
    """
    The decorator function checks the edge index before setting it.
    Checking is required only for debugging and can be disabled in the release.

    """
    @functools.wraps(setter)
    def checker(edge_object, index):
        if not 0 <= index < 30:
            raise EdgeIndexValueError(index=index)
        setter(edge_object, index)
    return checker


class Edge:
    def __init__(self, grid=Grid(), index=0):
        self._grid = grid
        self._set_index(index)
        self._edge_nodes_generators = (
            self._edge0_nodes_generator,
            self._edge1_nodes_generator,
            self._edge2_nodes_generator,
            self._edge3_nodes_generator,
            self._edge4_nodes_generator,
            self._edge5_nodes_generator,
            self._edge6_nodes_generator,
            self._edge7_nodes_generator,
            self._edge8_nodes_generator,
            self._edge9_nodes_generator,
            self._edge10_nodes_generator,
            self._edge11_nodes_generator,
            self._edge12_nodes_generator,
            self._edge13_nodes_generator,
            self._edge14_nodes_generator,
            self._edge15_nodes_generator,
            self._edge16_nodes_generator,
            self._edge17_nodes_generator,
            self._edge18_nodes_generator,
            self._edge19_nodes_generator,
            self._edge20_nodes_generator,
            self._edge21_nodes_generator,
            self._edge22_nodes_generator,
            self._edge23_nodes_generator,
            self._edge24_nodes_generator,
            self._edge25_nodes_generator,
            self._edge26_nodes_generator,
            self._edge27_nodes_generator,
            self._edge28_nodes_generator,
            self._edge29_nodes_generator
        )
        self._icosahedron_node_layers = [None, None]
        self._icosahedron_node_positions_in_layers = [None, None]
        self._icosahedron_nodes = None

    def __repr__(self):
        return f'{self.__class__.__name__}(grid={self._grid}, index={self._index})'

    @property
    def icosahedron_nodes(self) -> namedtuple:
        if not self._icosahedron_nodes:
            self._set_icosahedron_nodes()
        return self._icosahedron_nodes

    @property
    def index(self) -> int:
        return self._index

    def edge_nodes_generator(self) -> Generator[Node, None, None]:
        yield from self._edge_nodes_generators[self._index]()

    def _edge0_nodes_generator(self):
        return (
            Node(
                location_object=NodeLocation(
                    grid=self._grid,
                    layer=i,
                    position_in_layer=0,
                )
            ) for i in range(0, self._grid.NUMBER_OF_NODES_IN_EDGE)
        )

    def _edge1_nodes_generator(self):
        return (
            Node(
                location_object=NodeLocation(
                    grid=self._grid,
                    layer=i,
                    position_in_layer=i   
                )
            ) for i in range(0, self._grid.NUMBER_OF_NODES_IN_EDGE)
        )

    def _edge2_nodes_generator(self):
        return (
            Node(
                location_object=NodeLocation(
                    grid=self._grid,
                    layer=i,
                    position_in_layer=2 * i
                )
            ) for i in range(0, self._grid.NUMBER_OF_NODES_IN_EDGE)
        )

    def _edge3_nodes_generator(self):
        return (
            Node(
                location_object=NodeLocation(
                    grid=self._grid,
                    layer=i,
                    position_in_layer=3 * i
                )
            ) for i in range(0, self._grid.NUMBER_OF_NODES_IN_EDGE)
        )

    def _edge4_nodes_generator(self):
        return (
            Node(
                location_object=NodeLocation(
                    grid=self._grid,
                    layer=i,
                    position_in_layer=4 * i
                )
            ) for i in range(0, self._grid.NUMBER_OF_NODES_IN_EDGE)
        )

    def _edge5_nodes_generator(self):
        return (
            Node(
                location_object=NodeLocation(
                    grid=self._grid,
                    layer=self._grid.FIRST_NODE_LAYER_IN_PART2,
                    position_in_layer=i
                )
            ) for i in range(0, self._grid.NUMBER_OF_NODES_IN_EDGE)
        )

    def _edge6_nodes_generator(self):
        return (
            Node(
                location_object=NodeLocation(
                    grid=self._grid,
                    layer=self._grid.FIRST_NODE_LAYER_IN_PART2,
                    position_in_layer=i + self._grid.PARTITION
                )
            ) for i in range(0, self._grid.NUMBER_OF_NODES_IN_EDGE)
        )

    def _edge7_nodes_generator(self):
        return (
            Node(
                location_object=NodeLocation(
                    grid=self._grid,
                    layer=self._grid.FIRST_NODE_LAYER_IN_PART2,
                    position_in_layer=i + self._grid.PARTITION_X2
                )
            ) for i in range(0, self._grid.NUMBER_OF_NODES_IN_EDGE)
        )

    def _edge8_nodes_generator(self):
        return (
            Node(
                location_object=NodeLocation(
                    grid=self._grid,
                    layer=self._grid.FIRST_NODE_LAYER_IN_PART2,
                    position_in_layer=i + self._grid.PARTITION_X3
                )
            ) for i in range(0, self._grid.NUMBER_OF_NODES_IN_EDGE)
        )

    def _edge9_nodes_generator(self):
        for i in range(0, self._grid.NUMBER_OF_NODES_IN_EDGE):
            if i < self._grid.NUMBER_OF_NODES_IN_EDGE - 1:
                yield Node(
                    location_object=NodeLocation(
                        grid=self._grid,
                        layer=self._grid.FIRST_NODE_LAYER_IN_PART2,
                        position_in_layer=i + self._grid.PARTITION_X4
                    )
                )
            else:
                yield Node(
                    location_object=NodeLocation(
                        grid=self._grid,
                        layer=self._grid.FIRST_NODE_LAYER_IN_PART2,
                        position_in_layer=0
                    )
                )

    def _edge10_nodes_generator(self):
        return (
            Node(
                location_object=NodeLocation(
                    grid=self._grid,
                    layer=self._grid.FIRST_NODE_LAYER_IN_PART2,
                    position_in_layer=0
                )
            ) for i in range(0, self._grid.NUMBER_OF_NODES_IN_EDGE)
        )

    def _edge11_nodes_generator(self):
        return (
            Node(
                location_object=NodeLocation(
                    grid=self._grid,
                    layer=i + self._grid.FIRST_NODE_LAYER_IN_PART2,
                    position_in_layer=i
                )
            ) for i in range(0, self._grid.NUMBER_OF_NODES_IN_EDGE)
        )

    def _edge12_nodes_generator(self):
        return (
            Node(
                location_object=NodeLocation(
                    grid=self._grid,
                    layer=i + self._grid.FIRST_NODE_LAYER_IN_PART2,
                    position_in_layer=self._grid.PARTITION
                )
            ) for i in range(0, self._grid.NUMBER_OF_NODES_IN_EDGE)
        )

    def _edge13_nodes_generator(self):
        return (
            Node(
                location_object=NodeLocation(
                    grid=self._grid,
                    layer=i + self._grid.FIRST_NODE_LAYER_IN_PART2,
                    position_in_layer=i + self._grid.PARTITION
                )
            ) for i in range(0, self._grid.NUMBER_OF_NODES_IN_EDGE)
        )

    def _edge14_nodes_generator(self):
        return (
            Node(
                location_object=NodeLocation(
                    grid=self._grid,
                    layer=i + self._grid.FIRST_NODE_LAYER_IN_PART2,
                    position_in_layer=self._grid.PARTITION_X2
                )
            ) for i in range(0, self._grid.NUMBER_OF_NODES_IN_EDGE)
        )

    def _edge15_nodes_generator(self):
        return (
            Node(
                location_object=NodeLocation(
                    grid=self._grid,
                    layer=i + self._grid.FIRST_NODE_LAYER_IN_PART2,
                    position_in_layer=i + self._grid.PARTITION_X2
                )
            ) for i in range(0, self._grid.NUMBER_OF_NODES_IN_EDGE)
        )

    def _edge16_nodes_generator(self):
        return (
            Node(
                location_object=NodeLocation(
                    grid=self._grid,
                    layer=i + self._grid.FIRST_NODE_LAYER_IN_PART2,
                    position_in_layer=self._grid.PARTITION_X3
                )
            ) for i in range(0, self._grid.NUMBER_OF_NODES_IN_EDGE)
        )

    def _edge17_nodes_generator(self):
        return (
            Node(
                location_object=NodeLocation(
                    grid=self._grid,
                    layer=i + self._grid.FIRST_NODE_LAYER_IN_PART2,
                    position_in_layer=i + self._grid.PARTITION_X3
                )
            ) for i in range(0, self._grid.NUMBER_OF_NODES_IN_EDGE)
        )

    def _edge18_nodes_generator(self):
        return (
            Node(
                location_object=NodeLocation(
                    grid=self._grid,
                    layer=i + self._grid.FIRST_NODE_LAYER_IN_PART2,
                    position_in_layer=self._grid.PARTITION_X4
                )
            ) for i in range(0, self._grid.NUMBER_OF_NODES_IN_EDGE)
        )

    def _edge19_nodes_generator(self):
        for i in range(0, self._grid.NUMBER_OF_NODES_IN_EDGE):
            if i < self._grid.NUMBER_OF_NODES_IN_EDGE - 1:
                yield Node(
                    location_object=NodeLocation(
                        grid=self._grid,
                        layer=i + self._grid.FIRST_NODE_LAYER_IN_PART2,
                        position_in_layer=i + self._grid.PARTITION_X4
                    )
                )
            else:
                yield Node(
                    location_object=NodeLocation(
                        grid=self._grid,
                        layer=self._grid.LAST_NODE_LAYER_IN_PART2,
                        position_in_layer=0
                    )
                )

    def _edge20_nodes_generator(self):
        return (
            Node(
                location_object=NodeLocation(
                    grid=self._grid,
                    layer=self._grid.LAST_NODE_LAYER_IN_PART2,
                    position_in_layer=i
                )
            ) for i in range(0, self._grid.NUMBER_OF_NODES_IN_EDGE)
        )

    def _edge21_nodes_generator(self):
        return (
            Node(
                location_object=NodeLocation(
                    grid=self._grid,
                    layer=self._grid.LAST_NODE_LAYER_IN_PART2,
                    position_in_layer=i + self._grid.PARTITION
                )
            ) for i in range(0, self._grid.NUMBER_OF_NODES_IN_EDGE)
        )

    def _edge22_nodes_generator(self):
        return (
            Node(
                location_object=NodeLocation(
                    grid=self._grid,
                    layer=self._grid.LAST_NODE_LAYER_IN_PART2,
                    position_in_layer=i + self._grid.PARTITION_X2
                )
            ) for i in range(0, self._grid.NUMBER_OF_NODES_IN_EDGE)
        )

    def _edge23_nodes_generator(self):
        return (
            Node(
                location_object=NodeLocation(
                    grid=self._grid,
                    layer=self._grid.LAST_NODE_LAYER_IN_PART2,
                    position_in_layer=i + self._grid.PARTITION_X3
                )
            ) for i in range(0, self._grid.NUMBER_OF_NODES_IN_EDGE)
        )

    def _edge24_nodes_generator(self):
        for i in range(0, self._grid.NUMBER_OF_NODES_IN_EDGE):
            if i < self._grid.NUMBER_OF_NODES_IN_EDGE - 1:
                yield Node(
                    location_object=NodeLocation(
                        grid=self._grid,
                        layer=self._grid.LAST_NODE_LAYER_IN_PART2,
                        position_in_layer=i + self._grid.PARTITION_X4
                    )
                )
            else:
                yield Node(
                    location_object=NodeLocation(
                        grid=self._grid,
                        layer=self._grid.LAST_NODE_LAYER_IN_PART2,
                        position_in_layer=0
                    )
                )

    def _edge25_nodes_generator(self):
        return (
            Node(
                location_object=NodeLocation(
                    grid=self._grid,
                    layer=i + self._grid.LAST_NODE_LAYER_IN_PART2,
                    position_in_layer=0
                )
            ) for i in range(0, self._grid.NUMBER_OF_NODES_IN_EDGE)
        )

    def _edge26_nodes_generator(self):
        return (
            Node(
                location_object=NodeLocation(
                    grid=self._grid,
                    layer=i + self._grid.LAST_NODE_LAYER_IN_PART2,
                    position_in_layer=self._grid.PARTITION - i
                )
            ) for i in range(0, self._grid.NUMBER_OF_NODES_IN_EDGE)
        )

    def _edge27_nodes_generator(self):
        return (
            Node(
                location_object=NodeLocation(
                    grid=self._grid,
                    layer=i + self._grid.LAST_NODE_LAYER_IN_PART2,
                    position_in_layer=self._grid.PARTITION_X2 - 2 * i
                )
            ) for i in range(0, self._grid.NUMBER_OF_NODES_IN_EDGE)
        )

    def _edge28_nodes_generator(self):
        return (
            Node(
                location_object=NodeLocation(
                    grid=self._grid,
                    layer=i + self._grid.LAST_NODE_LAYER_IN_PART2,
                    position_in_layer=self._grid.PARTITION_X3 - 3 * i
                )
            ) for i in range(0, self._grid.NUMBER_OF_NODES_IN_EDGE)
        )

    def _edge29_nodes_generator(self):
        return (
            Node(
                location_object=NodeLocation(
                    grid=self._grid,
                    layer=i + self._grid.LAST_NODE_LAYER_IN_PART2,
                    position_in_layer=self._grid.PARTITION_X4 - 4 * i
                )
            ) for i in range(0, self._grid.NUMBER_OF_NODES_IN_EDGE)
        )

    def _set_icosahedron_nodes(self):
        if 10 <= self._index <= 19:
            self._icosahedron_node_layers[0] = self._grid.FIRST_NODE_LAYER_IN_PART2
            self._icosahedron_node_layers[1] = self._grid.LAST_NODE_LAYER_IN_PART2
            if self._index % 2 == 0:
                node_position_in_layer = ((self._index - 10) // 2) * self._grid.PARTITION
                self._icosahedron_node_positions_in_layers[0] = node_position_in_layer
                self._icosahedron_node_positions_in_layers[1] = node_position_in_layer
            else:
                self._icosahedron_node_positions_in_layers[0] = ((self._index - 11) // 2) * self._grid.PARTITION
                self._icosahedron_node_positions_in_layers[1] = \
                    self._icosahedron_node_positions_in_layers[0] + self._grid.PARTITION
                if self._index == 19:  # Take into account cyclicality
                    self._icosahedron_node_positions_in_layers[1] = 0
        elif 5 <= self._index <= 9:
            self._icosahedron_node_layers[0] = self._grid.FIRST_NODE_LAYER_IN_PART2
            self._icosahedron_node_positions_in_layers[0] = (self._index - 5) * self._grid.PARTITION
            self._icosahedron_node_layers[1] = self._grid.FIRST_NODE_LAYER_IN_PART2
            self._icosahedron_node_positions_in_layers[1] = \
                self._icosahedron_node_positions_in_layers[0] + self._grid.PARTITION
            if self._index == 9:
                self._icosahedron_node_positions_in_layers[1] = 0
        elif 20 <= self._index <= 24:
            self._icosahedron_node_layers[0] = self._grid.LAST_NODE_LAYER_IN_PART2
            self._icosahedron_node_positions_in_layers[0] = (self._index - 20) * self._grid.PARTITION
            self._icosahedron_node_layers[1] = self._grid.LAST_NODE_LAYER_IN_PART2
            self._icosahedron_node_positions_in_layers[1] = \
                self._icosahedron_node_positions_in_layers[0] + self._grid.PARTITION
            if self._index == 24:
                self._icosahedron_node_positions_in_layers[1] = 0
        elif 0 <= self._index <= 4:
            self._icosahedron_node_layers[0] = 0
            self._icosahedron_node_positions_in_layers[0] = 0
            self._icosahedron_node_layers[1] = self._grid.FIRST_NODE_LAYER_IN_PART2
            self._icosahedron_node_positions_in_layers[1] = self._index * self._grid.PARTITION
        else:  # 25 <= self._index <= 29
            self._icosahedron_node_layers[0] = self._grid.LAST_NODE_LAYER_IN_PART2
            self._icosahedron_node_positions_in_layers[0] = (self._index - 25) * self._grid.PARTITION
            self._icosahedron_node_layers[1] = self._grid.LAST_NODE_LAYER
            self._icosahedron_node_positions_in_layers[1] = 0

        Result = namedtuple('Nodes', ['node0', 'node1'])
        self._icosahedron_nodes = Result._make(
            (
                Node(
                    location_object=NodeLocation(
                        grid=self._grid,
                        layer=self._icosahedron_node_layers[i],
                        position_in_layer=self._icosahedron_node_positions_in_layers[i]
                    )
                ) for i in range(0, 2)
            )
        )

    @_check_edge_index
    def _set_index(self, index):
        self._index = index


if __name__ == '__main__':
    edge4 = Edge(
        grid=Grid(partition=4),
        index=4
    )

    edge24 = Edge(
        grid=Grid(partition=4),
        index=24
    )

    for nd in edge4.icosahedron_nodes:
        print(nd.index)

    print('-' * 10)

    for nd in edge4.edge_nodes_generator():
        print(nd.index)

    print('-' * 10)

    for nd in edge24.edge_nodes_generator():
        print(nd.index)

    from collections.abc import Generator
    print(isinstance(edge24.edge_nodes_generator(), Generator))
    print(edge24.icosahedron_nodes.node0)

