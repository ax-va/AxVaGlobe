import pytest

from core.schema.node_b import NodeB


@pytest.mark.parametrize(
    "index,"
    "layer_index,"
    "in_layer_index",
    [
        (16, 3, 0),
        (17, 3, 1),
        (18, 3, 2),
        (19, 3, 3),
        (20, 3, 4),
        (21, 3, 5),
        (22, 3, 6),
        (23, 3, 7),
        (24, 3, 8),
        (25, 3, 9),
    ]
)
def test_creation_of_node_b_for_schema_two(
        index,
        layer_index,
        in_layer_index,
        schema_two,  # function fixture
):
    node_b = NodeB(layer_index, in_layer_index, schema_two.constants)
    assert node_b.INDEX == index
    assert node_b.LAYER_INDEX == layer_index
    assert node_b.IN_LAYER_INDEX == in_layer_index

    node_b = NodeB.create_node_by_index(index, schema_two.constants)
    assert node_b.INDEX == index
    assert node_b.LAYER_INDEX == layer_index
    assert node_b.IN_LAYER_INDEX == in_layer_index


@pytest.mark.parametrize(
    "index,"
    "layer_index,"
    "in_layer_index",
    [
        (31, 4, 0),
        (32, 4, 1),
        (33, 4, 2),
        (34, 4, 3),
        (35, 4, 4),
        (36, 4, 5),
        (37, 4, 6),
        (38, 4, 7),
        (39, 4, 8),
        (40, 4, 9),
        (41, 4, 10),
        (42, 4, 11),
        (43, 4, 12),
        (44, 4, 13),
        (45, 4, 14),
        (46, 5, 0),
        (47, 5, 1),
        (48, 5, 2),
        (49, 5, 3),
        (50, 5, 4),
        (51, 5, 5),
        (52, 5, 6),
        (53, 5, 7),
        (54, 5, 8),
        (55, 5, 9),
        (56, 5, 10),
        (57, 5, 11),
        (58, 5, 12),
        (59, 5, 13),
        (60, 5, 14),
    ]
)
def test_creation_of_node_b_for_schema_three(
        index,
        layer_index,
        in_layer_index,
        schema_three,  # function fixture
):
    node_b = NodeB(layer_index, in_layer_index, schema_three.constants)
    assert node_b.INDEX == index
    assert node_b.LAYER_INDEX == layer_index
    assert node_b.IN_LAYER_INDEX == in_layer_index

    node_b = NodeB.create_node_by_index(index, schema_three.constants)
    assert node_b.INDEX == index
    assert node_b.LAYER_INDEX == layer_index
    assert node_b.IN_LAYER_INDEX == in_layer_index


@pytest.mark.parametrize(
    "index,"
    "layer_index,"
    "in_layer_index",
    [
        (51, 5, 0),
        (52, 5, 1),
        (53, 5, 2),
        (54, 5, 3),
        (55, 5, 4),
        (56, 5, 5),
        (57, 5, 6),
        (58, 5, 7),
        (59, 5, 8),
        (60, 5, 9),
        (61, 5, 10),
        (62, 5, 11),
        (63, 5, 12),
        (64, 5, 13),
        (65, 5, 14),
        (66, 5, 15),
        (67, 5, 16),
        (68, 5, 17),
        (69, 5, 18),
        (70, 5, 19),
        (71, 6, 0),
        (72, 6, 1),
        (73, 6, 2),
        (74, 6, 3),
        (75, 6, 4),
        (76, 6, 5),
        (77, 6, 6),
        (78, 6, 7),
        (79, 6, 8),
        (80, 6, 9),
        (81, 6, 10),
        (82, 6, 11),
        (83, 6, 12),
        (84, 6, 13),
        (85, 6, 14),
        (86, 6, 15),
        (87, 6, 16),
        (88, 6, 17),
        (89, 6, 18),
        (90, 6, 19),
        (91, 7, 0),
        (92, 7, 1),
        (93, 7, 2),
        (94, 7, 3),
        (95, 7, 4),
        (96, 7, 5),
        (97, 7, 6),
        (98, 7, 7),
        (99, 7, 8),
        (100, 7, 9),
        (101, 7, 10),
        (102, 7, 11),
        (103, 7, 12),
        (104, 7, 13),
        (105, 7, 14),
        (106, 7, 15),
        (107, 7, 16),
        (108, 7, 17),
        (109, 7, 18),
        (110, 7, 19),
    ]
)
def test_creation_of_node_b_for_schema_four(
        index,
        layer_index,
        in_layer_index,
        schema_four,  # function fixture
):
    node_b = NodeB(layer_index, in_layer_index, schema_four.constants)
    assert node_b.INDEX == index
    assert node_b.LAYER_INDEX == layer_index
    assert node_b.IN_LAYER_INDEX == in_layer_index

    node_b = NodeB.create_node_by_index(index, schema_four.constants)
    assert node_b.INDEX == index
    assert node_b.LAYER_INDEX == layer_index
    assert node_b.IN_LAYER_INDEX == in_layer_index


