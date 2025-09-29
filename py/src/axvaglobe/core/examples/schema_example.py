from axvaglobe.core.schema import Schema

schema_4 = Schema(4)

node_25 = schema_4.get_node_by_its_index(25)
print(node_25)
# _NodeA(3, 9, Constants(4))
print(node_25.INDEX)
# 25
print(node_25.LAYER_INDEX)
# 3
print(node_25.IN_LAYER_INDEX)
# 9

node_100 = schema_4.get_node_by_its_index(100)
print(node_100)
# _NodeB(7, 9, Constants(4))
print(node_100.INDEX)
# 100
print(node_100.LAYER_INDEX)
# 7
print(node_100.IN_LAYER_INDEX)
# 9
