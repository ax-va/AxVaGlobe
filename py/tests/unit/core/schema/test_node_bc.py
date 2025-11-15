import pytest

from axvaglobe.core.schema._node_bc import _NodeBC
from axvaglobe.core.schema.partition import Partition


@pytest.mark.parametrize(
    "index,layer_index,in_layer_index",
    [
        (26, 4, 0),
        (27, 4, 1),
        (28, 4, 2),
        (29, 4, 3),
        (30, 4, 4),
        (31, 4, 5),
        (32, 4, 6),
        (33, 4, 7),
        (34, 4, 8),
        (35, 4, 9),
    ],
)
def test_creation_of_node_bc_for_partition_two(
    index,
    layer_index,
    in_layer_index,
):
    partition_obj = Partition(2)
    node_bc = _NodeBC(layer_index, in_layer_index, partition_obj)
    assert node_bc.INDEX == index
    assert node_bc.LAYER_INDEX == layer_index
    assert node_bc.IN_LAYER_INDEX == in_layer_index

    node_bc = _NodeBC.create_node(index, partition_obj)
    assert node_bc.INDEX == index
    assert node_bc.LAYER_INDEX == layer_index
    assert node_bc.IN_LAYER_INDEX == in_layer_index


@pytest.mark.parametrize(
    "index,layer_index,in_layer_index",
    [
        (61, 6, 0),
        (62, 6, 1),
        (63, 6, 2),
        (64, 6, 3),
        (65, 6, 4),
        (66, 6, 5),
        (67, 6, 6),
        (68, 6, 7),
        (69, 6, 8),
        (70, 6, 9),
        (71, 6, 10),
        (72, 6, 11),
        (73, 6, 12),
        (74, 6, 13),
        (75, 6, 14),
    ],
)
def test_creation_of_node_bc_for_partition_three(
    index,
    layer_index,
    in_layer_index,
):
    partition_obj = Partition(3)
    node_bc = _NodeBC(layer_index, in_layer_index, partition_obj)
    assert node_bc.INDEX == index
    assert node_bc.LAYER_INDEX == layer_index
    assert node_bc.IN_LAYER_INDEX == in_layer_index

    node_bc = _NodeBC.create_node(index, partition_obj)
    assert node_bc.INDEX == index
    assert node_bc.LAYER_INDEX == layer_index
    assert node_bc.IN_LAYER_INDEX == in_layer_index


@pytest.mark.parametrize(
    "index,layer_index,in_layer_index",
    [
        (111, 8, 0),
        (112, 8, 1),
        (113, 8, 2),
        (114, 8, 3),
        (115, 8, 4),
        (116, 8, 5),
        (117, 8, 6),
        (118, 8, 7),
        (119, 8, 8),
        (120, 8, 9),
        (121, 8, 10),
        (122, 8, 11),
        (123, 8, 12),
        (124, 8, 13),
        (125, 8, 14),
        (126, 8, 15),
        (127, 8, 16),
        (128, 8, 17),
        (129, 8, 18),
        (130, 8, 19),
    ],
)
def test_creation_of_node_bc_for_partition_four(
    index,
    layer_index,
    in_layer_index,
):
    partition_obj = Partition(4)
    node_bc = _NodeBC(layer_index, in_layer_index, partition_obj)
    assert node_bc.INDEX == index
    assert node_bc.LAYER_INDEX == layer_index
    assert node_bc.IN_LAYER_INDEX == in_layer_index

    node_bc = _NodeBC.create_node(index, partition_obj)
    assert node_bc.INDEX == index
    assert node_bc.LAYER_INDEX == layer_index
    assert node_bc.IN_LAYER_INDEX == in_layer_index
