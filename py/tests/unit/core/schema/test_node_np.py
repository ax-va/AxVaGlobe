import pytest

from axvaglobe.core.schema.nodes._node_np import _NodeNP


@pytest.mark.parametrize("index,layer_index,in_layer_index", ([0, 0, 0],))
def test_creation_of_node_np_for_partition_two(
    index,
    layer_index,
    in_layer_index,
):
    node_np = _NodeNP(2, layer_index, in_layer_index)
    assert node_np.INDEX == index
    assert node_np.LAYER_INDEX == layer_index
    assert node_np.IN_LAYER_INDEX == in_layer_index

    node_np = _NodeNP.create_node_by_index(2, index)
    assert node_np.INDEX == index
    assert node_np.LAYER_INDEX == layer_index
    assert node_np.IN_LAYER_INDEX == in_layer_index


@pytest.mark.parametrize("index,layer_index,in_layer_index", ([0, 0, 0],))
def test_creation_of_node_np_for_partition_three(
    index,
    layer_index,
    in_layer_index,
):
    node_np = _NodeNP(3, layer_index, in_layer_index)
    assert node_np.INDEX == index
    assert node_np.LAYER_INDEX == layer_index
    assert node_np.IN_LAYER_INDEX == in_layer_index

    node_np = _NodeNP.create_node_by_index(3, index)
    assert node_np.INDEX == index
    assert node_np.LAYER_INDEX == layer_index
    assert node_np.IN_LAYER_INDEX == in_layer_index


@pytest.mark.parametrize("index,layer_index,in_layer_index", ([0, 0, 0],))
def test_creation_of_node_np_for_partition_four(
    index,
    layer_index,
    in_layer_index,
):
    node_np = _NodeNP(4, layer_index, in_layer_index)
    assert node_np.INDEX == index
    assert node_np.LAYER_INDEX == layer_index
    assert node_np.IN_LAYER_INDEX == in_layer_index

    node_np = _NodeNP.create_node_by_index(4, index)
    assert node_np.INDEX == index
    assert node_np.LAYER_INDEX == layer_index
    assert node_np.IN_LAYER_INDEX == in_layer_index


@pytest.mark.parametrize("index,layer_index,in_layer_index", ([0, 0, 0],))
def test_creation_of_node_np_for_partition_five(
    index,
    layer_index,
    in_layer_index,
):
    node_np = _NodeNP(5, layer_index, in_layer_index)
    assert node_np.INDEX == index
    assert node_np.LAYER_INDEX == layer_index
    assert node_np.IN_LAYER_INDEX == in_layer_index

    node_np = _NodeNP.create_node_by_index(5, index)
    assert node_np.INDEX == index
    assert node_np.LAYER_INDEX == layer_index
    assert node_np.IN_LAYER_INDEX == in_layer_index
