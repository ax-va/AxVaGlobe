import pytest

from core.schema.partition import Partition


@pytest.mark.parametrize(
    "partition,"
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
        (4, 0, 30, 31, 31, 50, 20, 51, 110, 60, 111, 130, 20, 131, 161, 31),
    ],
)
def test_valid_partitions(
		partition,
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
