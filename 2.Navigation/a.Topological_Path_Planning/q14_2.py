import networkx as nx
import matplotlib.pyplot as plt

edges = [
    (1, 2, {"weight": 4}),
    (1, 3, {"weight": 2}),
    (2, 3, {"weight": 1}),
    (2, 4, {"weight": 5}),
    (3, 4, {"weight": 8}),
    (3, 5, {"weight": 10}),
    (4, 5, {"weight": 2}),
    (4, 6, {"weight": 8}),
    (5, 6, {"weight": 5}),
]
edge_labels = {
    (1, 2): 4,
    (1, 3): 2,
    (2, 3): 1,
    (2, 4): 5,
    (3, 4): 8,
    (3, 5): 10,
    (4, 5): 2,
    (4, 6): 8,
    (5, 6): 5,
}


G = nx.Graph()
for i in range(1, 7):
    G.add_node(i)
G.add_edges_from(edges)

pos = nx.planar_layout(G)

# This will give us all the shortest paths from node 1 using the weights from the edges.
p1 = nx.shortest_path(G, source=1, weight="weight")

# This will give us the shortest path from node 1 to node 6.
p1to6 = nx.shortest_path(G, source=1, target=6, weight="weight")

# This will give us the length of the shortest path from node 1 to node 6.
length = nx.shortest_path_length(G, source=1, target=6, weight="weight")

print("All shortest paths from 1: ", p1)
print("Shortest path from 1 to 6: ", p1to6)
print("Length of the shortest path: ", length)

plt.figure(figsize=(10,5))
ax = plt.gca()

# Draw the graph with shortest path highlighted
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)
edges = [(p1to6[i], p1to6[i + 1]) for i in range(len(p1to6) - 1)]
nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='r', width=2)
ax.set_title('Dijkstra Algorithm with graphs')
# Display the graph
plt.show()
