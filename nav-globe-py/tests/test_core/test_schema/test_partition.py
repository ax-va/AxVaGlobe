import pytest

from core.schema.partition import Partition


@pytest.mark.parametrize(
    "partition,"
    "number_of_nodes,"
    "number_of_triangles,"
    "number_of_node_layers,"
    "number_of_triangle_layers,"
    "number_of_node_edges",
    [
        (2, 42, 80, 7, 6, 3),  # partition: 2
        (3, 92, 180, 10, 9, 4),  # partition: 3
        (4, 162, 320, 13, 12, 5),  # partition: 4
    ],
)
def test_common_constants(
        partition,
        # common constants
        number_of_nodes,
        number_of_triangles,
        number_of_node_layers,
        number_of_triangle_layers,
        number_of_node_edges,
):
    prt = Partition(partition)
    # Check common constants
    assert prt.NUMBER_OF_NODES == number_of_nodes
    assert prt.NUMBER_OF_TRIANGLES == number_of_triangles
    assert prt.NUMBER_OF_NODE_LAYERS == number_of_node_layers
    assert prt.NUMBER_OF_TRIANGLE_LAYERS == number_of_triangle_layers
    assert prt.NUMBER_OF_EDGE_NODES == number_of_node_edges


@pytest.mark.parametrize(
    "partition,"
    # constants for node indices
    "area_a_first_node_index,"
    "area_a_last_node_index,"
    "area_a_number_of_nodes,"
    "node_border_ab_first_node_index,"
    "node_border_ab_last_node_index,"
    "node_border_ab_number_of_nodes,"
    "area_b_first_node_index,"
    "area_b_last_node_index,"
    "area_b_number_of_nodes,"
    "node_border_bc_first_node_index,"
    "node_border_bc_last_node_index,"
    "node_border_bc_number_of_nodes,"
    "area_c_first_node_index,"
    "area_c_last_node_index,"
    "area_c_number_of_nodes",
    [
        (2, 0, 5, 6, 6, 15, 10, 16, 25, 10, 26, 35, 10, 36, 41, 6),  # partition: 2
        (3, 0, 15, 16, 16, 30, 15, 31, 60, 30, 61, 75, 15, 76, 91, 16),  # partition: 3
        (4, 0, 30, 31, 31, 50, 20, 51, 110, 60, 111, 130, 20, 131, 161, 31),  # partition: 4
    ],
)
def test_constants_for_node_indices(
        partition,
        # constants for node indices
        area_a_first_node_index,
        area_a_last_node_index,
        area_a_number_of_nodes,
        node_border_ab_first_node_index,
        node_border_ab_last_node_index,
        node_border_ab_number_of_nodes,
        area_b_first_node_index,
        area_b_last_node_index,
        area_b_number_of_nodes,
        node_border_bc_first_node_index,
        node_border_bc_last_node_index,
        node_border_bc_number_of_nodes,
        area_c_first_node_index,
        area_c_last_node_index,
        area_c_number_of_nodes,
):
    prt = Partition(partition)
    # Check constants for node indices
    assert prt.area_a.FIRST_NODE_INDEX == area_a_first_node_index
    assert prt.area_a.LAST_NODE_INDEX == area_a_last_node_index
    assert prt.area_a.NUMBER_OF_NODES == area_a_number_of_nodes
    assert prt.node_border_ab.FIRST_NODE_INDEX == node_border_ab_first_node_index
    assert prt.node_border_ab.LAST_NODE_INDEX == node_border_ab_last_node_index
    assert prt.node_border_ab.NUMBER_OF_NODES == node_border_ab_number_of_nodes
    assert prt.area_b.FIRST_NODE_INDEX == area_b_first_node_index
    assert prt.area_b.LAST_NODE_INDEX == area_b_last_node_index
    assert prt.area_b.NUMBER_OF_NODES == area_b_number_of_nodes
    assert prt.node_border_bc.FIRST_NODE_INDEX == node_border_bc_first_node_index
    assert prt.node_border_bc.LAST_NODE_INDEX == node_border_bc_last_node_index
    assert prt.node_border_bc.NUMBER_OF_NODES == node_border_bc_number_of_nodes
    assert prt.area_c.FIRST_NODE_INDEX == area_c_first_node_index
    assert prt.area_c.LAST_NODE_INDEX == area_c_last_node_index
    assert prt.area_c.NUMBER_OF_NODES == area_c_number_of_nodes


