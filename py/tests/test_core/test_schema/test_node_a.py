import pytest

from core.schema.schema import Schema
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
):
    schema = Schema(2)
    node_a = _NodeA(layer_index, in_layer_index, schema)
    assert node_a.INDEX == index
    assert node_a.LAYER_INDEX == layer_index
    assert node_a.IN_LAYER_INDEX == in_layer_index

    node_a = _NodeA.create_node_by_index(index, schema)
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
):
    schema = Schema(3)
    node_a = _NodeA(layer_index, in_layer_index, schema)
    assert node_a.INDEX == index
    assert node_a.LAYER_INDEX == layer_index
    assert node_a.IN_LAYER_INDEX == in_layer_index

    node_a = _NodeA.create_node_by_index(index, schema)
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
):
    schema = Schema(4)
    node_a = _NodeA(layer_index, in_layer_index, schema)
    assert node_a.INDEX == index
    assert node_a.LAYER_INDEX == layer_index
    assert node_a.IN_LAYER_INDEX == in_layer_index

    node_a = _NodeA.create_node_by_index(index, schema)
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
):
    schema = Schema(5)
    node_a = _NodeA(layer_index, in_layer_index, schema)
    assert node_a.INDEX == index
    assert node_a.LAYER_INDEX == layer_index
    assert node_a.IN_LAYER_INDEX == in_layer_index

    node_a = _NodeA.create_node_by_index(index, schema)
    assert node_a.INDEX == index
    assert node_a.LAYER_INDEX == layer_index
    assert node_a.IN_LAYER_INDEX == in_layer_index

@pytest.mark.parametrize(
    "index,"
    "layer_and_in_layer_indices",
    [
        (1, ((0, 0), (1, 1), (2, 1), (2, 0), (2, 9), (1, 4))),
        (2, ((0, 0), (1, 2), (2, 3), (2, 2), (2, 1), (1, 0))),
        (3, ((0, 0), (1, 3), (2, 5), (2, 4), (2, 3), (1, 1))),
        (4, ((0, 0), (1, 4), (2, 7), (2, 6), (2, 5), (1, 2))),
        (5, ((0, 0), (1, 0), (2, 9), (2, 8), (2, 7), (1, 3))),
    ]
)
def test_getting_layer_and_in_layer_indices_of_neighboring_nodes_for_schema_two(
    index,
    layer_and_in_layer_indices,
):
    schema = Schema(2)
    node_a = _NodeA.create_node_by_index(index, schema)
    assert node_a.get_layer_and_in_layer_indices_of_neighboring_nodes() == layer_and_in_layer_indices

@pytest.mark.parametrize(
    "index,"
    "layer_and_in_layer_indices",
    [
        (1, ((0, 0), (1, 1), (2, 1), (2, 0), (2, 9), (1, 4))),
        (2, ((0, 0), (1, 2), (2, 3), (2, 2), (2, 1), (1, 0))),
        (3, ((0, 0), (1, 3), (2, 5), (2, 4), (2, 3), (1, 1))),
        (4, ((0, 0), (1, 4), (2, 7), (2, 6), (2, 5), (1, 2))),
        (5, ((0, 0), (1, 0), (2, 9), (2, 8), (2, 7), (1, 3))),
        (6, ((1, 0), (2, 1), (3, 1), (3, 0), (3, 14), (2, 9))),
        (7, ((1, 0), (1, 1), (2, 2), (3, 2), (3, 1), (2, 0))),
        (8, ((1, 1), (2, 3), (3, 4), (3, 3), (3, 2), (2, 1))),
        (9, ((1, 1), (1, 2), (2, 4), (3, 5), (3, 4), (2, 2))),
        (10, ((1, 2), (2, 5), (3, 7), (3, 6), (3, 5), (2, 3))),
    ]
)
def test_getting_layer_and_in_layer_indices_of_neighboring_nodes_for_schema_three(
    index,
    layer_and_in_layer_indices,
):
    schema = Schema(3)
    node_a = _NodeA.create_node_by_index(index, schema)
    assert node_a.get_layer_and_in_layer_indices_of_neighboring_nodes() == layer_and_in_layer_indices
