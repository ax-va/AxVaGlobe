import pytest

from core.schema.nodes.node_np import _NodeNP


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
        schema_two,  # function fixture
):
    node_np = _NodeNP(layer_index, in_layer_index, schema_two.constants)
    assert node_np.INDEX == index
    assert node_np.LAYER_INDEX == layer_index
    assert node_np.IN_LAYER_INDEX == in_layer_index

    node_np = _NodeNP.create_node_by_index(index, schema_two.constants)
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
        schema_three,  # function fixture
):
    node_np = _NodeNP(layer_index, in_layer_index, schema_three.constants)
    assert node_np.INDEX == index
    assert node_np.LAYER_INDEX == layer_index
    assert node_np.IN_LAYER_INDEX == in_layer_index

    node_np = _NodeNP.create_node_by_index(index, schema_three.constants)
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
        schema_four,  # function fixture
):
    node_np = _NodeNP(layer_index, in_layer_index, schema_four.constants)
    assert node_np.INDEX == index
    assert node_np.LAYER_INDEX == layer_index
    assert node_np.IN_LAYER_INDEX == in_layer_index

    node_np = _NodeNP.create_node_by_index(index, schema_four.constants)
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
        schema_five,  # function fixture
):
    node_np = _NodeNP(layer_index, in_layer_index, schema_five.constants)
    assert node_np.INDEX == index
    assert node_np.LAYER_INDEX == layer_index
    assert node_np.IN_LAYER_INDEX == in_layer_index

    node_np = _NodeNP.create_node_by_index(index, schema_five.constants)
    assert node_np.INDEX == index
    assert node_np.LAYER_INDEX == layer_index
    assert node_np.IN_LAYER_INDEX == in_layer_index
