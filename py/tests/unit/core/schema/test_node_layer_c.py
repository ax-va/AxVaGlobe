import pytest

from axvaglobe.core.schema.node_layers._node_layer_c import _NodeLayerC


@pytest.mark.parametrize(
    "index,node_index_offset_for_layer,number_of_nodes,end_node_in_layer_index",
    [
        (5, 36, 5, 4),
    ],
)
def test_node_layer_c_for_schema_two(
    index,
    node_index_offset_for_layer,
    number_of_nodes,
    end_node_in_layer_index,
    schema_two,  # function fixture
):
    node_layer_c = _NodeLayerC(index, schema_two.constants)
    assert node_layer_c.INDEX == index
    assert node_layer_c.NODE_INDEX_OFFSET_FOR_LAYER == node_index_offset_for_layer
    assert node_layer_c.NUMBER_OF_NODES == number_of_nodes
    assert node_layer_c.END_NODE_IN_LAYER_INDEX == end_node_in_layer_index


@pytest.mark.parametrize(
    "index,node_index_offset_for_layer,number_of_nodes,end_node_in_layer_index",
    [
        (7, 76, 10, 9),
        (8, 86, 5, 4),
    ],
)
def test_node_layer_c_for_schema_three(
    index,
    node_index_offset_for_layer,
    number_of_nodes,
    end_node_in_layer_index,
    schema_three,  # function fixture
):
    node_layer_c = _NodeLayerC(index, schema_three.constants)
    assert node_layer_c.INDEX == index
    assert node_layer_c.NODE_INDEX_OFFSET_FOR_LAYER == node_index_offset_for_layer
    assert node_layer_c.NUMBER_OF_NODES == number_of_nodes
    assert node_layer_c.END_NODE_IN_LAYER_INDEX == end_node_in_layer_index


@pytest.mark.parametrize(
    "index,node_index_offset_for_layer,number_of_nodes,end_node_in_layer_index",
    [
        (9, 131, 15, 14),
        (10, 146, 10, 9),
        (11, 156, 5, 4),
    ],
)
def test_node_layer_c_for_schema_four(
    index,
    node_index_offset_for_layer,
    number_of_nodes,
    end_node_in_layer_index,
    schema_four,  # function fixture
):
    node_layer_c = _NodeLayerC(index, schema_four.constants)
    assert node_layer_c.INDEX == index
    assert node_layer_c.NODE_INDEX_OFFSET_FOR_LAYER == node_index_offset_for_layer
    assert node_layer_c.NUMBER_OF_NODES == number_of_nodes
    assert node_layer_c.END_NODE_IN_LAYER_INDEX == end_node_in_layer_index
