from axvaglobe.core.schema import Schema

# Get a schema
schema_4 = Schema.get_schema(4)

# Get a node in the schema
node_25 = schema_4.get_node(25)
print(node_25)
# _NodeA(layer_index=3, in_layer_index=9, partition_obj=Partition(partition=4))
print(node_25.INDEX)
# 25
print(node_25.LAYER_INDEX)
# 3
print(node_25.IN_LAYER_INDEX)
# 9

# Get a node in the schema
node_100 = schema_4.get_node(100)
print(node_100)
# _NodeB(layer_index=7, in_layer_index=9, partition_obj=Partition(partition=4))
print(node_100.INDEX)
# 100
print(node_100.LAYER_INDEX)
# 7
print(node_100.IN_LAYER_INDEX)
# 9