@pytest.mark.parametrize(
    "partition,"
    # constants for node layer indices
    "area_a_first_node_layer_index,"
    "area_a_last_node_layer_index,"
    "area_a_number_of_node_layers,"
    "node_border_ab_node_layer_index,"
    "area_b_first_node_layer_index,"
    "area_b_last_node_layer_index,"
    "area_b_number_of_node_layers,"
    "area_b_number_of_node_layer_nodes,"
    "node_border_bc_node_layer_index,"
    "area_c_first_node_layer_index,"
    "area_c_last_node_layer_index,"
    "area_c_number_of_node_layers",
    [
        (4, 0, 3, 4, 4, 5, 7, 3, 20, 8, 9, 12, 4),  # partition: 4
    ],
)
def test_constants_for_node_layer_indices(
        partition,
        # constants for node layer indices
        area_a_first_node_layer_index,
        area_a_last_node_layer_index,
        area_a_number_of_node_layers,
        node_border_ab_node_layer_index,
        area_b_first_node_layer_index,
        area_b_last_node_layer_index,
        area_b_number_of_node_layers,
        area_b_number_of_node_layer_nodes,
        node_border_bc_node_layer_index,
        area_c_first_node_layer_index,
        area_c_last_node_layer_index,
        area_c_number_of_node_layers,
):
    prt = Partition(partition)
    # Check constants for node layer indices
    assert prt.area_a.FIRST_NODE_LAYER_INDEX == area_a_first_node_layer_index
    assert prt.area_a.LAST_NODE_LAYER_INDEX == area_a_last_node_layer_index
    assert prt.area_a.NUMBER_OF_NODE_LAYERS == area_a_number_of_node_layers
    assert prt.node_border_ab.NODE_LAYER_INDEX == node_border_ab_node_layer_index
    assert prt.area_b.FIRST_NODE_LAYER_INDEX == area_b_first_node_layer_index
    assert prt.area_b.LAST_NODE_LAYER_INDEX == area_b_last_node_layer_index
    assert prt.area_b.NUMBER_OF_NODE_LAYERS == area_b_number_of_node_layers
    assert prt.area_b.NUMBER_OF_NODE_LAYER_NODES == area_b_number_of_node_layer_nodes
    assert prt.node_border_bc.NODE_LAYER_INDEX == node_border_bc_node_layer_index
    assert prt.area_c.FIRST_NODE_LAYER_INDEX == area_c_first_node_layer_index
    assert prt.area_c.LAST_NODE_LAYER_INDEX == area_c_last_node_layer_index
    assert prt.area_c.NUMBER_OF_NODE_LAYERS == area_c_number_of_node_layers


@pytest.mark.parametrize(
    "partition,"
    # constants for triangle indices
    "area_a_first_triangle_index,"
    "area_a_last_triangle_index,"
    "area_a_number_of_triangles,"
    "area_b_first_triangle_index,"
    "area_b_last_triangle_index,"
    "area_b_number_of_triangles,"
    "area_c_first_triangle_index,"
    "area_c_last_triangle_index,"
    "area_c_number_of_triangles",
    [
        (4, 0, 79, 80, 80, 239, 160, 240, 319, 80),  # partition: 4
    ],
)
def test_constants_for_triangle_indices(
        partition,
        # constants for triangle indices
        area_a_first_triangle_index,
        area_a_last_triangle_index,
        area_a_number_of_triangles,
        area_b_first_triangle_index,
        area_b_last_triangle_index,
        area_b_number_of_triangles,
        area_c_first_triangle_index,
        area_c_last_triangle_index,
        area_c_number_of_triangles,
):
    prt = Partition(partition)
    # Check constants for triangle indices
    assert prt.area_a.FIRST_TRIANGLE_INDEX == area_a_first_triangle_index
    assert prt.area_a.LAST_TRIANGLE_INDEX == area_a_last_triangle_index
    assert prt.area_a.NUMBER_OF_TRIANGLES == area_a_number_of_triangles
    assert prt.area_b.FIRST_TRIANGLE_INDEX == area_b_first_triangle_index
    assert prt.area_b.LAST_TRIANGLE_INDEX == area_b_last_triangle_index
    assert prt.area_b.NUMBER_OF_TRIANGLES == area_b_number_of_triangles
    assert prt.area_c.FIRST_TRIANGLE_INDEX == area_c_first_triangle_index
    assert prt.area_c.LAST_TRIANGLE_INDEX == area_c_last_triangle_index
    assert prt.area_c.NUMBER_OF_TRIANGLES == area_c_number_of_triangles


@pytest.mark.parametrize(
    "partition,"
    # constants for triangle layer indices
    "area_a_first_triangle_layer_index,"
    "area_a_last_triangle_layer_index,"
    "area_a_number_of_triangle_layers,"
    "area_b_first_triangle_layer_index,"
    "area_b_last_triangle_layer_index,"
    "area_b_number_of_triangle_layers,"
    "area_c_first_triangle_layer_index,"
    "area_c_last_triangle_layer_index,"
    "area_c_number_of_triangle_layers",
    [
        (4, 0, 3, 4, 4, 7, 4, 8, 11, 4),  # partition: 4
    ],
)
def test_constants_for_triangle_layer_indices(
        partition,
        # constants for triangle layer indices
        area_a_first_triangle_layer_index,
        area_a_last_triangle_layer_index,
        area_a_number_of_triangle_layers,
        area_b_first_triangle_layer_index,
        area_b_last_triangle_layer_index,
        area_b_number_of_triangle_layers,
        area_c_first_triangle_layer_index,
        area_c_last_triangle_layer_index,
        area_c_number_of_triangle_layers,
):
    prt = Partition(partition)
    # Check constants for triangle layer indices
    assert prt.area_a.FIRST_TRIANGLE_LAYER_INDEX == area_a_first_triangle_layer_index
    assert prt.area_a.LAST_TRIANGLE_LAYER_INDEX == area_a_last_triangle_layer_index
    assert prt.area_a.NUMBER_OF_TRIANGLE_LAYERS == area_a_number_of_triangle_layers
    assert prt.area_b.FIRST_TRIANGLE_LAYER_INDEX == area_b_first_triangle_layer_index
    assert prt.area_b.LAST_TRIANGLE_LAYER_INDEX == area_b_last_triangle_layer_index
    assert prt.area_b.NUMBER_OF_TRIANGLE_LAYERS == area_b_number_of_triangle_layers
    assert prt.area_c.FIRST_TRIANGLE_LAYER_INDEX == area_c_first_triangle_layer_index
    assert prt.area_c.LAST_TRIANGLE_LAYER_INDEX == area_c_last_triangle_layer_index
    assert prt.area_c.NUMBER_OF_TRIANGLE_LAYERS == area_c_number_of_triangle_layers
