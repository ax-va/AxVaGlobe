import pytest

from core.schema.schema import Schema
from core.schema.node_b import _NodeB


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
):
    schema = Schema(2)
    node_b = _NodeB(layer_index, in_layer_index, schema)
    assert node_b.INDEX == index
    assert node_b.LAYER_INDEX == layer_index
    assert node_b.IN_LAYER_INDEX == in_layer_index

    node_b = _NodeB.create_node_by_index(index, schema)
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
):
    schema = Schema(3)
    node_b = _NodeB(layer_index, in_layer_index, schema)
    assert node_b.INDEX == index
    assert node_b.LAYER_INDEX == layer_index
    assert node_b.IN_LAYER_INDEX == in_layer_index

    node_b = _NodeB.create_node_by_index(index, schema)
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
):
    schema = Schema(4)
    node_b = _NodeB(layer_index, in_layer_index, schema)
    assert node_b.INDEX == index
    assert node_b.LAYER_INDEX == layer_index
    assert node_b.IN_LAYER_INDEX == in_layer_index

    node_b = _NodeB.create_node_by_index(index, schema)
    assert node_b.INDEX == index
    assert node_b.LAYER_INDEX == layer_index
    assert node_b.IN_LAYER_INDEX == in_layer_index


@pytest.mark.parametrize(
    "index,"
    "layer_and_in_layer_indices",
    [
        (16, ((2, 9), (2, 0), (3, 1), (4, 1), (4, 0), (3, 9))),
        (17, ((2, 0), (2, 1), (3, 2), (4, 2), (4, 1), (3, 0))),
        (18, ((2, 1), (2, 2), (3, 3), (4, 3), (4, 2), (3, 1))),
        (19, ((2, 2), (2, 3), (3, 4), (4, 4), (4, 3), (3, 2))),
        (20, ((2, 3), (2, 4), (3, 5), (4, 5), (4, 4), (3, 3))),
        (21, ((2, 4), (2, 5), (3, 6), (4, 6), (4, 5), (3, 4))),
        (22, ((2, 5), (2, 6), (3, 7), (4, 7), (4, 6), (3, 5))),
        (23, ((2, 6), (2, 7), (3, 8), (4, 8), (4, 7), (3, 6))),
        (24, ((2, 7), (2, 8), (3, 9), (4, 9), (4, 8), (3, 7))),
        (25, ((2, 8), (2, 9), (3, 0), (4, 0), (4, 9), (3, 8))),
    ]
)
def test_getting_layer_and_in_layer_indices_of_neighboring_nodes_for_schema_two(
    index,
    layer_and_in_layer_indices,
):
    schema = Schema(2)
    node = _NodeB.create_node_by_index(index, schema)
    assert node.get_layer_and_in_layer_indices_of_neighboring_nodes() == layer_and_in_layer_indices


@pytest.mark.parametrize(
    "index,"
    "layer_and_in_layer_indices",
    [
        (31, ((3, 14), (3, 0), (4, 1), (5, 1), (5, 0), (4, 14))),
        (32, ((3, 0), (3, 1), (4, 2), (5, 2), (5, 1), (4, 0))),
        (33, ((3, 1), (3, 2), (4, 3), (5, 3), (5, 2), (4, 1))),
        (34, ((3, 2), (3, 3), (4, 4), (5, 4), (5, 3), (4, 2))),
        (35, ((3, 3), (3, 4), (4, 5), (5, 5), (5, 4), (4, 3))),
        (36, ((3, 4), (3, 5), (4, 6), (5, 6), (5, 5), (4, 4))),
        (37, ((3, 5), (3, 6), (4, 7), (5, 7), (5, 6), (4, 5))),
        (38, ((3, 6), (3, 7), (4, 8), (5, 8), (5, 7), (4, 6))),
        (39, ((3, 7), (3, 8), (4, 9), (5, 9), (5, 8), (4, 7))),
        (40, ((3, 8), (3, 9), (4, 10), (5, 10), (5, 9), (4, 8))),
        (41, ((3, 9), (3, 10), (4, 11), (5, 11), (5, 10), (4, 9))),
        (42, ((3, 10), (3, 11), (4, 12), (5, 12), (5, 11), (4, 10))),
        (43, ((3, 11), (3, 12), (4, 13), (5, 13), (5, 12), (4, 11))),
        (44, ((3, 12), (3, 13), (4, 14), (5, 14), (5, 13), (4, 12))),
        (45, ((3, 13), (3, 14), (4, 0), (5, 0), (5, 14), (4, 13))),
        (46, ((4, 14), (4, 0), (5, 1), (6, 1), (6, 0), (5, 14))),
        (47, ((4, 0), (4, 1), (5, 2), (6, 2), (6, 1), (5, 0))),
        (48, ((4, 1), (4, 2), (5, 3), (6, 3), (6, 2), (5, 1))),
        (49, ((4, 2), (4, 3), (5, 4), (6, 4), (6, 3), (5, 2))),
        (50, ((4, 3), (4, 4), (5, 5), (6, 5), (6, 4), (5, 3))),
        (51, ((4, 4), (4, 5), (5, 6), (6, 6), (6, 5), (5, 4))),
        (52, ((4, 5), (4, 6), (5, 7), (6, 7), (6, 6), (5, 5))),
        (53, ((4, 6), (4, 7), (5, 8), (6, 8), (6, 7), (5, 6))),
        (54, ((4, 7), (4, 8), (5, 9), (6, 9), (6, 8), (5, 7))),
        (55, ((4, 8), (4, 9), (5, 10), (6, 10), (6, 9), (5, 8))),
        (56, ((4, 9), (4, 10), (5, 11), (6, 11), (6, 10), (5, 9))),
        (57, ((4, 10), (4, 11), (5, 12), (6, 12), (6, 11), (5, 10))),
        (58, ((4, 11), (4, 12), (5, 13), (6, 13), (6, 12), (5, 11))),
        (59, ((4, 12), (4, 13), (5, 14), (6, 14), (6, 13), (5, 12))),
        (60, ((4, 13), (4, 14), (5, 0), (6, 0), (6, 14), (5, 13))),
    ]
)
def test_getting_layer_and_in_layer_indices_of_neighboring_nodes_for_schema_three(
    index,
    layer_and_in_layer_indices,
):
    schema = Schema(3)
    node = _NodeB.create_node_by_index(index, schema)
    assert node.get_layer_and_in_layer_indices_of_neighboring_nodes() == layer_and_in_layer_indices
