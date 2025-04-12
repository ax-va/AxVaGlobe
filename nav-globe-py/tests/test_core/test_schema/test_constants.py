import pytest

from core.schema.constants import Constants


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
    constants = Constants(partition)
    # Check common constants
    assert constants.NUMBER_OF_NODES == number_of_nodes
    assert constants.NUMBER_OF_TRIANGLES == number_of_triangles
    assert constants.NUMBER_OF_NODE_LAYERS == number_of_node_layers
    assert constants.NUMBER_OF_TRIANGLE_LAYERS == number_of_triangle_layers
    assert constants.NUMBER_OF_EDGE_NODES == number_of_node_edges


@pytest.mark.parametrize(
    "partition,"
    # constants for node indices
    "north_pole_node_index,"
    "area_a_nodes_start,"
    "area_a_nodes_end,"
    "area_a_nodes_number,"
    "border_ab_nodes_start,"
    "border_ab_nodes_end,"
    "border_ab_nodes_number,"
    "area_b_nodes_start,"
    "area_b_nodes_end,"
    "area_b_nodes_number,"
    "border_bc_nodes_start,"
    "border_bc_nodes_end,"
    "border_bc_nodes_number,"
    "area_c_nodes_start,"
    "area_c_nodes_end,"
    "area_c_nodes_number,"
    "south_pole_node_index",
    [
        (2, 0, 1, 5, 5, 6, 15, 10, 16, 25, 10, 26, 35, 10, 36, 40, 5, 41),  # partition: 2
        (3, 0, 1, 15, 15, 16, 30, 15, 31, 60, 30, 61, 75, 15, 76, 90, 15, 91),  # partition: 3
        (4, 0, 1, 30, 30, 31, 50, 20, 51, 110, 60, 111, 130, 20, 131, 160, 30, 161),  # partition: 4
    ],
)
def test_constants_for_node_indices(
        partition,
        # constants for node indices
        north_pole_node_index,
        area_a_nodes_start,
        area_a_nodes_end,
        area_a_nodes_number,
        border_ab_nodes_start,
        border_ab_nodes_end,
        border_ab_nodes_number,
        area_b_nodes_start,
        area_b_nodes_end,
        area_b_nodes_number,
        border_bc_nodes_start,
        border_bc_nodes_end,
        border_bc_nodes_number,
        area_c_nodes_start,
        area_c_nodes_end,
        area_c_nodes_number,
        south_pole_node_index,
):
    constants = Constants(partition)
    # Check constants for node indices
    assert constants.north_pole.node.INDEX == north_pole_node_index
    assert constants.area_a.nodes.START == area_a_nodes_start
    assert constants.area_a.nodes.END == area_a_nodes_end
    assert constants.area_a.nodes.NUMBER == area_a_nodes_number
    assert constants.border_ab.nodes.START == border_ab_nodes_start
    assert constants.border_ab.nodes.END == border_ab_nodes_end
    assert constants.border_ab.nodes.NUMBER == border_ab_nodes_number
    assert constants.area_b.nodes.START == area_b_nodes_start
    assert constants.area_b.nodes.END == area_b_nodes_end
    assert constants.area_b.nodes.NUMBER == area_b_nodes_number
    assert constants.border_bc.nodes.START == border_bc_nodes_start
    assert constants.border_bc.nodes.END == border_bc_nodes_end
    assert constants.border_bc.nodes.NUMBER == border_bc_nodes_number
    assert constants.area_c.nodes.START == area_c_nodes_start
    assert constants.area_c.nodes.END == area_c_nodes_end
    assert constants.area_c.nodes.NUMBER == area_c_nodes_number
    assert constants.south_pole.node.INDEX == south_pole_node_index


@pytest.mark.parametrize(
    "partition,"
    # constants for triangle indices
    "area_a_triangles_start,"
    "area_a_triangles_end,"
    "area_a_triangles_number,"
    "area_b_triangles_start,"
    "area_b_triangles_end,"
    "area_b_triangles_number,"
    "area_c_triangles_start,"
    "area_c_triangles_end,"
    "area_c_triangles_number",
    [
        (2, 0, 19, 20, 20, 59, 40, 60, 79, 20),  # partition: 2
        (3, 0, 44, 45, 45, 134, 90, 135, 179, 45),  # partition: 3
        (4, 0, 79, 80, 80, 239, 160, 240, 319, 80),  # partition: 4
    ],
)
def test_constants_for_triangle_indices(
        partition,
        # constants for triangle indices
        area_a_triangles_start,
        area_a_triangles_end,
        area_a_triangles_number,
        area_b_triangles_start,
        area_b_triangles_end,
        area_b_triangles_number,
        area_c_triangles_start,
        area_c_triangles_end,
        area_c_triangles_number,
):
    constants = Constants(partition)
    # Check constants for triangle indices
    assert constants.area_a.triangles.START == area_a_triangles_start
    assert constants.area_a.triangles.END == area_a_triangles_end
    assert constants.area_a.triangles.NUMBER == area_a_triangles_number
    assert constants.area_b.triangles.START == area_b_triangles_start
    assert constants.area_b.triangles.END == area_b_triangles_end
    assert constants.area_b.triangles.NUMBER == area_b_triangles_number
    assert constants.area_c.triangles.START == area_c_triangles_start
    assert constants.area_c.triangles.END == area_c_triangles_end
    assert constants.area_c.triangles.NUMBER == area_c_triangles_number


