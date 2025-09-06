from core.schema import Schema

schema_4 = Schema(4)

schema_4_node_25 = schema_4.get_node_by_index(25)
print(schema_4_node_25)
# _NodeA(3, 9, Constants(4))
print(schema_4_node_25.INDEX)
# 25
print(schema_4_node_25.LAYER_INDEX)
# 3
print(schema_4_node_25.IN_LAYER_INDEX)
# 9

schema_4_node_100 = schema_4.get_node_by_index(100)
print(schema_4_node_100)
# _NodeB(7, 9, Constants(4))
print(schema_4_node_100.INDEX)
# 100
print(schema_4_node_100.LAYER_INDEX)
# 7
print(schema_4_node_100.IN_LAYER_INDEX)
# 9
