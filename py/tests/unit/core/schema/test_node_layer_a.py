import pytest

from axvaglobe.core.schema.node_layers.node_layer_a import _NodeLayerA


@pytest.mark.parametrize(
    "index,node_index_offset_for_layer,number_of_nodes,end_node_in_layer_index",
    [
        (1, 1, 5, 4),
    ],
)
def test_node_layer_a_for_schema_two(
    index,
    node_index_offset_for_layer,
    number_of_nodes,
    end_node_in_layer_index,
    schema_two,  # function fixture
):
    node_layer_a = _NodeLayerA(index, schema_two.constants)
    assert node_layer_a.INDEX == index
    assert node_layer_a.NODE_INDEX_OFFSET_FOR_LAYER == node_index_offset_for_layer
    assert node_layer_a.NUMBER_OF_NODES == number_of_nodes
    assert node_layer_a.END_NODE_IN_LAYER_INDEX == end_node_in_layer_index


@pytest.mark.parametrize(
    "index,node_index_offset_for_layer,number_of_nodes,end_node_in_layer_index",
    [
        (1, 1, 5, 4),
        (2, 6, 10, 9),
    ],
)
def test_node_layer_a_for_schema_three(
    index,
    node_index_offset_for_layer,
    number_of_nodes,
    end_node_in_layer_index,
    schema_three,  # function fixture
):
    node_layer_a = _NodeLayerA(index, schema_three.constants)
    assert node_layer_a.INDEX == index
    assert node_layer_a.NODE_INDEX_OFFSET_FOR_LAYER == node_index_offset_for_layer
    assert node_layer_a.NUMBER_OF_NODES == number_of_nodes
    assert node_layer_a.END_NODE_IN_LAYER_INDEX == end_node_in_layer_index


@pytest.mark.parametrize(
    "index,node_index_offset_for_layer,number_of_nodes,end_node_in_layer_index",
    [
        (1, 1, 5, 4),
        (2, 6, 10, 9),
        (3, 16, 15, 14),
    ],
)
def test_node_layer_a_for_schema_four(
    index,
    node_index_offset_for_layer,
    number_of_nodes,
    end_node_in_layer_index,
    schema_four,  # function fixture
):
    node_layer_a = _NodeLayerA(index, schema_four.constants)
    assert node_layer_a.INDEX == index
    assert node_layer_a.NODE_INDEX_OFFSET_FOR_LAYER == node_index_offset_for_layer
    assert node_layer_a.NUMBER_OF_NODES == number_of_nodes
    assert node_layer_a.END_NODE_IN_LAYER_INDEX == end_node_in_layer_index


@pytest.mark.parametrize(
    "index,node_index_offset_for_layer,number_of_nodes,end_node_in_layer_index",
    [
        (1, 1, 5, 4),
        (2, 6, 10, 9),
        (3, 16, 15, 14),
        (4, 31, 20, 19),
    ],
)
def test_node_layer_a_for_schema_five(
    index,
    node_index_offset_for_layer,
    number_of_nodes,
    end_node_in_layer_index,
    schema_five,  # function fixture
):
    node_layer_a = _NodeLayerA(index, schema_five.constants)
    assert node_layer_a.INDEX == index
    assert node_layer_a.NODE_INDEX_OFFSET_FOR_LAYER == node_index_offset_for_layer
    assert node_layer_a.NUMBER_OF_NODES == number_of_nodes
    assert node_layer_a.END_NODE_IN_LAYER_INDEX == end_node_in_layer_index