@pytest.mark.parametrize(
    "node_params,"
    "neighboring_nodes_params",
    [
        ((3, 0), ((2, 9), (2, 0), (3, 1), (4, 1), (4, 0), (3, 9))),  # for node index 16
        ((3, 1), ((2, 0), (2, 1), (3, 2), (4, 2), (4, 1), (3, 0))),  # for node index 17
        ((3, 2), ((2, 1), (2, 2), (3, 3), (4, 3), (4, 2), (3, 1))),  # for node index 18
        ((3, 3), ((2, 2), (2, 3), (3, 4), (4, 4), (4, 3), (3, 2))),  # for node index 19
        ((3, 4), ((2, 3), (2, 4), (3, 5), (4, 5), (4, 4), (3, 3))),  # for node index 20
        ((3, 5), ((2, 4), (2, 5), (3, 6), (4, 6), (4, 5), (3, 4))),  # for node index 21
        ((3, 6), ((2, 5), (2, 6), (3, 7), (4, 7), (4, 6), (3, 5))),  # for node index 22
        ((3, 7), ((2, 6), (2, 7), (3, 8), (4, 8), (4, 7), (3, 6))),  # for node index 23
        ((3, 8), ((2, 7), (2, 8), (3, 9), (4, 9), (4, 8), (3, 7))),  # for node index 24
        ((3, 9), ((2, 8), (2, 9), (3, 0), (4, 0), (4, 9), (3, 8))),  # for node index 25
    ]
)
def test_getting_layer_and_in_layer_indices_of_neighboring_nodes_for_schema_two(
        node_params,
        neighboring_nodes_params,
        schema_two,  # function fixture
):
    layer_index, in_layer_index = node_params
    node_b = NodeB(layer_index, in_layer_index, schema_two.constants)
    assert node_b.get_layer_and_in_layer_indices_of_neighboring_nodes() == neighboring_nodes_params


