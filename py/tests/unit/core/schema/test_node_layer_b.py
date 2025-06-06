import pytest

from core.schema.node_layer_b import _NodeLayerB


@pytest.mark.parametrize(
    "index,"
    "node_index_offset_for_layer,"
    "number_of_nodes,"
    "end_node_in_layer_index",
    [
        (3, 16, 10, 9),
    ]
)
def test_node_layer_b_for_schema_two(
        index,
        node_index_offset_for_layer,
        number_of_nodes,
        end_node_in_layer_index,
        schema_two,  # function fixture
):
    node_layer_b = _NodeLayerB(index, schema_two)
    assert node_layer_b.INDEX == index
    assert node_layer_b.NODE_INDEX_OFFSET_FOR_LAYER == node_index_offset_for_layer
    assert node_layer_b.NUMBER_OF_NODES == number_of_nodes
    assert node_layer_b.END_NODE_IN_LAYER_INDEX == end_node_in_layer_index


@pytest.mark.parametrize(
    "index,"
    "node_index_offset_for_layer,"
    "number_of_nodes,"
    "end_node_in_layer_index",
    [
        (4, 31, 15, 14),
        (5, 46, 15, 14),
    ]
)
def test_node_layer_b_for_schema_three(
        index,
        node_index_offset_for_layer,
        number_of_nodes,
        end_node_in_layer_index,
        schema_three,  # function fixture
):
    node_layer_b = _NodeLayerB(index, schema_three)
    assert node_layer_b.INDEX == index
    assert node_layer_b.NODE_INDEX_OFFSET_FOR_LAYER == node_index_offset_for_layer
    assert node_layer_b.NUMBER_OF_NODES == number_of_nodes
    assert node_layer_b.END_NODE_IN_LAYER_INDEX == end_node_in_layer_index


@pytest.mark.parametrize(
    "index,"
    "node_index_offset_for_layer,"
    "number_of_nodes,"
    "end_node_in_layer_index",
    [
        (5, 51, 20, 19),
        (6, 71, 20, 19),
        (7, 91, 20, 19),
    ]
)
def test_node_layer_b_for_schema_four(
        index,
        node_index_offset_for_layer,
        number_of_nodes,
        end_node_in_layer_index,
        schema_four,  # function fixture
):
    node_layer_b = _NodeLayerB(index, schema_four)
    assert node_layer_b.INDEX == index
    assert node_layer_b.NODE_INDEX_OFFSET_FOR_LAYER == node_index_offset_for_layer
    assert node_layer_b.NUMBER_OF_NODES == number_of_nodes
    assert node_layer_b.END_NODE_IN_LAYER_INDEX == end_node_in_layer_index
