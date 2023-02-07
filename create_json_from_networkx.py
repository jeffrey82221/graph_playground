import networkx as nx

# Create an empty graph
G = nx.Graph()

# Add nodes with properties
G.add_node(1, name='Node 1', type='Type 1')
G.add_node(2, name='Node 2', type='Type 2')
G.add_node(3, name='Node 3', type='Type 1')

# Add edges with properties
G.add_edge(1, 2, weight=10, distance=100)
G.add_edge(2, 3, weight=5, distance=50)

# Access node properties
print(G.nodes[1]['name'])  # Output: Node 1
print(G.nodes[1]['type'])  # Output: Type 1

# Access edge properties
print(G[1][2]['weight'])  # Output: 10
print(G[1][2]['distance'])  # Output: 100


# Creating node_link_data Json:
import pprint

graph_dict = nx.node_link_data(G)
pprint.pprint(graph_dict)

"""
Undirected Simple Graph Example: 

{'directed': False,
 'graph': {}, 
  # metadata of the graph, such as author, mentainer, experiment name can be placed here! 
 'links': [{'distance': 100, 'source': 1, 'target': 2, 'weight': 10},
           {'distance': 50, 'source': 2, 'target': 3, 'weight': 5}],
 'multigraph': False,
 'nodes': [{'id': 1, 'name': 'Node 1', 'type': 'Type 1'},
           {'id': 2, 'name': 'Node 2', 'type': 'Type 2'},
           {'id': 3, 'name': 'Node 3', 'type': 'Type 1'}]}

Multi-Graph Example:

{
    "directed": false,
    "multigraph": true,
    "nodes": [
        {"id": 1, "name": "Node 1"},
        {"id": 2, "name": "Node 2"},
        {"id": 3, "name": "Node 3"}
    ],
    "links": [
        {"source": 1, "target": 2, "weight": 10},
        {"source": 2, "target": 3, "weight": 5},
        {"source": 1, "target": 2, "weight": 15}
    ]
}
"""
import json
with open("graph.json", "w") as f:
    json.dump(graph_dict, f)