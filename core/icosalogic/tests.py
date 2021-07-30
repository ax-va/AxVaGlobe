"""
Write 'py.test tests.py' in the terminal to test by using the 'pytest' package.
For this, change the path in Windows by 'cd pyglobe3d\core\icosalogic\'.
"""
from pyglobe3d.core.icosalogic.mesh import Mesh
from pyglobe3d.core.icosalogic.node import Node
from pyglobe3d.core.icosalogic.node_attrs import NodeIndex, NodeLocation

import pyglobe3d.core.icosalogic.mesh4_test_data as mesh4_data


def test_edges():
    pass


def test_nodes(mesh, adjacent_triangles_data, neighboring_nodes_data):
    print("Running the node test:")
    print("transformation index -> layer and position -> index...")
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

        assert nd1.index == nd2.index == nd3.index, 'Node indices do not match'
        assert nd1.layer == nd2.layer == nd3.layer, 'Node layers do not match'
        assert nd1.position_in_layer == nd2.position_in_layer == nd3.position_in_layer, \
            'Node positions in layer do not match'
        assert nd1 == nd2 == nd3
    print("...is OK")

    print("node comparison...")
    for index1 in range(0, mesh.GRID.LAST_NODE_INDEX):
        for index2 in range(0, mesh.GRID.LAST_NODE_INDEX):
            nd1 = mesh.create_node(index=index1)
            nd2 = mesh.create_node(index=index2)
            if index1 < index2:
                assert nd1 < nd2, 'node1 < node2 does not hold'
            if index1 <= index2:
                assert nd1 <= nd2, 'node1 <= node2 does not hold'
            if index1 > index2:
                assert nd1 > nd2, 'node1 > nod2 does not hold'
            if index1 >= index2:
                assert nd1 >= nd2, 'node1 >= node2 does not hold'
            if index1 != index2:
                assert nd1 != nd2, 'node1 != node2 does not hold'
    print("...is OK")

    print("adjacent triangles...")
    for index in adjacent_triangles_data:
        nd = mesh.create_node(index=index)
        ad_tr_indices1 = adjacent_triangles_data[index]
        ad_tr_indices2 = tuple(x.index for x in nd.adjacent_triangles)
        # print(index)
        # print(ad_tr_indices1)
        # print(ad_tr_indices2)
        assert ad_tr_indices1 == ad_tr_indices2, 'Calculated adjacent triangles do not match test adjacent triangles'
    print("...are OK")

    print("neighboring nodes...")
    for index in neighboring_nodes_data:
        nd = mesh.create_node(index=index)
        ne_ns_indices1 = neighboring_nodes_data[index]
        ne_ns_indices2 = tuple(x.index for x in nd.neighboring_nodes)
        # print(index)
        # print(ne_ns_indices1)
        # print(ne_ns_indices2)
        assert ne_ns_indices1 == ne_ns_indices2, 'Calculated neighboring nodes do not match test neighboring nodes'
    print("...are OK")


def test_triangles(mesh, triangle_nodes_data):
    print("Running the triangle test:")

    print("triangle nodes...")
    for index in triangle_nodes_data:
        tr = mesh.create_triangle(index=index)
        tr_ns_indices1 = triangle_nodes_data[index]
        tr_ns_indices2 = tuple(x.index for x in tr.triangle_nodes)
        assert tr_ns_indices1 == tr_ns_indices2, 'Calculated triangle nodes do not match test triangle nodes'
    print("...are OK")


mesh4 = Mesh(partition=4)
test_nodes(mesh4, mesh4_data.adjacent_triangles_data, mesh4_data.neighboring_nodes_data)
print('-'*20)
test_triangles(mesh4, mesh4_data.triangle_nodes_data)
