import pytest

from core.schema.node_c import _NodeC


@pytest.mark.parametrize(
    "index,"
    "layer_index,"
    "in_layer_index",
    [
        (36, 5, 0),
        (37, 5, 1),
        (38, 5, 2),
        (39, 5, 3),
        (40, 5, 4),
    ]
)
def test_creation_of_node_c_for_schema_two(
        index,
        layer_index,
        in_layer_index,
        schema_two,  # function fixture
):
    node_c = _NodeC(layer_index, in_layer_index, schema_two)
    assert node_c.INDEX == index
    assert node_c.LAYER_INDEX == layer_index
    assert node_c.IN_LAYER_INDEX == in_layer_index

    node_c = _NodeC.create_node_by_index(index, schema_two)
    assert node_c.INDEX == index
    assert node_c.LAYER_INDEX == layer_index
    assert node_c.IN_LAYER_INDEX == in_layer_index


@pytest.mark.parametrize(
    "index,"
    "layer_index,"
    "in_layer_index",
    [
        (76, 7, 0),
        (77, 7, 1),
        (78, 7, 2),
        (79, 7, 3),
        (80, 7, 4),
        (81, 7, 5),
        (82, 7, 6),
        (83, 7, 7),
        (84, 7, 8),
        (85, 7, 9),
        (86, 8, 0),
        (87, 8, 1),
        (88, 8, 2),
        (89, 8, 3),
        (90, 8, 4),
    ]
)
def test_creation_of_node_c_for_schema_three(
        index,
        layer_index,
        in_layer_index,
        schema_three,  # function fixture
):
    node_c = _NodeC(layer_index, in_layer_index, schema_three)
    assert node_c.INDEX == index
    assert node_c.LAYER_INDEX == layer_index
    assert node_c.IN_LAYER_INDEX == in_layer_index

    node_c = _NodeC.create_node_by_index(index, schema_three)
    assert node_c.INDEX == index
    assert node_c.LAYER_INDEX == layer_index
    assert node_c.IN_LAYER_INDEX == in_layer_index


@pytest.mark.parametrize(
    "index,"
    "layer_index,"
    "in_layer_index",
    [
        (131, 9, 0),
        (132, 9, 1),
        (133, 9, 2),
        (134, 9, 3),
        (135, 9, 4),
        (136, 9, 5),
        (137, 9, 6),
        (138, 9, 7),
        (139, 9, 8),
        (140, 9, 9),
        (141, 9, 10),
        (142, 9, 11),
        (143, 9, 12),
        (144, 9, 13),
        (145, 9, 14),
        (146, 10, 0),
        (147, 10, 1),
        (148, 10, 2),
        (149, 10, 3),
        (150, 10, 4),
        (151, 10, 5),
        (152, 10, 6),
        (153, 10, 7),
        (154, 10, 8),
        (155, 10, 9),
        (156, 11, 0),
        (157, 11, 1),
        (158, 11, 2),
        (159, 11, 3),
        (160, 11, 4),
    ]
)
def test_creation_of_node_c_for_schema_four(
        index,
        layer_index,
        in_layer_index,
        schema_four,  # function fixture
):
    node_c = _NodeC(layer_index, in_layer_index, schema_four)
    assert node_c.INDEX == index
    assert node_c.LAYER_INDEX == layer_index
    assert node_c.IN_LAYER_INDEX == in_layer_index

    node_c = _NodeC.create_node_by_index(index, schema_four)
    assert node_c.INDEX == index
    assert node_c.LAYER_INDEX == layer_index
    assert node_c.IN_LAYER_INDEX == in_layer_index
