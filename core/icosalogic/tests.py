from pyglobe3d.core.icosalogic.mesh import Mesh
from pyglobe3d.core.icosalogic.node import Node
from pyglobe3d.core.icosalogic.node_attrs import NodeIndex, NodeLocation
from pyglobe3d.core.icosalogic.mesh4_test_data import mesh4_adjacent_triangles, mesh4_neighboring_nodes


def test_edges():
    pass


def test_nodes():
    print("Running a node test:")
    mesh = Mesh(partition=4)

    print("index-layer&position-index transformation...")
    for index in range(0, mesh.GRID.LAST_NODE_INDEX):
        nd1 = mesh.create_node(index=index)
        nd2 = Node(
            location_object=NodeLocation(
                grid=mesh.GRID,
                layer=nd1.layer,
                position_in_layer=nd1.position_in_layer
            )
        )
        nd3 = Node(
            index_object=NodeIndex(
                grid=mesh.GRID,
                index=nd2.index
            )
        )

        assert nd1.index == nd2.index == nd3.index
        assert nd1.layer == nd2.layer == nd3.layer
        assert nd1.position_in_layer == nd2.position_in_layer == nd3.position_in_layer
        assert nd1 == nd2 == nd3
    print("...is OK")

    print("node comparison...")
    for index1 in range(0, mesh.GRID.LAST_NODE_INDEX):
        for index2 in range(0, mesh.GRID.LAST_NODE_INDEX):
            nd1 = mesh.create_node(index=index1)
            nd2 = mesh.create_node(index=index2)
            if index1 < index2:
                assert nd1 < nd2
            if index1 <= index2:
                assert nd1 <= nd2
            if index1 > index2:
                assert nd1 > nd2
            if index1 >= index2:
                assert nd1 >= nd2
            if index1 != index2:
                assert nd1 != nd2
    print("...is OK")

    for index in mesh4_neighboring_nodes:
        nd = mesh.create_node(index=index)
        nn_indices1 = mesh4_neighboring_nodes[index]
        nn_indices2 = tuple(x.index for x in nd.neighboring_nodes)
        # print(index)
        # print(nn_indices1)
        # print(nn_indices2)
        assert nn_indices1 == nn_indices2

    for index in mesh4_adjacent_triangles:
        nd = mesh.create_node(index=index)
        at_indices1 = mesh4_adjacent_triangles[index]
        at_indices2 = tuple(x.index for x in nd.adjacent_triangles)
        # print(index)
        # print(at_indices1)
        # print(at_indices2)
        assert at_indices1 == at_indices2


def test_triangles():
    pass


test_nodes()
