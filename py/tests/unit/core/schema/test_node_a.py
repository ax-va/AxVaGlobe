import pytest

from core.schema.node_a import _NodeA


@pytest.mark.parametrize(
    "index,"
    "layer_index,"
    "in_layer_index",
    [
        (1, 1, 0),
        (2, 1, 1),
        (3, 1, 2),
        (4, 1, 3),
        (5, 1, 4),
    ]
)
def test_creation_of_node_a_for_schema_two(
        index,
        layer_index,
        in_layer_index,
        schema_two,  # function fixture
):
    node_a = _NodeA(layer_index, in_layer_index, schema_two)
    assert node_a.INDEX == index
    assert node_a.LAYER_INDEX == layer_index
    assert node_a.IN_LAYER_INDEX == in_layer_index

    node_a = _NodeA.create_node_by_index(index, schema_two)
    assert node_a.INDEX == index
    assert node_a.LAYER_INDEX == layer_index
    assert node_a.IN_LAYER_INDEX == in_layer_index


@pytest.mark.parametrize(
    "index,"
    "layer_index,"
    "in_layer_index",
    [
        (1, 1, 0),
        (2, 1, 1),
        (3, 1, 2),
        (4, 1, 3),
        (5, 1, 4),
        (6, 2, 0),
        (7, 2, 1),
        (8, 2, 2),
        (9, 2, 3),
        (10, 2, 4),
        (11, 2, 5),
        (12, 2, 6),
        (13, 2, 7),
        (14, 2, 8),
        (15, 2, 9),
    ]
)
def test_creation_of_node_a_for_schema_three(
        index,
        layer_index,
        in_layer_index,
        schema_three,  # function fixture
):
    node_a = _NodeA(layer_index, in_layer_index, schema_three)
    assert node_a.INDEX == index
    assert node_a.LAYER_INDEX == layer_index
    assert node_a.IN_LAYER_INDEX == in_layer_index

    node_a = _NodeA.create_node_by_index(index, schema_three)
    assert node_a.INDEX == index
    assert node_a.LAYER_INDEX == layer_index
    assert node_a.IN_LAYER_INDEX == in_layer_index


@pytest.mark.parametrize(
    "index,"
    "layer_index,"
    "in_layer_index",
    [
        (1, 1, 0),
        (2, 1, 1),
        (3, 1, 2),
        (4, 1, 3),
        (5, 1, 4),
        (6, 2, 0),
        (7, 2, 1),
        (8, 2, 2),
        (9, 2, 3),
        (10, 2, 4),
        (11, 2, 5),
        (12, 2, 6),
        (13, 2, 7),
        (14, 2, 8),
        (15, 2, 9),
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
        (26, 3, 10),
        (27, 3, 11),
        (28, 3, 12),
        (29, 3, 13),
        (30, 3, 14),
    ]
)
def test_creation_of_node_a_for_schema_four(
        index,
        layer_index,
        in_layer_index,
        schema_four,  # function fixture
):
    node_a = _NodeA(layer_index, in_layer_index, schema_four)
    assert node_a.INDEX == index
    assert node_a.LAYER_INDEX == layer_index
    assert node_a.IN_LAYER_INDEX == in_layer_index

    node_a = _NodeA.create_node_by_index(index, schema_four)
    assert node_a.INDEX == index
    assert node_a.LAYER_INDEX == layer_index
    assert node_a.IN_LAYER_INDEX == in_layer_index


