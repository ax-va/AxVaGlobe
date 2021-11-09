"""
Write 'py.test tests.py' in the terminal to test by using the 'pytest' package.
For this, change the path in Windows by 'cd pyglobe3d\core\icosalogic\'.
"""
from pyglobe3d.core.icosalogic.mesh import Mesh
from pyglobe3d.core.icosalogic.node import Node
from pyglobe3d.core.icosalogic.node_attrs import NodeIndex, NodeLocation

import pyglobe3d.core.icosalogic.mesh4_test_data as mesh4_data
from pyglobe3d.core.icosalogic.triangle import Triangle
from pyglobe3d.core.icosalogic.triangle_attrs import TriangleLocation, TriangleIndex


def test_grid():
    pass


def test_edges(mesh, icosahedron_nodes_indices, edge_nodes_indices):
    print('Running the edge test:')
    print('*** icosahedron nodes of edges...')
    for index in icosahedron_nodes_indices:
        ed = mesh.EDGES[index]
        ic_ns_indices1 = icosahedron_nodes_indices[index]
        ic_ns_indices2 = tuple(x.index for x in ed.icosahedron_nodes)
        assert ic_ns_indices1 == ic_ns_indices2, 'Calculated icosahedron nodes do not match test icosahedron nodes'
    print('...are OK')

    print('*** edge nodes...')
    for index in edge_nodes_indices:
        ed = mesh.EDGES[index]
        ed_ns_indices1 = edge_nodes_indices[index]
        ed_ns_indices2 = tuple(x.index for x in ed.edge_nodes_generator())
        assert ed_ns_indices1 == ed_ns_indices2, 'Calculated edge nodes do not match test edge nodes'
    print('...are OK')


def test_nodes(mesh, adjacent_triangles_indices, neighboring_nodes_indices):
    print('Running the node test:')
    print("*** transformation 'index -> layer and position -> index'...")
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
        assert nd1 == nd2 == nd3, 'Node objects do not match'
    print('...is OK')

    print('*** node comparison...')
    for index1 in range(0, mesh.GRID.LAST_NODE_INDEX):
        for index2 in range(0, mesh.GRID.LAST_NODE_INDEX):
            nd1 = mesh.create_node(index=index1)
            nd2 = mesh.create_node(index=index2)
            if index1 < index2:
                assert nd1 < nd2, 'node1 < node2 does not hold'
            if index1 <= index2:
                assert nd1 <= nd2, 'node1 <= node2 does not hold'
            if index1 > index2:
                assert nd1 > nd2, 'node1 > node2 does not hold'
            if index1 >= index2:
                assert nd1 >= nd2, 'node1 >= node2 does not hold'
            if index1 != index2:
                assert nd1 != nd2, 'node1 != node2 does not hold'
    print("...is OK")

    print('*** adjacent triangles...')
    for index in adjacent_triangles_indices:
        nd = mesh.create_node(index=index)
        ad_tr_indices1 = adjacent_triangles_indices[index]
        ad_tr_indices2 = tuple(x.index for x in nd.adjacent_triangles)
        # print(index)
        # print(ad_tr_indices1)
        # print(ad_tr_indices2)
        assert ad_tr_indices1 == ad_tr_indices2, 'Calculated adjacent triangles do not match test adjacent triangles'
    print("...are OK")

    print('*** neighboring nodes...')
    for index in neighboring_nodes_indices:
        nd = mesh.create_node(index=index)
        ne_ns_indices1 = neighboring_nodes_indices[index]
        ne_ns_indices2 = tuple(x.index for x in nd.neighboring_nodes)
        # print(index)
        # print(ne_ns_indices1)
        # print(ne_ns_indices2)
        assert ne_ns_indices1 == ne_ns_indices2, 'Calculated neighboring nodes do not match test neighboring nodes'
    print('...are OK')


def test_triangles(mesh, triangle_nodes_indices):
    print('Running the triangle test:')

    print("*** transformation 'index -> layer and position -> index'...")
    for index in range(0, mesh.GRID.LAST_TRIANGLE_INDEX):
        tr1 = mesh.create_triangle(index=index)
        tr2 = Triangle(
            location_object=TriangleLocation(
                grid=mesh.GRID,
                layer=tr1.layer,
                position_in_layer=tr1.position_in_layer
            )
        )
        tr3 = Triangle(
            index_object=TriangleIndex(
                grid=mesh.GRID,
                index=tr2.index
            )
        )

        assert tr1.index == tr2.index == tr3.index, 'Triangle indices do not match'
        assert tr1.layer == tr2.layer == tr3.layer, 'Triangle layers do not match'
        assert tr1.position_in_layer == tr2.position_in_layer == tr3.position_in_layer, \
            'Triangle positions in layer do not match'
        assert tr1 == tr2 == tr3, 'Triangle objects do not match'
    print('...is OK')

    print('*** triangle comparison...')
    for index1 in range(0, mesh.GRID.LAST_TRIANGLE_INDEX):
        for index2 in range(0, mesh.GRID.LAST_TRIANGLE_INDEX):
            tr1 = mesh.create_triangle(index=index1)
            tr2 = mesh.create_triangle(index=index2)
            if index1 < index2:
                assert tr1 < tr2, 'triangle1 < triangle2 does not hold'
            if index1 <= index2:
                assert tr1 <= tr2, 'triangle1 <= triangle2 does not hold'
            if index1 > index2:
                assert tr1 > tr2, 'triangle1 > triangle2 does not hold'
            if index1 >= index2:
                assert tr1 >= tr2, 'triangle1 >= triangle2 does not hold'
            if index1 != index2:
                assert tr1 != tr2, 'triangle1 != triangle2 does not hold'
    print('...is OK')

    print('*** triangle nodes...')
    for index in triangle_nodes_indices:
        tr = mesh.create_triangle(index=index)
        tr_ns_indices1 = triangle_nodes_indices[index]
        tr_ns_indices2 = tuple(x.index for x in tr.triangle_nodes)
        assert tr_ns_indices1 == tr_ns_indices2, 'Calculated triangle nodes do not match test triangle nodes'
    print('...are OK')


mesh4 = Mesh(partition=4)
test_edges(mesh4, mesh4_data.icosahedron_nodes_indices, mesh4_data.edge_nodes_indices)
print('-'*20)
test_nodes(mesh4, mesh4_data.adjacent_triangles_indices, mesh4_data.neighboring_nodes_indices)
print('-'*20)
test_triangles(mesh4, mesh4_data.triangle_nodes_indices)
