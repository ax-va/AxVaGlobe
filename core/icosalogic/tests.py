from pyglobe3d.core.icosalogic.mesh import Mesh
from pyglobe3d.core.icosalogic.node import Node
from pyglobe3d.core.icosalogic.node_attrs import NodeIndex, NodeLocation

mesh4_neighboring_nodes = {
    0: (1, 2, 3, 4, 5),
    1: (0, 2, 7, 6, 15, 5),
    2: (0, 3, 9, 8, 7, 1),
    5: (0, 1, 15, 14, 13, 4),
    7: (1, 2, 8, 18, 17, 6),
    8: (2, 9, 20, 19, 18, 7),
    11: (3, 4, 12, 24, 23, 10),
    12: (4, 13, 26, 25, 24, 11),
    13: (4, 5, 14, 27, 26, 12),
    15: (5, 1, 6, 30, 29, 14),
    16: (6, 17, 32, 31, 50, 30),
    17: (6, 7, 18, 33, 32, 16),
    19: (8, 20, 36, 35, 34, 18),
    20: (8, 9, 21, 37, 36, 19),
    25: (12, 26, 44, 43, 42, 24),
    27: (13, 14, 28, 46, 45, 26),
    29: (14, 15, 30, 49, 48, 28),
    31: (16, 32, 52, 51, 50),
    32: (16, 17, 33, 53, 52, 31),
    34: (18, 19, 35, 55, 54, 33),
    38: (21, 22, 39, 59, 58, 37),
    39: (22, 40, 60, 59, 38),
    40: (22, 23, 41, 61, 60, 39),
    43: (25, 44, 64, 63, 42),
    47: (28, 48, 68, 67, 46),
    50: (30, 16, 31, 51, 70, 49),
    51: (50, 31, 52, 72, 71, 70),
    52: (31, 32, 53, 73, 72, 51),
    55: (34, 35, 56, 76, 75, 54),
    59: (38, 39, 60, 80, 79, 58),
    60: (39, 40, 61, 81, 80, 59),
    65: (44, 45, 66, 86, 85, 64),
    70: (49, 50, 51, 71, 90, 69),
    71: (70, 51, 72, 92, 91, 90),
    75: (54, 55, 76, 96, 95, 74),
    80: (59, 60, 81, 101, 100, 79),
    82: (61, 62, 83, 103, 102, 81),
    90: (69, 70, 71, 91, 110, 89),
    91: (90, 71, 92, 112, 111, 110),
    95: (74, 75, 96, 116, 115, 94),
    100: (79, 80, 101, 121, 120, 99),
    107: (86, 87, 108, 128, 127, 106),
    111: (110, 91, 112, 131, 130),
    115: (94, 95, 116, 134, 114),
    119: (98, 99, 120, 137, 118),
    121: (100, 101, 122, 139, 138, 120),
    127: (106, 107, 128, 143, 126),
    128: (107, 108, 129, 144, 143, 127),
    130: (109, 110, 111, 131, 145, 129),
    131: (111, 112, 132, 146, 145, 130),
    132: (112, 113, 133, 147, 146, 131),
    134: (115, 116, 135, 148, 133, 114),
    140: (123, 124, 141, 152, 139, 122),
    142: (125, 126, 143, 154, 153, 141),
    143: (127, 128, 144, 154, 142, 126),
    145: (129, 130, 131, 146, 155, 144),
    147: (132, 133, 148, 157, 156, 146),
    146: (131, 132, 147, 156, 155, 145),
    150: (137, 138, 151, 158, 149, 136),
    151: (138, 139, 152, 159, 158, 150),
    154: (143, 144, 155, 160, 153, 142),
    155: (144, 145, 146, 156, 160, 154),
    158: (150, 151, 159, 161, 157, 149),
    159: (152, 153, 160, 161, 158, 151),
    160: (154, 155, 156, 161, 159, 153),
    161: (156, 157, 158, 159, 160)
}


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
        assert nn_indices1 == nn_indices2


def test_triangles():
    pass


if __name__ == '__main__':
    test_nodes()