@pytest.mark.parametrize(
    "partition,"
    # constants for node layer indices
    "north_pole_node_layer_index,"
    "area_a_node_layers_start,"
    "area_a_node_layers_end,"
    "area_a_node_layers_number,"
    "border_ab_node_layer_index,"
    "area_b_node_layers_start,"
    "area_b_node_layers_end,"
    "area_b_node_layers_number,"
    "area_b_number_of_nodes_in_node_layer,"
    "border_bc_node_layer_index,"
    "area_c_node_layers_start,"
    "area_c_node_layers_end,"
    "area_c_node_layers_number,"
    "south_pole_node_layer_index",
    [
        (2, 0, 1, 1, 1, 2, 3, 3, 1, 10, 4, 5, 5, 1, 6),  # partition: 2
        (3, 0, 1, 2, 2, 3, 4, 5, 2, 15, 6, 7, 8, 2, 9),  # partition: 3
        (4, 0, 1, 3, 3, 4, 5, 7, 3, 20, 8, 9, 11, 3, 12),  # partition: 4
    ],
)
def test_constants_for_node_layer_indices(
        partition,
        # constants for node layer indices
        north_pole_node_layer_index,
        area_a_node_layers_start,
        area_a_node_layers_end,
        area_a_node_layers_number,
        border_ab_node_layer_index,
        area_b_node_layers_start,
        area_b_node_layers_end,
        area_b_node_layers_number,
        area_b_number_of_nodes_in_node_layer,
        border_bc_node_layer_index,
        area_c_node_layers_start,
        area_c_node_layers_end,
        area_c_node_layers_number,
        south_pole_node_layer_index,
):
    constants = Constants(partition)
    # Check constants for node layer indices
    assert constants.north_pole.node_layer.INDEX == north_pole_node_layer_index
    assert constants.area_a.node_layers.START == area_a_node_layers_start
    assert constants.area_a.node_layers.END == area_a_node_layers_end
    assert constants.area_a.node_layers.NUMBER == area_a_node_layers_number
    assert constants.border_ab.node_layer.INDEX == border_ab_node_layer_index
    assert constants.area_b.node_layers.START == area_b_node_layers_start
    assert constants.area_b.node_layers.END == area_b_node_layers_end
    assert constants.area_b.node_layers.NUMBER == area_b_node_layers_number
    assert constants.area_b.NUMBER_OF_NODES_IN_NODE_LAYER == area_b_number_of_nodes_in_node_layer
    assert constants.border_bc.node_layer.INDEX == border_bc_node_layer_index
    assert constants.area_c.node_layers.START == area_c_node_layers_start
    assert constants.area_c.node_layers.END == area_c_node_layers_end
    assert constants.area_c.node_layers.NUMBER == area_c_node_layers_number
    assert constants.south_pole.node_layer.INDEX == south_pole_node_layer_index


@pytest.mark.parametrize(
    "partition,"
    # constants for triangle layer indices
    "area_a_triangle_layers_start,"
    "area_a_triangle_layers_end,"
    "area_a_triangle_layers_number,"
    "area_b_triangle_layers_start,"
    "area_b_triangle_layers_end,"
    "area_b_triangle_layers_number,"
    "area_c_triangle_layers_start,"
    "area_c_triangle_layers_end,"
    "area_c_triangle_layers_number",
    [
        (2, 0, 1, 2, 2, 3, 2, 4, 5, 2),  # partition: 2
        (3, 0, 2, 3, 3, 5, 3, 6, 8, 3),  # partition: 3
        (4, 0, 3, 4, 4, 7, 4, 8, 11, 4),  # partition: 4
    ],
)
def test_constants_for_triangle_layer_indices(
        partition,
        # constants for triangle layer indices
        area_a_triangle_layers_start,
        area_a_triangle_layers_end,
        area_a_triangle_layers_number,
        area_b_triangle_layers_start,
        area_b_triangle_layers_end,
        area_b_triangle_layers_number,
        area_c_triangle_layers_start,
        area_c_triangle_layers_end,
        area_c_triangle_layers_number,
):
    constants = Constants(partition)
    # Check constants for triangle layer indices
    assert constants.area_a.triangle_layers.START == area_a_triangle_layers_start
    assert constants.area_a.triangle_layers.END == area_a_triangle_layers_end
    assert constants.area_a.triangle_layers.NUMBER == area_a_triangle_layers_number
    assert constants.area_b.triangle_layers.START == area_b_triangle_layers_start
    assert constants.area_b.triangle_layers.END == area_b_triangle_layers_end
    assert constants.area_b.triangle_layers.NUMBER == area_b_triangle_layers_number
    assert constants.area_c.triangle_layers.START == area_c_triangle_layers_start
    assert constants.area_c.triangle_layers.END == area_c_triangle_layers_end
    assert constants.area_c.triangle_layers.NUMBER == area_c_triangle_layers_number
