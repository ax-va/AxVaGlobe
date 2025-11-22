from axvaglobe.core.schema import Schema, Node

# Get a schema by partition
schema_4: Schema = Schema.get_schema(4)

# Get a node by its index in the schema
node_25: Node = schema_4.get_node(25)

# Investigate the node

print(node_25)
# _NodeA(layer_index=3, in_layer_index=9, partition_obj=Partition(partition=4))
print(node_25.INDEX)
# 25
print(node_25.LAYER_INDEX)
# 3
print(node_25.IN_LAYER_INDEX)
# 9

# Get another node by its index in the schema
node_100: Node = schema_4.get_node(100)

# Investigate the node

print(node_100)
# _NodeB(layer_index=7, in_layer_index=9, partition_obj=Partition(partition=4))
print(node_100.INDEX)
# 100
print(node_100.LAYER_INDEX)
# 7
print(node_100.IN_LAYER_INDEX)
# 9

schema_2 = Schema.get_schema(2)
for i in range(16, 26):
    node_i = schema_2.get_node(i)
    print(node_i.LAYER_INDEX, node_i.IN_LAYER_INDEX)
    neighbors = node_i.get_positions_of_neighbor_nodes()
    print(neighbors)
    print("-"*20)
