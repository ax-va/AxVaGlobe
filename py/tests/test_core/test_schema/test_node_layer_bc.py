import pytest

from core.schema.node_layer_bc import _NodeLayerBC


@pytest.mark.parametrize(
    "index,"
    "node_index_offset_for_layer,"
    "number_of_nodes,"
    "end_node_in_layer_index",
    [
        (4, 26, 10, 9),
    ]
)
def test_node_layer_bc_for_schema_two(
        index,
        node_index_offset_for_layer,
        number_of_nodes,
        end_node_in_layer_index,
        schema_two,  # function fixture
):
    node_layer_bc = _NodeLayerBC(index, schema_two)
    assert node_layer_bc.INDEX == index
    assert node_layer_bc.NODE_INDEX_OFFSET_FOR_LAYER == node_index_offset_for_layer
    assert node_layer_bc.NUMBER_OF_NODES == number_of_nodes
    assert node_layer_bc.END_NODE_IN_LAYER_INDEX == end_node_in_layer_index


@pytest.mark.parametrize(
    "index,"
    "node_index_offset_for_layer,"
    "number_of_nodes,"
    "end_node_in_layer_index",
    [
        (6, 61, 15, 14),
    ]
)
def test_node_layer_bc_for_schema_three(
        index,
        node_index_offset_for_layer,
        number_of_nodes,
        end_node_in_layer_index,
        schema_three,  # function fixture
):
    node_layer_bc = _NodeLayerBC(index, schema_three)
    assert node_layer_bc.INDEX == index
    assert node_layer_bc.NODE_INDEX_OFFSET_FOR_LAYER == node_index_offset_for_layer
    assert node_layer_bc.NUMBER_OF_NODES == number_of_nodes
    assert node_layer_bc.END_NODE_IN_LAYER_INDEX == end_node_in_layer_index


@pytest.mark.parametrize(
    "index,"
    "node_index_offset_for_layer,"
    "number_of_nodes,"
    "end_node_in_layer_index",
    [
        (8, 111, 20, 19),
    ]
)
def test_node_layer_bc_for_schema_four(
        index,
        node_index_offset_for_layer,
        number_of_nodes,
        end_node_in_layer_index,
        schema_four,  # function fixture
):
    node_layer_bc = _NodeLayerBC(index, schema_four)
    assert node_layer_bc.INDEX == index
    assert node_layer_bc.NODE_INDEX_OFFSET_FOR_LAYER == node_index_offset_for_layer
    assert node_layer_bc.NUMBER_OF_NODES == number_of_nodes
    assert node_layer_bc.END_NODE_IN_LAYER_INDEX == end_node_in_layer_index
