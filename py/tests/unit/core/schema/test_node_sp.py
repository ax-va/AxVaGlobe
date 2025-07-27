import pytest

from core.schema.nodes.node_sp import _NodeSP


@pytest.mark.parametrize(
    "index,"
    "layer_index,"
    "in_layer_index",
    (
        [41, 6, 0],
    )
)
def test_creation_of_node_sp_for_schema_two(
        index,
        layer_index,
        in_layer_index,
        schema_two,  # function fixture
):
    node_sp = _NodeSP(layer_index, in_layer_index, schema_two.constants)
    assert node_sp.INDEX == index
    assert node_sp.LAYER_INDEX == layer_index
    assert node_sp.IN_LAYER_INDEX == in_layer_index

    node_sp = _NodeSP.create_node_by_index(index, schema_two.constants)
    assert node_sp.INDEX == index
    assert node_sp.LAYER_INDEX == layer_index
    assert node_sp.IN_LAYER_INDEX == in_layer_index


@pytest.mark.parametrize(
    "index,"
    "layer_index,"
    "in_layer_index",
    (
        [91, 9, 0],
    )
)
def test_creation_of_node_sp_for_schema_three(
        index,
        layer_index,
        in_layer_index,
        schema_three,  # function fixture
):
    node_sp = _NodeSP(layer_index, in_layer_index, schema_three.constants)
    assert node_sp.INDEX == index
    assert node_sp.LAYER_INDEX == layer_index
    assert node_sp.IN_LAYER_INDEX == in_layer_index

    node_sp = _NodeSP.create_node_by_index(index, schema_three.constants)
    assert node_sp.INDEX == index
    assert node_sp.LAYER_INDEX == layer_index
    assert node_sp.IN_LAYER_INDEX == in_layer_index


@pytest.mark.parametrize(
    "index,"
    "layer_index,"
    "in_layer_index",
    (
        [161, 12, 0],
    )
)
def test_creation_of_node_sp_for_schema_four(
        index,
        layer_index,
        in_layer_index,
        schema_four,  # function fixture
):
    node_sp = _NodeSP(layer_index, in_layer_index, schema_four.constants)
    assert node_sp.INDEX == index
    assert node_sp.LAYER_INDEX == layer_index
    assert node_sp.IN_LAYER_INDEX == in_layer_index

    node_sp = _NodeSP.create_node_by_index(index, schema_four.constants)
    assert node_sp.INDEX == index
    assert node_sp.LAYER_INDEX == layer_index
    assert node_sp.IN_LAYER_INDEX == in_layer_index
