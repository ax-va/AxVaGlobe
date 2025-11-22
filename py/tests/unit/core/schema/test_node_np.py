import pytest

from axvaglobe.core.schema._node_np import _NodeNP
from axvaglobe.core.schema.partition import Partition


@pytest.mark.parametrize("index,layer_index,in_layer_index", ([0, 0, 0],))
def test_creating_node_np_for_partition_two(
    index,
    layer_index,
    in_layer_index,
):
    partition_obj = Partition(2)
    node_np = _NodeNP(layer_index, in_layer_index, partition_obj)
    assert node_np.INDEX == index
    assert node_np.LAYER_INDEX == layer_index
    assert node_np.IN_LAYER_INDEX == in_layer_index

    node_np = _NodeNP.create_node(partition_obj)
    assert node_np.INDEX == index
    assert node_np.LAYER_INDEX == layer_index
    assert node_np.IN_LAYER_INDEX == in_layer_index


@pytest.mark.parametrize("index,layer_index,in_layer_index", ([0, 0, 0],))
def test_creating_node_np_for_partition_three(
    index,
    layer_index,
    in_layer_index,
):
    partition_obj = Partition(3)
    node_np = _NodeNP(layer_index, in_layer_index, partition_obj)
    assert node_np.INDEX == index
    assert node_np.LAYER_INDEX == layer_index
    assert node_np.IN_LAYER_INDEX == in_layer_index

    node_np = _NodeNP.create_node(partition_obj)
    assert node_np.INDEX == index
    assert node_np.LAYER_INDEX == layer_index
    assert node_np.IN_LAYER_INDEX == in_layer_index


@pytest.mark.parametrize("index,layer_index,in_layer_index", ([0, 0, 0],))
def test_creating_node_np_for_partition_four(
    index,
    layer_index,
    in_layer_index,
):
    partition_obj = Partition(4)
    node_np = _NodeNP(layer_index, in_layer_index, partition_obj)
    assert node_np.INDEX == index
    assert node_np.LAYER_INDEX == layer_index
    assert node_np.IN_LAYER_INDEX == in_layer_index

    node_np = _NodeNP.create_node(partition_obj)
    assert node_np.INDEX == index
    assert node_np.LAYER_INDEX == layer_index
    assert node_np.IN_LAYER_INDEX == in_layer_index


@pytest.mark.parametrize("index,layer_index,in_layer_index", ([0, 0, 0],))
def test_creating_node_np_for_partition_five(
    index,
    layer_index,
    in_layer_index,
):
    partition_obj = Partition(5)
    node_np = _NodeNP(layer_index, in_layer_index, partition_obj)
    assert node_np.INDEX == index
    assert node_np.LAYER_INDEX == layer_index
    assert node_np.IN_LAYER_INDEX == in_layer_index

    node_np = _NodeNP.create_node(partition_obj)
    assert node_np.INDEX == index
    assert node_np.LAYER_INDEX == layer_index
    assert node_np.IN_LAYER_INDEX == in_layer_index
