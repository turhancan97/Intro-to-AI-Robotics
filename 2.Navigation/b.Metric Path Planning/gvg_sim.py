import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d

# Define the start and end points for the robot's path
start = (0,0)
end = (10,10)

# Define a list of points to use as landmarks
landmarks = [(2,2), (8,8), (5,5), (2,8), (8,2)]

# Compute the Voronoi diagram for the landmarks
vor = Voronoi(landmarks)

# Find the index of the nearest landmark to the start and end points
start_idx = np.argmin([np.linalg.norm(np.array(start) - np.array(l)) for l in landmarks])
end_idx = np.argmin([np.linalg.norm(np.array(end) - np.array(l)) for l in landmarks])

# Find the shortest path through the diagram by following the edges from the start to the end
path = [start]
current_idx = start_idx
while current_idx != end_idx:
    for edge in vor.ridge_vertices:
        if current_idx in edge:
            neighbor_idx = edge[0] if edge[1] == current_idx else edge[1]
            path.append(landmarks[neighbor_idx])
            current_idx = neighbor_idx
            break

# Add the end point to the path
path.append(end)

# Plot the diagram and the path
voronoi_plot_2d(vor)
plt.plot([p[0] for p in path], [p[1] for p in path], 'r-')
plt.plot(start[0], start[1], 'bo')
plt.plot(end[0], end[1], 'bo')
plt.xlim(-1,12)
plt.ylim(-1,12)
plt.show()