import pytest

from axvaglobe.core.schema._node_layer_a import _NodeLayerA
from axvaglobe.core.schema.partition import Partition


@pytest.mark.parametrize(
    "index,node_index_offset,number_of_nodes,last_in_layer_index",
    [
        (1, 1, 5, 4),
    ],
)
def test_node_layer_a_for_partition_two(
    index,
    node_index_offset,
    number_of_nodes,
    last_in_layer_index,
):
    partition_obj = Partition(2)
    node_layer_a = _NodeLayerA(index, partition_obj)
    assert node_layer_a.INDEX == index
    assert node_layer_a.NODE_INDEX_OFFSET == node_index_offset
    assert node_layer_a.NUMBER_OF_NODES == number_of_nodes
    assert node_layer_a.LAST_IN_LAYER_INDEX == last_in_layer_index


@pytest.mark.parametrize(
    "index,node_index_offset,number_of_nodes,last_in_layer_index",
    [
        (1, 1, 5, 4),
        (2, 6, 10, 9),
    ],
)
def test_node_layer_a_for_partition_three(
    index,
    node_index_offset,
    number_of_nodes,
    last_in_layer_index,
):
    partition_obj = Partition(3)
    node_layer_a = _NodeLayerA(index, partition_obj)
    assert node_layer_a.INDEX == index
    assert node_layer_a.NODE_INDEX_OFFSET == node_index_offset
    assert node_layer_a.NUMBER_OF_NODES == number_of_nodes
    assert node_layer_a.LAST_IN_LAYER_INDEX == last_in_layer_index


@pytest.mark.parametrize(
    "index,node_index_offset,number_of_nodes,last_in_layer_index",
    [
        (1, 1, 5, 4),
        (2, 6, 10, 9),
        (3, 16, 15, 14),
    ],
)
def test_node_layer_a_for_partition_four(
    index,
    node_index_offset,
    number_of_nodes,
    last_in_layer_index,
):
    partition_obj = Partition(4)
    node_layer_a = _NodeLayerA(index, partition_obj)
    assert node_layer_a.INDEX == index
    assert node_layer_a.NODE_INDEX_OFFSET == node_index_offset
    assert node_layer_a.NUMBER_OF_NODES == number_of_nodes
    assert node_layer_a.LAST_IN_LAYER_INDEX == last_in_layer_index


@pytest.mark.parametrize(
    "index,node_index_offset,number_of_nodes,last_in_layer_index",
    [
        (1, 1, 5, 4),
        (2, 6, 10, 9),
        (3, 16, 15, 14),
        (4, 31, 20, 19),
    ],
)
def test_node_layer_a_for_partition_five(
    index,
    node_index_offset,
    number_of_nodes,
    last_in_layer_index,
):
    partition_obj = Partition(5)
    node_layer_a = _NodeLayerA(index, partition_obj)
    assert node_layer_a.INDEX == index
    assert node_layer_a.NODE_INDEX_OFFSET == node_index_offset
    assert node_layer_a.NUMBER_OF_NODES == number_of_nodes
    assert node_layer_a.LAST_IN_LAYER_INDEX == last_in_layer_index
