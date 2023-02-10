from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt

# Define a list of points
points = [(0,0), (0,1), (1,0), (1,1), (0.5,0.5), 
        (1.5,1.5), (0,1.5),(1.5,0),(2,2),(1,2),(2,1),(3,3),(2,3),(3,2)]

# Compute the Voronoi diagram
vor = Voronoi(points)

# Plot the diagram
voronoi_plot_2d(vor)
plt.show()