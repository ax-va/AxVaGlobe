import pytest

from core.schema.schema import Schema
from core.schema.node_layer_bc import _NodeLayerBC


@pytest.mark.parametrize(
    "index,"
    "node_index_offset_for_layer,"
    "number_of_nodes",
    [
        (4, 26, 10),
    ]
)
def test_node_layer_a_for_schema_two(
        index,
        node_index_offset_for_layer,
        number_of_nodes,
):
    schema = Schema(2)
    node_layer_bc = _NodeLayerBC(index, schema)
    assert node_layer_bc.INDEX == index
    assert node_layer_bc.NODE_INDEX_OFFSET_FOR_LAYER == node_index_offset_for_layer
    assert node_layer_bc.NUMBER_OF_NODES == number_of_nodes


@pytest.mark.parametrize(
    "index,"
    "node_index_offset_for_layer,"
    "number_of_nodes",
    [
        (6, 61, 15),
    ]
)
def test_node_layer_a_for_schema_three(
        index,
        node_index_offset_for_layer,
        number_of_nodes,
):
    schema = Schema(3)
    node_layer_bc = _NodeLayerBC(index, schema)
    assert node_layer_bc.INDEX == index
    assert node_layer_bc.NODE_INDEX_OFFSET_FOR_LAYER == node_index_offset_for_layer
    assert node_layer_bc.NUMBER_OF_NODES == number_of_nodes


@pytest.mark.parametrize(
    "index,"
    "node_index_offset_for_layer,"
    "number_of_nodes",
    [
        (8, 111, 20),
    ]
)
def test_node_layer_a_for_schema_four(
        index,
        node_index_offset_for_layer,
        number_of_nodes,
):
    schema = Schema(4)
    node_layer_bc = _NodeLayerBC(index, schema)
    assert node_layer_bc.INDEX == index
    assert node_layer_bc.NODE_INDEX_OFFSET_FOR_LAYER == node_index_offset_for_layer
    assert node_layer_bc.NUMBER_OF_NODES == number_of_nodes
