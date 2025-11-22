import pytest

from axvaglobe.core.schema._node_layer_c import _NodeLayerC
from axvaglobe.core.schema.partition import Partition


@pytest.mark.parametrize(
    "index,node_index_offset_for_layer,number_of_nodes,last_in_layer_index",
    [
        (5, 36, 5, 4),
    ],
)
def test_node_layer_c_for_partition_two(
    index,
    node_index_offset_for_layer,
    number_of_nodes,
    last_in_layer_index,
):
    partition_obj = Partition(2)
    node_layer_c = _NodeLayerC(index, partition_obj)
    assert node_layer_c.INDEX == index
    assert node_layer_c.NODE_INDEX_OFFSET_FOR_LAYER == node_index_offset_for_layer
    assert node_layer_c.NUMBER_OF_NODES == number_of_nodes
    assert node_layer_c.LAST_IN_LAYER_INDEX == last_in_layer_index


@pytest.mark.parametrize(
    "index,node_index_offset_for_layer,number_of_nodes,last_in_layer_index",
    [
        (7, 76, 10, 9),
        (8, 86, 5, 4),
    ],
)
def test_node_layer_c_for_partition_three(
    index,
    node_index_offset_for_layer,
    number_of_nodes,
    last_in_layer_index,
):
    partition_obj = Partition(3)
    node_layer_c = _NodeLayerC(index, partition_obj)
    assert node_layer_c.INDEX == index
    assert node_layer_c.NODE_INDEX_OFFSET_FOR_LAYER == node_index_offset_for_layer
    assert node_layer_c.NUMBER_OF_NODES == number_of_nodes
    assert node_layer_c.LAST_IN_LAYER_INDEX == last_in_layer_index


@pytest.mark.parametrize(
    "index,node_index_offset_for_layer,number_of_nodes,last_in_layer_index",
    [
        (9, 131, 15, 14),
        (10, 146, 10, 9),
        (11, 156, 5, 4),
    ],
)
def test_node_layer_c_for_partition_four(
    index,
    node_index_offset_for_layer,
    number_of_nodes,
    last_in_layer_index,
):
    partition_obj = Partition(4)
    node_layer_c = _NodeLayerC(index, partition_obj)
    assert node_layer_c.INDEX == index
    assert node_layer_c.NODE_INDEX_OFFSET_FOR_LAYER == node_index_offset_for_layer
    assert node_layer_c.NUMBER_OF_NODES == number_of_nodes
    assert node_layer_c.LAST_IN_LAYER_INDEX == last_in_layer_index
