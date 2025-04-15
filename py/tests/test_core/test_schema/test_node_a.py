import pytest

from core.schema.node_a import NodeA


@pytest.mark.parametrize(
    "index,"
    "layer_index,"
    "in_layer_index,"
    "number_of_nodes_in_layer,"
    "index_offset_for_layer",
    [
        (1, 1, 0, 5, 1),
        (2, 1, 1, 5, 1),
        (3, 1, 2, 5, 1),
        (4, 1, 3, 5, 1),
        (5, 1, 4, 5, 1),
        (6, 2, 0, 10, 6),
        (7, 2, 1, 10, 6),
        (8, 2, 2, 10, 6),
        (9, 2, 3, 10, 6),
        (10, 2, 4, 10, 6),
        (11, 2, 5, 10, 6),
        (12, 2, 6, 10, 6),
        (13, 2, 7, 10, 6),
        (14, 2, 8, 10, 6),
        (15, 2, 9, 10, 6),
        (16, 3, 0, 15, 16),
        (17, 3, 1, 15, 16),
        (18, 3, 2, 15, 16),
        (19, 3, 3, 15, 16),
        (20, 3, 4, 15, 16),
        (21, 3, 5, 15, 16),
        (22, 3, 6, 15, 16),
        (23, 3, 7, 15, 16),
        (24, 3, 8, 15, 16),
        (25, 3, 9, 15, 16),
        (26, 3, 10, 15, 16),
        (27, 3, 11, 15, 16),
        (28, 3, 12, 15, 16),
        (29, 3, 13, 15, 16),
        (30, 3, 14, 15, 16),
        (31, 4, 0, 20, 31),
        (32, 4, 1, 20, 31),
        (33, 4, 2, 20, 31),
        (34, 4, 3, 20, 31),
        (35, 4, 4, 20, 31),
        (36, 4, 5, 20, 31),
        (37, 4, 6, 20, 31),
        (38, 4, 7, 20, 31),
        (39, 4, 8, 20, 31),
        (40, 4, 9, 20, 31),
        (41, 4, 10, 20, 31),
        (42, 4, 11, 20, 31),
        (43, 4, 12, 20, 31),
        (44, 4, 13, 20, 31),
        (45, 4, 14, 20, 31),
        (46, 4, 15, 20, 31),
        (47, 4, 16, 20, 31),
        (48, 4, 17, 20, 31),
        (49, 4, 18, 20, 31),
        (50, 4, 19, 20, 31),
        (51, 5, 0, 25, 51),
    ]
)
def test_indices(
    index,
    layer_index,
    in_layer_index,
    number_of_nodes_in_layer,
    index_offset_for_layer,
):
    node_a = NodeA(index)
    assert node_a.INDEX == index
    assert node_a.LAYER_INDEX == layer_index
    assert node_a.IN_LAYER_INDEX == in_layer_index
    assert node_a.NUMBER_OF_NODES_IN_LAYER == number_of_nodes_in_layer
    assert node_a.INDEX_OFFSET_FOR_LAYER == index_offset_for_layer
    assert node_a.INDEX == node_a.INDEX_OFFSET_FOR_LAYER + node_a.IN_LAYER_INDEX
