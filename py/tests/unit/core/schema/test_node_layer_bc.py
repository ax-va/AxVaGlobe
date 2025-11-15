import pytest

from axvaglobe.core.schema._node_layer_bc import _NodeLayerBC
from axvaglobe.core.schema.partition import Partition


@pytest.mark.parametrize(
    "index,node_index_offset_for_layer,number_of_nodes,end_node_in_layer_index",
    [
        (4, 26, 10, 9),
    ],
)
def test_node_layer_bc_for_partition_two(
    index,
    node_index_offset_for_layer,
    number_of_nodes,
    end_node_in_layer_index,
):
    partition_obj = Partition(2)
    node_layer_bc = _NodeLayerBC(index, partition_obj)
    assert node_layer_bc.INDEX == index
    assert node_layer_bc.NODE_INDEX_OFFSET_FOR_LAYER == node_index_offset_for_layer
    assert node_layer_bc.NUMBER_OF_NODES == number_of_nodes
    assert node_layer_bc.END_NODE_IN_LAYER_INDEX == end_node_in_layer_index


@pytest.mark.parametrize(
    "index,node_index_offset_for_layer,number_of_nodes,end_node_in_layer_index",
    [
        (6, 61, 15, 14),
    ],
)
def test_node_layer_bc_for_partition_three(
    index,
    node_index_offset_for_layer,
    number_of_nodes,
    end_node_in_layer_index,
):
    partition_obj = Partition(3)
    node_layer_bc = _NodeLayerBC(index, partition_obj)
    assert node_layer_bc.INDEX == index
    assert node_layer_bc.NODE_INDEX_OFFSET_FOR_LAYER == node_index_offset_for_layer
    assert node_layer_bc.NUMBER_OF_NODES == number_of_nodes
    assert node_layer_bc.END_NODE_IN_LAYER_INDEX == end_node_in_layer_index


@pytest.mark.parametrize(
    "index,node_index_offset_for_layer,number_of_nodes,end_node_in_layer_index",
    [
        (8, 111, 20, 19),
    ],
)
def test_node_layer_bc_for_partition_four(
    index,
    node_index_offset_for_layer,
    number_of_nodes,
    end_node_in_layer_index,
):
    partition_obj = Partition(4)
    node_layer_bc = _NodeLayerBC(index, partition_obj)
    assert node_layer_bc.INDEX == index
    assert node_layer_bc.NODE_INDEX_OFFSET_FOR_LAYER == node_index_offset_for_layer
    assert node_layer_bc.NUMBER_OF_NODES == number_of_nodes
    assert node_layer_bc.END_NODE_IN_LAYER_INDEX == end_node_in_layer_index
