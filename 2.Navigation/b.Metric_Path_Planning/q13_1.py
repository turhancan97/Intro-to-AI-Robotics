import heapq
import numpy as np

def heuristic(a, b):
    # Manhattan distance as heuristic function
    return np.abs(a[0] - b[0]) + np.abs(a[1] - b[1])

def astar(array, start, goal):
    # initialize the heap and the visited set
    heap = []
    heapq.heappush(heap, (0, start))
    visited = set()

    while heap:
        (cost, current) = heapq.heappop(heap)
        if current == goal:
            return cost

        if current in visited:
            continue
        visited.add(current)

        # get the neighbors of the current node
        for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            neighbor = (current[0] + i, current[1] + j)
            if 0 <= neighbor[0] < array.shape[0]:
                if 0 <= neighbor[1] < array.shape[1]:
                    if array[neighbor[0]][neighbor[1]] == 0:
                        heapq.heappush(heap, (cost + heuristic(goal, neighbor), neighbor))

# create a sample 2D grid
grid = np.array([
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0],
])
start = (0, 0)
goal = (4, 5)

# run A* algorithm and print the cost
cost = astar(grid, start, goal)
print("Cost:", cost)