@pytest.mark.parametrize(
    "node_params,"
    "neighboring_nodes_params",
    [
        ((4, 0), ((3, 14), (3, 0), (4, 1), (5, 1), (5, 0), (4, 14))),  # for node index 31
        ((4, 1), ((3, 0), (3, 1), (4, 2), (5, 2), (5, 1), (4, 0))),  # for node index 32
        ((4, 2), ((3, 1), (3, 2), (4, 3), (5, 3), (5, 2), (4, 1))),  # for node index 33
        ((4, 3), ((3, 2), (3, 3), (4, 4), (5, 4), (5, 3), (4, 2))),  # for node index 34
        ((4, 4), ((3, 3), (3, 4), (4, 5), (5, 5), (5, 4), (4, 3))),  # for node index 35
        ((4, 5), ((3, 4), (3, 5), (4, 6), (5, 6), (5, 5), (4, 4))),  # for node index 36
        ((4, 6), ((3, 5), (3, 6), (4, 7), (5, 7), (5, 6), (4, 5))),  # for node index 37
        ((4, 7), ((3, 6), (3, 7), (4, 8), (5, 8), (5, 7), (4, 6))),  # for node index 38
        ((4, 8), ((3, 7), (3, 8), (4, 9), (5, 9), (5, 8), (4, 7))),  # for node index 39
        ((4, 9), ((3, 8), (3, 9), (4, 10), (5, 10), (5, 9), (4, 8))),  # for node index 40
        ((4, 10), ((3, 9), (3, 10), (4, 11), (5, 11), (5, 10), (4, 9))),  # for node index 41
        ((4, 11), ((3, 10), (3, 11), (4, 12), (5, 12), (5, 11), (4, 10))),  # for node index 42
        ((4, 12), ((3, 11), (3, 12), (4, 13), (5, 13), (5, 12), (4, 11))),  # for node index 43
        ((4, 13), ((3, 12), (3, 13), (4, 14), (5, 14), (5, 13), (4, 12))),  # for node index 44
        ((4, 14), ((3, 13), (3, 14), (4, 0), (5, 0), (5, 14), (4, 13))),  # for node index 45
        ((5, 0), ((4, 14), (4, 0), (5, 1), (6, 1), (6, 0), (5, 14))),  # for node index 46
        ((5, 1), ((4, 0), (4, 1), (5, 2), (6, 2), (6, 1), (5, 0))),  # for node index 47
        ((5, 2), ((4, 1), (4, 2), (5, 3), (6, 3), (6, 2), (5, 1))),  # for node index 48
        ((5, 3), ((4, 2), (4, 3), (5, 4), (6, 4), (6, 3), (5, 2))),  # for node index 49
        ((5, 4), ((4, 3), (4, 4), (5, 5), (6, 5), (6, 4), (5, 3))),  # for node index 50
        ((5, 5), ((4, 4), (4, 5), (5, 6), (6, 6), (6, 5), (5, 4))),  # for node index 51
        ((5, 6), ((4, 5), (4, 6), (5, 7), (6, 7), (6, 6), (5, 5))),  # for node index 52
        ((5, 7), ((4, 6), (4, 7), (5, 8), (6, 8), (6, 7), (5, 6))),  # for node index 53
        ((5, 8), ((4, 7), (4, 8), (5, 9), (6, 9), (6, 8), (5, 7))),  # for node index 54
        ((5, 9), ((4, 8), (4, 9), (5, 10), (6, 10), (6, 9), (5, 8))),  # for node index 55
        ((5, 10), ((4, 9), (4, 10), (5, 11), (6, 11), (6, 10), (5, 9))),  # for node index 56
        ((5, 11), ((4, 10), (4, 11), (5, 12), (6, 12), (6, 11), (5, 10))),  # for node index 57
        ((5, 12), ((4, 11), (4, 12), (5, 13), (6, 13), (6, 12), (5, 11))),  # for node index 58
        ((5, 13), ((4, 12), (4, 13), (5, 14), (6, 14), (6, 13), (5, 12))),  # for node index 59
        ((5, 14), ((4, 13), (4, 14), (5, 0), (6, 0), (6, 14), (5, 13))),  # for node index 60
    ]
)
def test_getting_layer_and_in_layer_indices_of_neighboring_nodes_for_schema_three(
    node_params,
    neighboring_nodes_params,
    schema_three,  # function fixture
):
    layer_index, in_layer_index = node_params
    node_b = NodeB(layer_index, in_layer_index, schema_three.constants)
    assert node_b.get_layer_and_in_layer_indices_of_neighboring_nodes() == neighboring_nodes_params


