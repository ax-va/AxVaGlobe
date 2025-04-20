import pytest

from core.schema.schema import Schema
from core.schema.node_layer_b import _NodeLayerB


@pytest.mark.parametrize(
    "index,"
    "node_index_offset_for_layer,"
    "number_of_nodes",
    [
        (3, 16, 10),
    ]
)
def test_node_layer_b_for_schema_two(
        index,
        node_index_offset_for_layer,
        number_of_nodes,
):
    schema = Schema(2)
    node_layer_b = _NodeLayerB(index, schema)
    assert node_layer_b.INDEX == index
    assert node_layer_b.NODE_INDEX_OFFSET_FOR_LAYER == node_index_offset_for_layer
    assert node_layer_b.NUMBER_OF_NODES == number_of_nodes


@pytest.mark.parametrize(
    "index,"
    "node_index_offset_for_layer,"
    "number_of_nodes",
    [
        (4, 31, 15),
        (5, 46, 15),
    ]
)
def test_node_layer_b_for_schema_three(
        index,
        node_index_offset_for_layer,
        number_of_nodes,
):
    schema = Schema(3)
    node_layer_b = _NodeLayerB(index, schema)
    assert node_layer_b.INDEX == index
    assert node_layer_b.NODE_INDEX_OFFSET_FOR_LAYER == node_index_offset_for_layer
    assert node_layer_b.NUMBER_OF_NODES == number_of_nodes


@pytest.mark.parametrize(
    "index,"
    "node_index_offset_for_layer,"
    "number_of_nodes",
    [
        (5, 51, 20),
        (6, 71, 20),
        (7, 91, 20),
    ]
)
def test_node_layer_b_for_schema_four(
        index,
        node_index_offset_for_layer,
        number_of_nodes,
):
    schema = Schema(4)
    node_layer_b = _NodeLayerB(index, schema)
    assert node_layer_b.INDEX == index
    assert node_layer_b.NODE_INDEX_OFFSET_FOR_LAYER == node_index_offset_for_layer
    assert node_layer_b.NUMBER_OF_NODES == number_of_nodes
