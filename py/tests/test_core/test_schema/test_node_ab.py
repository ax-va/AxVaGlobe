import pytest

from core.schema.constants import Constants
from core.schema.node_ab import NodeAB


@pytest.mark.parametrize(
    "partition,"
    "index,"
    "layer_index,"
    "in_layer_index,"
    "number_of_nodes_in_layer,"
    "index_offset_for_layer",
    [
        (2, 6, 2, 0, 10, 6),
        (2, 7, 2, 1, 10, 6),
        (2, 8, 2, 2, 10, 6),
        (2, 9, 2, 3, 10, 6),
        (2, 10, 2, 4, 10, 6),
        (2, 11, 2, 5, 10, 6),
        (2, 12, 2, 6, 10, 6),
        (2, 13, 2, 7, 10, 6),
        (2, 14, 2, 8, 10, 6),
        (2, 15, 2, 9, 10, 6),
        (3, 16, 3, 0, 15, 16),
        (3, 17, 3, 1, 15, 16),
        (3, 18, 3, 2, 15, 16),
        (3, 19, 3, 3, 15, 16),
        (3, 20, 3, 4, 15, 16),
        (3, 21, 3, 5, 15, 16),
        (3, 22, 3, 6, 15, 16),
        (3, 23, 3, 7, 15, 16),
        (3, 24, 3, 8, 15, 16),
        (3, 25, 3, 9, 15, 16),
        (3, 26, 3, 10, 15, 16),
        (3, 27, 3, 11, 15, 16),
        (3, 28, 3, 12, 15, 16),
        (3, 29, 3, 13, 15, 16),
        (3, 30, 3, 14, 15, 16),
        (4, 31, 4, 0, 20, 31),
        (4, 32, 4, 1, 20, 31),
        (4, 33, 4, 2, 20, 31),
        (4, 34, 4, 3, 20, 31),
        (4, 35, 4, 4, 20, 31),
        (4, 36, 4, 5, 20, 31),
        (4, 37, 4, 6, 20, 31),
        (4, 38, 4, 7, 20, 31),
        (4, 39, 4, 8, 20, 31),
        (4, 40, 4, 9, 20, 31),
        (4, 41, 4, 10, 20, 31),
        (4, 42, 4, 11, 20, 31),
        (4, 43, 4, 12, 20, 31),
        (4, 44, 4, 13, 20, 31),
        (4, 45, 4, 14, 20, 31),
        (4, 46, 4, 15, 20, 31),
        (4, 47, 4, 16, 20, 31),
        (4, 48, 4, 17, 20, 31),
        (4, 49, 4, 18, 20, 31),
        (4, 50, 4, 19, 20, 31),
    ]
)
def test_indices(
    partition,
    index,
    layer_index,
    in_layer_index,
    number_of_nodes_in_layer,
    index_offset_for_layer,
):
    constants = Constants(partition)
    node_ab = NodeAB(index, constants)
    assert node_ab.INDEX == index
    assert node_ab.LAYER_INDEX == layer_index
    assert node_ab.IN_LAYER_INDEX == in_layer_index
    assert node_ab.NUMBER_OF_NODES_IN_LAYER == number_of_nodes_in_layer
    assert node_ab.INDEX_OFFSET_FOR_LAYER == index_offset_for_layer
    assert node_ab.INDEX == node_ab.INDEX_OFFSET_FOR_LAYER + node_ab.IN_LAYER_INDEX
