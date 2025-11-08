import pytest

from axvaglobe.core.schema._node_sp import _NodeSP


@pytest.mark.parametrize("index,layer_index,in_layer_index", ([41, 6, 0],))
def test_creation_of_node_sp_for_partition_two(
    index,
    layer_index,
    in_layer_index,
):
    node_sp = _NodeSP(2, layer_index, in_layer_index)
    assert node_sp.INDEX == index
    assert node_sp.LAYER_INDEX == layer_index
    assert node_sp.IN_LAYER_INDEX == in_layer_index

    node_sp = _NodeSP.create_node_by_index(2, index)
    assert node_sp.INDEX == index
    assert node_sp.LAYER_INDEX == layer_index
    assert node_sp.IN_LAYER_INDEX == in_layer_index


@pytest.mark.parametrize("index,layer_index,in_layer_index", ([91, 9, 0],))
def test_creation_of_node_sp_for_partition_three(
    index,
    layer_index,
    in_layer_index,
):
    node_sp = _NodeSP(3, layer_index, in_layer_index)
    assert node_sp.INDEX == index
    assert node_sp.LAYER_INDEX == layer_index
    assert node_sp.IN_LAYER_INDEX == in_layer_index

    node_sp = _NodeSP.create_node_by_index(3, index)
    assert node_sp.INDEX == index
    assert node_sp.LAYER_INDEX == layer_index
    assert node_sp.IN_LAYER_INDEX == in_layer_index


@pytest.mark.parametrize("index,layer_index,in_layer_index", ([161, 12, 0],))
def test_creation_of_node_sp_for_partition_four(
    index,
    layer_index,
    in_layer_index,
):
    node_sp = _NodeSP(4, layer_index, in_layer_index)
    assert node_sp.INDEX == index
    assert node_sp.LAYER_INDEX == layer_index
    assert node_sp.IN_LAYER_INDEX == in_layer_index

    node_sp = _NodeSP.create_node_by_index(4, index)
    assert node_sp.INDEX == index
    assert node_sp.LAYER_INDEX == layer_index
    assert node_sp.IN_LAYER_INDEX == in_layer_index
