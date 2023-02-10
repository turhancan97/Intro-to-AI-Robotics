import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
G = nx.Graph()

# Add nodes to the graph
G.add_node(1, pos=(1,1))
G.add_node(2, pos=(2,2))
G.add_node(3, pos=(3,1))
G.add_node(4, pos=(4,2))

# Add edges to the graph
G.add_edge(1, 2, weight=1)
G.add_edge(2, 3, weight=2)
G.add_edge(3, 4, weight=1)

# Find the shortest path using A* algorithm
start = 1
end = 4
path = nx.astar_path(G, start, end, weight='weight')

# Plot the graph
pos = nx.get_node_attributes(G, 'pos')
nx.draw(G, pos, with_labels=True)

# Plot the shortest path
path_edges = [(path[i], path[i+1]) for i in range(len(path) - 1)]
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2)

plt.show()
