import pytest

from axvaglobe.core.schema._node_layer_b import _NodeLayerB
from axvaglobe.core.schema.partition import Partition


@pytest.mark.parametrize(
    "index,node_index_offset,number_of_nodes,last_in_layer_index",
    [
        (3, 16, 10, 9),
    ],
)
def test_node_layer_b_for_partition_two(
    index,
    node_index_offset,
    number_of_nodes,
    last_in_layer_index,
):
    partition_obj = Partition(2)
    node_layer_b = _NodeLayerB(index, partition_obj)
    assert node_layer_b.INDEX == index
    assert node_layer_b.NODE_INDEX_OFFSET == node_index_offset
    assert node_layer_b.NUMBER_OF_NODES == number_of_nodes
    assert node_layer_b.LAST_IN_LAYER_INDEX == last_in_layer_index


@pytest.mark.parametrize(
    "index,node_index_offset,number_of_nodes,last_in_layer_index",
    [
        (4, 31, 15, 14),
        (5, 46, 15, 14),
    ],
)
def test_node_layer_b_for_partition_three(
    index,
    node_index_offset,
    number_of_nodes,
    last_in_layer_index,
):
    partition_obj = Partition(3)
    node_layer_b = _NodeLayerB(index, partition_obj)
    assert node_layer_b.INDEX == index
    assert node_layer_b.NODE_INDEX_OFFSET == node_index_offset
    assert node_layer_b.NUMBER_OF_NODES == number_of_nodes
    assert node_layer_b.LAST_IN_LAYER_INDEX == last_in_layer_index


@pytest.mark.parametrize(
    "index,node_index_offset,number_of_nodes,last_in_layer_index",
    [
        (5, 51, 20, 19),
        (6, 71, 20, 19),
        (7, 91, 20, 19),
    ],
)
def test_node_layer_b_for_partition_four(
    index,
    node_index_offset,
    number_of_nodes,
    last_in_layer_index,
):
    partition_obj = Partition(4)
    node_layer_b = _NodeLayerB(index, partition_obj)
    assert node_layer_b.INDEX == index
    assert node_layer_b.NODE_INDEX_OFFSET == node_index_offset
    assert node_layer_b.NUMBER_OF_NODES == number_of_nodes
    assert node_layer_b.LAST_IN_LAYER_INDEX == last_in_layer_index
