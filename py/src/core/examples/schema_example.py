from core.schema import Schema

schema_four = Schema(4)

schema_four_node_25 = schema_four.get_node_by_index(25)
print(schema_four_node_25)
# NodeA(3, 9, Constants(4))
print(schema_four_node_25.INDEX)
# 25
print(schema_four_node_25.LAYER_INDEX)
# 3
print(schema_four_node_25.IN_LAYER_INDEX)
# 9

schema_four_node_100 = schema_four.get_node_by_index(100)
print(schema_four_node_100)
# NodeB(7, 9, Constants(4))
print(schema_four_node_100.INDEX)
# 100
print(schema_four_node_100.LAYER_INDEX)
# 7
print(schema_four_node_100.IN_LAYER_INDEX)
# 9
