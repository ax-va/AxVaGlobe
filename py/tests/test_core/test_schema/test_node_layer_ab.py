import pytest

from core.schema.schema import Schema
from core.schema.node_layer_ab import _NodeLayerAB


@pytest.mark.parametrize(
    "index,"
    "node_index_offset_for_layer,"
    "number_of_nodes",
    [
        (2, 6, 10),
    ]
)
def test_node_layer_ab_for_schema_two(
        index,
        node_index_offset_for_layer,
        number_of_nodes,
):
    schema = Schema(2)
    node_layer_ab = _NodeLayerAB(index, schema)
    assert node_layer_ab.INDEX == index
    assert node_layer_ab.NODE_INDEX_OFFSET_FOR_LAYER == node_index_offset_for_layer
    assert node_layer_ab.NUMBER_OF_NODES == number_of_nodes


@pytest.mark.parametrize(
    "index,"
    "node_index_offset_for_layer,"
    "number_of_nodes,"
    "end_node_in_layer_index",
    [
        (3, 16, 15, 14),
    ]
)
def test_node_layer_ab_for_schema_three(
        index,
        node_index_offset_for_layer,
        number_of_nodes,
        end_node_in_layer_index,
):
    schema = Schema(3)
    node_layer_ab = _NodeLayerAB(index, schema)
    assert node_layer_ab.INDEX == index
    assert node_layer_ab.NODE_INDEX_OFFSET_FOR_LAYER == node_index_offset_for_layer
    assert node_layer_ab.NUMBER_OF_NODES == number_of_nodes
    assert node_layer_ab.END_NODE_IN_LAYER_INDEX == end_node_in_layer_index


@pytest.mark.parametrize(
    "index,"
    "node_index_offset_for_layer,"
    "number_of_nodes,"
    "end_node_in_layer_index",
    [
        (4, 31, 20, 19),
    ]
)
def test_node_layer_ab_for_schema_four(
        index,
        node_index_offset_for_layer,
        number_of_nodes,
        end_node_in_layer_index,
):
    schema = Schema(4)
    node_layer_ab = _NodeLayerAB(index, schema)
    assert node_layer_ab.INDEX == index
    assert node_layer_ab.NODE_INDEX_OFFSET_FOR_LAYER == node_index_offset_for_layer
    assert node_layer_ab.NUMBER_OF_NODES == number_of_nodes
    assert node_layer_ab.END_NODE_IN_LAYER_INDEX == end_node_in_layer_index
