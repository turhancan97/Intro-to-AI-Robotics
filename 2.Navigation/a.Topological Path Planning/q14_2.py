import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
G = nx.Graph()

# Add nodes to the graph
G.add_nodes_from([i for i in range(1,7)])

# Add edges to the graph with weight
G.add_edge(1, 2, weight=2)
G.add_edge(1, 4, weight=1)
G.add_edge(1, 6, weight=5)
G.add_edge(2, 3, weight=1)
G.add_edge(2, 4, weight=3)
G.add_edge(2, 5, weight=10)
G.add_edge(2, 6, weight=15)
G.add_edge(3, 5, weight=5)
G.add_edge(3, 4, weight=2)
G.add_edge(3, 6, weight=3)
G.add_edge(4, 5, weight=5)
G.add_edge(4, 6, weight=2)
G.add_edge(4, 3, weight=1)


# Find the shortest path using Dijkstra's algorithm
shortest_path = nx.dijkstra_path(G, 1, 6)

# Draw the graph with shortest path highlighted
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)
edges = [(shortest_path[i], shortest_path[i + 1]) for i in range(len(shortest_path) - 1)]
nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='r', width=2)
plt.title("Dijkstra algorithm")

# Display the graph
plt.show()
