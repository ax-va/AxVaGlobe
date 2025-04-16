import pytest

from core.schema.schema import Schema
from core.schema.node_ab import NodeAB


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
        (46, 4, 15),
        (47, 4, 16),
        (48, 4, 17),
        (49, 4, 18),
        (50, 4, 19),
    ]
)
def test_node_ab_creation_for_partition_four(
    index,
    layer_index,
    in_layer_index,
):
    schema = Schema(4)
    node_a_1 = NodeAB(in_layer_index, schema)
    assert node_a_1.LAYER_INDEX == layer_index
    assert node_a_1.IN_LAYER_INDEX == in_layer_index
    assert node_a_1.INDEX == index

    node_a_2 = NodeAB.create_node_by_index(index, schema)
    assert node_a_2.LAYER_INDEX == layer_index
    assert node_a_2.IN_LAYER_INDEX == in_layer_index
    assert node_a_2.INDEX == index