@pytest.mark.parametrize(
    "node_params,"
    "neighboring_nodes_params",
    [
        ((5, 0), ((4, 19), (4, 0), (5, 1), (6, 1), (6, 0), (5, 19))),  # for node index 51
        ((5, 1), ((4, 0), (4, 1), (5, 2), (6, 2), (6, 1), (5, 0))),  # for node index 52
        ((5, 2), ((4, 1), (4, 2), (5, 3), (6, 3), (6, 2), (5, 1))),  # for node index 53
        ((5, 3), ((4, 2), (4, 3), (5, 4), (6, 4), (6, 3), (5, 2))),  # for node index 54
        ((5, 4), ((4, 3), (4, 4), (5, 5), (6, 5), (6, 4), (5, 3))),  # for node index 55
        ((5, 5), ((4, 4), (4, 5), (5, 6), (6, 6), (6, 5), (5, 4))),  # for node index 56
        ((5, 6), ((4, 5), (4, 6), (5, 7), (6, 7), (6, 6), (5, 5))),  # for node index 57
        ((5, 7), ((4, 6), (4, 7), (5, 8), (6, 8), (6, 7), (5, 6))),  # for node index 58
        ((5, 8), ((4, 7), (4, 8), (5, 9), (6, 9), (6, 8), (5, 7))),  # for node index 59
        ((5, 9), ((4, 8), (4, 9), (5, 10), (6, 10), (6, 9), (5, 8))),  # for node index 60
        ((5, 10), ((4, 9), (4, 10), (5, 11), (6, 11), (6, 10), (5, 9))),  # for node index 61
        ((5, 11), ((4, 10), (4, 11), (5, 12), (6, 12), (6, 11), (5, 10))),  # for node index 62
        ((5, 12), ((4, 11), (4, 12), (5, 13), (6, 13), (6, 12), (5, 11))),  # for node index 63
        ((5, 13), ((4, 12), (4, 13), (5, 14), (6, 14), (6, 13), (5, 12))),  # for node index 64
        ((5, 14), ((4, 13), (4, 14), (5, 15), (6, 15), (6, 14), (5, 13))),  # for node index 65
        ((5, 15), ((4, 14), (4, 15), (5, 16), (6, 16), (6, 15), (5, 14))),  # for node index 66
        ((5, 16), ((4, 15), (4, 16), (5, 17), (6, 17), (6, 16), (5, 15))),  # for node index 67
        ((5, 17), ((4, 16), (4, 17), (5, 18), (6, 18), (6, 17), (5, 16))),  # for node index 68
        ((5, 18), ((4, 17), (4, 18), (5, 19), (6, 19), (6, 18), (5, 17))),  # for node index 69
        ((5, 19), ((4, 18), (4, 19), (5, 0), (6, 0), (6, 19), (5, 18))),  # node_index 70
        ((6, 0), ((5, 19), (5, 0), (6, 1), (7, 1), (7, 0), (6, 19))),  # node_index 71
        ((6, 1), ((5, 0), (5, 1), (6, 2), (7, 2), (7, 1), (6, 0))),  # for node index 72
        ((6, 2), ((5, 1), (5, 2), (6, 3), (7, 3), (7, 2), (6, 1))),  # for node index 73
        ((6, 3), ((5, 2), (5, 3), (6, 4), (7, 4), (7, 3), (6, 2))),  # for node index 74
        ((6, 4), ((5, 3), (5, 4), (6, 5), (7, 5), (7, 4), (6, 3))),  # for node index 75
        ((6, 5), ((5, 4), (5, 5), (6, 6), (7, 6), (7, 5), (6, 4))),  # for node index 76
        ((6, 6), ((5, 5), (5, 6), (6, 7), (7, 7), (7, 6), (6, 5))),  # for node index 77
        ((6, 7), ((5, 6), (5, 7), (6, 8), (7, 8), (7, 7), (6, 6))),  # for node index 78
        ((6, 8), ((5, 7), (5, 8), (6, 9), (7, 9), (7, 8), (6, 7))),  # for node index 79
        ((6, 9), ((5, 8), (5, 9), (6, 10), (7, 10), (7, 9), (6, 8))),  # for node index 80
        ((6, 10), ((5, 9), (5, 10), (6, 11), (7, 11), (7, 10), (6, 9))),  # for node index 81
        ((6, 11), ((5, 10), (5, 11), (6, 12), (7, 12), (7, 11), (6, 10))),  # for node index 82
        ((6, 12), ((5, 11), (5, 12), (6, 13), (7, 13), (7, 12), (6, 11))),  # for node index 83
        ((6, 13), ((5, 12), (5, 13), (6, 14), (7, 14), (7, 13), (6, 12))),  # for node index 84
        ((6, 14), ((5, 13), (5, 14), (6, 15), (7, 15), (7, 14), (6, 13))),  # for node index 85
        ((6, 15), ((5, 14), (5, 15), (6, 16), (7, 16), (7, 15), (6, 14))),  # for node index 86
        ((6, 16), ((5, 15), (5, 16), (6, 17), (7, 17), (7, 16), (6, 15))),  # for node index 87
        ((6, 17), ((5, 16), (5, 17), (6, 18), (7, 18), (7, 17), (6, 16))),  # for node index 88
        ((6, 18), ((5, 17), (5, 18), (6, 19), (7, 19), (7, 18), (6, 17))),  # for node index 89
        ((6, 19), ((5, 18), (5, 19), (6, 0), (7, 0), (7, 19), (6, 18))),  # node_index 90
        ((7, 0), ((6, 19), (6, 0), (7, 1), (8, 1), (8, 0), (7, 19))),  # node_index 91
        ((7, 1), ((6, 0), (6, 1), (7, 2), (8, 2), (8, 1), (7, 0))),  # for node index 92
        ((7, 2), ((6, 1), (6, 2), (7, 3), (8, 3), (8, 2), (7, 1))),  # for node index 93
        ((7, 3), ((6, 2), (6, 3), (7, 4), (8, 4), (8, 3), (7, 2))),  # for node index 94
        ((7, 4), ((6, 3), (6, 4), (7, 5), (8, 5), (8, 4), (7, 3))),  # for node index 95
        ((7, 5), ((6, 4), (6, 5), (7, 6), (8, 6), (8, 5), (7, 4))),  # for node index 96
        ((7, 6), ((6, 5), (6, 6), (7, 7), (8, 7), (8, 6), (7, 5))),  # for node index 97
        ((7, 7), ((6, 6), (6, 7), (7, 8), (8, 8), (8, 7), (7, 6))),  # for node index 98
        ((7, 8), ((6, 7), (6, 8), (7, 9), (8, 9), (8, 8), (7, 7))),  # for node index 99
        ((7, 9), ((6, 8), (6, 9), (7, 10), (8, 10), (8, 9), (7, 8))),  # for node index 100
        ((7, 10), ((6, 9), (6, 10), (7, 11), (8, 11), (8, 10), (7, 9))),  # for node index 101
        ((7, 11), ((6, 10), (6, 11), (7, 12), (8, 12), (8, 11), (7, 10))),  # for node index 102
        ((7, 12), ((6, 11), (6, 12), (7, 13), (8, 13), (8, 12), (7, 11))),  # for node index 103
        ((7, 13), ((6, 12), (6, 13), (7, 14), (8, 14), (8, 13), (7, 12))),  # for node index 104
        ((7, 14), ((6, 13), (6, 14), (7, 15), (8, 15), (8, 14), (7, 13))),  # for node index 105
        ((7, 15), ((6, 14), (6, 15), (7, 16), (8, 16), (8, 15), (7, 14))),  # for node index 106
        ((7, 16), ((6, 15), (6, 16), (7, 17), (8, 17), (8, 16), (7, 15))),  # for node index 107
        ((7, 17), ((6, 16), (6, 17), (7, 18), (8, 18), (8, 17), (7, 16))),  # for node index 108
        ((7, 18), ((6, 17), (6, 18), (7, 19), (8, 19), (8, 18), (7, 17))),  # for node index 109
        ((7, 19), ((6, 18), (6, 19), (7, 0), (8, 0), (8, 19), (7, 18))),  # node_index 110
    ]
)
def test_getting_layer_and_in_layer_indices_of_neighboring_nodes_for_schema_four(
        node_params,
        neighboring_nodes_params,
        schema_four,  # function fixture
):
    schema = schema_four
    layer_index, in_layer_index = node_params
    node_b = NodeB(layer_index, in_layer_index, schema.constants)
    assert node_b.get_layer_and_in_layer_indices_of_neighboring_nodes() == neighboring_nodes_params
