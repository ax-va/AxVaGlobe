import pytest

from core.schema.schema import Schema
from core.schema.node_np import _NodeNP


@pytest.mark.parametrize(
    "index,"
    "layer_index,"
    "in_layer_index",
    (
        [0, 0, 0],
    )
)
def test_creation_of_node_np_for_schema_two(
        index,
        layer_index,
        in_layer_index,
):
    schema = Schema(2)
    node_np = _NodeNP(layer_index, in_layer_index, schema)
    assert node_np.INDEX == index
    assert node_np.LAYER_INDEX == layer_index
    assert node_np.IN_LAYER_INDEX == in_layer_index

    node_np = _NodeNP.create_node_by_index(index, schema)
    assert node_np.INDEX == index
    assert node_np.LAYER_INDEX == layer_index
    assert node_np.IN_LAYER_INDEX == in_layer_index


@pytest.mark.parametrize(
    "index,"
    "layer_index,"
    "in_layer_index",
    (
        [0, 0, 0],
    )
)
def test_creation_of_node_np_for_schema_three(
        index,
        layer_index,
        in_layer_index,
):
    schema = Schema(3)
    node_np = _NodeNP(layer_index, in_layer_index, schema)
    assert node_np.INDEX == index
    assert node_np.LAYER_INDEX == layer_index
    assert node_np.IN_LAYER_INDEX == in_layer_index

    node_np = _NodeNP.create_node_by_index(index, schema)
    assert node_np.INDEX == index
    assert node_np.LAYER_INDEX == layer_index
    assert node_np.IN_LAYER_INDEX == in_layer_index


@pytest.mark.parametrize(
    "index,"
    "layer_index,"
    "in_layer_index",
    (
        [0, 0, 0],
    )
)
def test_creation_of_node_np_for_schema_four(
        index,
        layer_index,
        in_layer_index,
):
    schema = Schema(4)
    node_np = _NodeNP(layer_index, in_layer_index, schema)
    assert node_np.INDEX == index
    assert node_np.LAYER_INDEX == layer_index
    assert node_np.IN_LAYER_INDEX == in_layer_index

    node_np = _NodeNP.create_node_by_index(index, schema)
    assert node_np.INDEX == index
    assert node_np.LAYER_INDEX == layer_index
    assert node_np.IN_LAYER_INDEX == in_layer_index


@pytest.mark.parametrize(
    "index,"
    "layer_index,"
    "in_layer_index",
    (
        [0, 0, 0],
    )
)
def test_creation_of_node_np_for_schema_five(
        index,
        layer_index,
        in_layer_index,
):
    schema = Schema(5)
    node_np = _NodeNP(layer_index, in_layer_index, schema)
    assert node_np.INDEX == index
    assert node_np.LAYER_INDEX == layer_index
    assert node_np.IN_LAYER_INDEX == in_layer_index

    node_np = _NodeNP.create_node_by_index(index, schema)
    assert node_np.INDEX == index
    assert node_np.LAYER_INDEX == layer_index
    assert node_np.IN_LAYER_INDEX == in_layer_index