@pytest.mark.parametrize(
    "index,"
    "layer_index,"
    "in_layer_index",
    [
        (1, 1, 0),
        (2, 1, 1),
        (3, 1, 2),
        (4, 1, 3),
        (5, 1, 4),
        (6, 2, 0),
        (7, 2, 1),
        (8, 2, 2),
        (9, 2, 3),
        (10, 2, 4),
        (11, 2, 5),
        (12, 2, 6),
        (13, 2, 7),
        (14, 2, 8),
        (15, 2, 9),
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
        (26, 3, 10),
        (27, 3, 11),
        (28, 3, 12),
        (29, 3, 13),
        (30, 3, 14),
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
        (46, 4, 15),
        (47, 4, 16),
        (48, 4, 17),
        (49, 4, 18),
        (50, 4, 19),
    ]
)
def test_creation_of_node_a_for_schema_five(
        index,
        layer_index,
        in_layer_index,
        schema_five,  # function fixture
):
    node_a = _NodeA(layer_index, in_layer_index, schema_five)
    assert node_a.INDEX == index
    assert node_a.LAYER_INDEX == layer_index
    assert node_a.IN_LAYER_INDEX == in_layer_index

    node_a = _NodeA.create_node_by_index(index, schema_five)
    assert node_a.INDEX == index
    assert node_a.LAYER_INDEX == layer_index
    assert node_a.IN_LAYER_INDEX == in_layer_index


@pytest.mark.parametrize(
    "node_params,"
    "neighboring_nodes_params",
    [
        ((1, 0), ((0, 0), (1, 1), (2, 1), (2, 0), (2, 9), (1, 4))),  # node_index 1
        ((1, 1), ((0, 0), (1, 2), (2, 3), (2, 2), (2, 1), (1, 0))),  # node_index 2
        ((1, 2), ((0, 0), (1, 3), (2, 5), (2, 4), (2, 3), (1, 1))),  # node_index 3
        ((1, 3), ((0, 0), (1, 4), (2, 7), (2, 6), (2, 5), (1, 2))),  # node_index 4
        ((1, 4), ((0, 0), (1, 0), (2, 9), (2, 8), (2, 7), (1, 3))),  # node_index 5
    ]
)
def test_getting_layer_and_in_layer_indices_of_neighboring_nodes_for_schema_two(
    node_params,
    neighboring_nodes_params,
    schema_two,  # function fixture
):
    layer_index, in_layer_index = node_params
    node_a = _NodeA(layer_index, in_layer_index, schema_two)
    assert node_a.get_layer_and_in_layer_indices_of_neighboring_nodes() == neighboring_nodes_params


@pytest.mark.parametrize(
    "node_params,"
    "neighboring_nodes_params",
    [
        ((1, 0), ((0, 0), (1, 1), (2, 1), (2, 0), (2, 9), (1, 4))),  # node_index 1
        ((1, 1), ((0, 0), (1, 2), (2, 3), (2, 2), (2, 1), (1, 0))),  # node_index 2
        ((1, 2), ((0, 0), (1, 3), (2, 5), (2, 4), (2, 3), (1, 1))),  # node_index 3
        ((1, 3), ((0, 0), (1, 4), (2, 7), (2, 6), (2, 5), (1, 2))),  # node_index 4
        ((1, 4), ((0, 0), (1, 0), (2, 9), (2, 8), (2, 7), (1, 3))),  # node_index 5
        ((2, 0), ((1, 0), (2, 1), (3, 1), (3, 0), (3, 14), (2, 9))), # node_index 6
        ((2, 1), ((1, 0), (1, 1), (2, 2), (3, 2), (3, 1), (2, 0))),  # node_index 7
        ((2, 2), ((1, 1), (2, 3), (3, 4), (3, 3), (3, 2), (2, 1))),  # node_index 8
        ((2, 3), ((1, 1), (1, 2), (2, 4), (3, 5), (3, 4), (2, 2))),  # node_index 9
        ((2, 4), ((1, 2), (2, 5), (3, 7), (3, 6), (3, 5), (2, 3))),  # node_index 10
        ((2, 5), ((1, 2), (1, 3), (2, 6), (3, 8), (3, 7), (2, 4))),  # node_index 11
        ((2, 6), ((1, 3), (2, 7), (3, 10), (3, 9), (3, 8), (2, 5))),  # node_index 12
        ((2, 7), ((1, 3), (1, 4), (2, 8), (3, 11), (3, 10), (2, 6))), # node_index 13
        ((2, 8), ((1, 4), (2, 9), (3, 13), (3, 12), (3, 11), (2, 7))),  # node_index 14
        ((2, 9), ((1, 4), (1, 0), (2, 0), (3, 14), (3, 13), (2, 8))),  # node_index 15
    ]
)
def test_getting_layer_and_in_layer_indices_of_neighboring_nodes_for_schema_three(
    node_params,
    neighboring_nodes_params,
    schema_three,  # function fixture
):
    layer_index, in_layer_index = node_params
    node_a = _NodeA(layer_index, in_layer_index, schema_three)
    assert node_a.get_layer_and_in_layer_indices_of_neighboring_nodes() == neighboring_nodes_params


