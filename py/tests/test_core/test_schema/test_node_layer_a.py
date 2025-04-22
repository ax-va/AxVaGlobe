import pytest

from core.schema.schema import Schema
from core.schema.node_layer_a import _NodeLayerA


@pytest.mark.parametrize(
    "index,"
    "node_index_offset_for_layer,"
    "number_of_nodes,"
    "end_node_in_layer_index",
    [
        (1, 1, 5, 4),
    ]
)
def test_node_layer_a_for_schema_two(
        index,
        node_index_offset_for_layer,
        number_of_nodes,
        end_node_in_layer_index,
):
    schema = Schema(2)
    node_layer_a = _NodeLayerA(index, schema)
    assert node_layer_a.INDEX == index
    assert node_layer_a.NODE_INDEX_OFFSET_FOR_LAYER == node_index_offset_for_layer
    assert node_layer_a.NUMBER_OF_NODES == number_of_nodes
    assert node_layer_a.END_NODE_IN_LAYER_INDEX == end_node_in_layer_index


@pytest.mark.parametrize(
    "index,"
    "node_index_offset_for_layer,"
    "number_of_nodes,"
    "end_node_in_layer_index",
    [
        (1, 1, 5, 4),
        (2, 6, 10, 9),
    ]
)
def test_node_layer_a_for_schema_three(
        index,
        node_index_offset_for_layer,
        number_of_nodes,
        end_node_in_layer_index
):
    schema = Schema(3)
    node_layer_a = _NodeLayerA(index, schema)
    assert node_layer_a.INDEX == index
    assert node_layer_a.NODE_INDEX_OFFSET_FOR_LAYER == node_index_offset_for_layer
    assert node_layer_a.NUMBER_OF_NODES == number_of_nodes
    assert node_layer_a.END_NODE_IN_LAYER_INDEX == end_node_in_layer_index


@pytest.mark.parametrize(
    "index,"
    "node_index_offset_for_layer,"
    "number_of_nodes,"
    "end_node_in_layer_index",
    [
        (1, 1, 5, 4),
        (2, 6, 10, 9),
        (3, 16, 15, 14),
    ]
)
def test_node_layer_a_for_schema_four(
        index,
        node_index_offset_for_layer,
        number_of_nodes,
        end_node_in_layer_index,
):
    schema = Schema(4)
    node_layer_a = _NodeLayerA(index, schema)
    assert node_layer_a.INDEX == index
    assert node_layer_a.NODE_INDEX_OFFSET_FOR_LAYER == node_index_offset_for_layer
    assert node_layer_a.NUMBER_OF_NODES == number_of_nodes
    assert node_layer_a.END_NODE_IN_LAYER_INDEX == end_node_in_layer_index


@pytest.mark.parametrize(
    "index,"
    "node_index_offset_for_layer,"
    "number_of_nodes,"
    "end_node_in_layer_index",
    [
        (1, 1, 5, 4),
        (2, 6, 10, 9),
        (3, 16, 15, 14),
        (4, 31, 20, 19),
    ]
)
def test_node_layer_a_for_schema_five(
        index,
        node_index_offset_for_layer,
        number_of_nodes,
        end_node_in_layer_index,
):
    schema = Schema(5)
    node_layer_a = _NodeLayerA(index, schema)
    assert node_layer_a.INDEX == index
    assert node_layer_a.NODE_INDEX_OFFSET_FOR_LAYER == node_index_offset_for_layer
    assert node_layer_a.NUMBER_OF_NODES == number_of_nodes
    assert node_layer_a.END_NODE_IN_LAYER_INDEX == end_node_in_layer_index
