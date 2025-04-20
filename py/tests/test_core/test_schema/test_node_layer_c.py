import pytest

from core.schema.schema import Schema
from core.schema.node_layer_c import _NodeLayerC


@pytest.mark.parametrize(
    "index,"
    "node_index_offset_for_layer,"
    "number_of_nodes",
    [
        (5, 36, 5),
    ]
)
def test_node_layer_a_for_schema_two(
        index,
        node_index_offset_for_layer,
        number_of_nodes,
):
    schema = Schema(2)
    node_layer_c = _NodeLayerC(index, schema)
    assert node_layer_c.INDEX == index
    assert node_layer_c.NODE_INDEX_OFFSET_FOR_LAYER == node_index_offset_for_layer
    assert node_layer_c.NUMBER_OF_NODES == number_of_nodes


@pytest.mark.parametrize(
    "index,"
    "node_index_offset_for_layer,"
    "number_of_nodes",
    [
        (7, 76, 10),
        (8, 86, 5),
    ]
)
def test_node_layer_a_for_schema_three(
        index,
        node_index_offset_for_layer,
        number_of_nodes,
):
    schema = Schema(3)
    node_layer_c = _NodeLayerC(index, schema)
    assert node_layer_c.INDEX == index
    assert node_layer_c.NODE_INDEX_OFFSET_FOR_LAYER == node_index_offset_for_layer
    assert node_layer_c.NUMBER_OF_NODES == number_of_nodes


@pytest.mark.parametrize(
    "index,"
    "node_index_offset_for_layer,"
    "number_of_nodes",
    [
        (9, 131, 15),
        (10, 146, 10),
        (11, 156, 5),
    ]
)
def test_node_layer_a_for_schema_four(
        index,
        node_index_offset_for_layer,
        number_of_nodes,
):
    schema = Schema(4)
    node_layer_c = _NodeLayerC(index, schema)
    assert node_layer_c.INDEX == index
    assert node_layer_c.NODE_INDEX_OFFSET_FOR_LAYER == node_index_offset_for_layer
    assert node_layer_c.NUMBER_OF_NODES == number_of_nodes
