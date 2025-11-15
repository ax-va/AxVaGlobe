import pytest

from axvaglobe.core.schema._node_sp import _NodeSP
from axvaglobe.core.schema.partition import Partition


@pytest.mark.parametrize("index,layer_index,in_layer_index", ([41, 6, 0],))
def test_creation_of_node_sp_for_partition_two(
    index,
    layer_index,
    in_layer_index,
):
    partition_obj = Partition(2)
    node_sp = _NodeSP(layer_index, in_layer_index, partition_obj)
    assert node_sp.INDEX == index
    assert node_sp.LAYER_INDEX == layer_index
    assert node_sp.IN_LAYER_INDEX == in_layer_index

    node_sp = _NodeSP.create_node_sp(partition_obj)
    assert node_sp.INDEX == index
    assert node_sp.LAYER_INDEX == layer_index
    assert node_sp.IN_LAYER_INDEX == in_layer_index


@pytest.mark.parametrize("index,layer_index,in_layer_index", ([91, 9, 0],))
def test_creation_of_node_sp_for_partition_three(
    index,
    layer_index,
    in_layer_index,
):
    partition_obj = Partition(3)
    node_sp = _NodeSP(layer_index, in_layer_index, partition_obj)
    assert node_sp.INDEX == index
    assert node_sp.LAYER_INDEX == layer_index
    assert node_sp.IN_LAYER_INDEX == in_layer_index

    node_sp = _NodeSP.create_node_sp(partition_obj)
    assert node_sp.INDEX == index
    assert node_sp.LAYER_INDEX == layer_index
    assert node_sp.IN_LAYER_INDEX == in_layer_index


@pytest.mark.parametrize("index,layer_index,in_layer_index", ([161, 12, 0],))
def test_creation_of_node_sp_for_partition_four(
    index,
    layer_index,
    in_layer_index,
):
    partition_obj = Partition(4)
    node_sp = _NodeSP(layer_index, in_layer_index, partition_obj)
    assert node_sp.INDEX == index
    assert node_sp.LAYER_INDEX == layer_index
    assert node_sp.IN_LAYER_INDEX == in_layer_index

    node_sp = _NodeSP.create_node_sp(partition_obj)
    assert node_sp.INDEX == index
    assert node_sp.LAYER_INDEX == layer_index
    assert node_sp.IN_LAYER_INDEX == in_layer_index