@pytest.mark.parametrize(
    "node_params,"
    "neighboring_nodes_params",
    [
        ((1, 0), ((0, 0), (1, 1), (2, 1), (2, 0), (2, 9), (1, 4))),  # node_index 1
        ((1, 1), ((0, 0), (1, 2), (2, 3), (2, 2), (2, 1), (1, 0))),  # node_index 2
        ((1, 2), ((0, 0), (1, 3), (2, 5), (2, 4), (2, 3), (1, 1))),  # node_index 3
        ((1, 3), ((0, 0), (1, 4), (2, 7), (2, 6), (2, 5), (1, 2))),  # node_index 4
        ((1, 4), ((0, 0), (1, 0), (2, 9), (2, 8), (2, 7), (1, 3))),  # node_index 5
        ((2, 0), ((1, 0), (2, 1), (3, 1), (3, 0), (3, 14), (2, 9))), # node_index 6
        ((2, 1), ((1, 0), (1, 1), (2, 2), (3, 2), (3, 1), (2, 0))),  # node_index 7
        ((2, 2), ((1, 1), (2, 3), (3, 4), (3, 3), (3, 2), (2, 1))),  # node_index 8
        ((2, 3), ((1, 1), (1, 2), (2, 4), (3, 5), (3, 4), (2, 2))),  # node_index 9
        ((2, 4), ((1, 2), (2, 5), (3, 7), (3, 6), (3, 5), (2, 3))),  # node_index 10
        ((2, 5), ((1, 2), (1, 3), (2, 6), (3, 8), (3, 7), (2, 4))),  # node_index 11
        ((2, 6), ((1, 3), (2, 7), (3, 10), (3, 9), (3, 8), (2, 5))),  # node_index 12
        ((2, 7), ((1, 3), (1, 4), (2, 8), (3, 11), (3, 10), (2, 6))), # node_index 13
        ((2, 8), ((1, 4), (2, 9), (3, 13), (3, 12), (3, 11), (2, 7))),  # node_index 14
        ((2, 9), ((1, 4), (1, 0), (2, 0), (3, 14), (3, 13), (2, 8))),  # node_index 15
        ((3, 0), ((2, 0), (3, 1), (4, 1), (4, 0), (4, 19), (3, 14))),  # node_index 16
        ((3, 1), ((2, 0), (2, 1), (3, 2), (4, 2), (4, 1), (3, 0))),  # node_index 17
        ((3, 2), ((2, 1), (2, 2), (3, 3), (4, 3), (4, 2), (3, 1))),  # node_index 18
        ((3, 3), ((2, 2), (3, 4), (4, 5), (4, 4), (4, 3), (3, 2))),  # node_index 19
        ((3, 4), ((2, 2), (2, 3), (3, 5), (4, 6), (4, 5), (3, 3))),  # node_index 20
        ((3, 5), ((2, 3), (2, 4), (3, 6), (4, 7), (4, 6), (3, 4))),  # node_index 21
    ]
)
def test_getting_layer_and_in_layer_indices_of_neighboring_nodes_for_schema_four(
    node_params,
    neighboring_nodes_params,
    schema_four,  # function fixture
):
    layer_index, in_layer_index = node_params
    node_a = _NodeA(layer_index, in_layer_index, schema_four)
    assert node_a.get_layer_and_in_layer_indices_of_neighboring_nodes() == neighboring_nodes_params
