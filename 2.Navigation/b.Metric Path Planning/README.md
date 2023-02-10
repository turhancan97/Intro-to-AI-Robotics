1. Represent your indoor environment as a GVG, regular grid, and quadtree.

Representing an indoor environment as a Graph-Based Virtual Environment (GVG), regular grid, and quadtree can be done as follows:

Graph-Based Virtual Environment (GVG):
    A GVG is a type of graph-based representation of an environment where nodes represent the locations or landmarks in the environment and edges represent the connectivity between those locations. In an indoor environment, nodes can represent rooms, doorways, and other distinctive places while edges can represent the paths connecting those locations.

Regular Grid:
    A regular grid is a type of representation where the environment is divided into a grid of cells. Each cell can be occupied by an object or be empty. In an indoor environment, the cells can represent rooms, hallways, or other distinctive places.

Quadtree:
    A quadtree is a type of representation where the environment is divided into four quadrants recursively. This representation can be used to divide an indoor environment into regions with different levels of detail. Each node in the quadtree can represent a region in the environment, and its child nodes can represent sub-regions of that region.

Each representation has its own advantages and disadvantages, and choosing one over the other depends on the specific requirements of the task at hand. For example, the regular grid representation is simple and straightforward, but it may not be suitable for complex environments with irregular shapes. The quadtree representation is useful for large environments, but it may be computationally expensive. The GVG representation is suitable for environments with distinctive landmarks, but it may be difficult to build for some environments.

2. Represent your indoor environment as a regular grid with a 10cm scale. Write down the rule you use to decide how to mark a grid element empty or occupied when there is a small portion overlapping it.

A regular grid is a 2D representation of a physical environment, where each cell of the grid represents an area of 10cm x 10cm. To decide how to mark a grid element as empty or occupied, you can use a simple rule called occupancy grid mapping.

The rule is as follows:

If more than 50% of the cell is occupied by an object, the cell is marked as occupied.

If less than 50% of the cell is occupied by an object, the cell is marked as empty.

This rule ensures that the grid representation accurately reflects the physical environment, and that small portions of overlapping objects do not significantly affect the overall representation.

3. Define path relaxation.

Path relaxation is a technique used in graph algorithms to determine the shortest path between two nodes. It involves iteratively updating the cost of reaching a node through an intermediate node, checking if it provides a more efficient path than previously known. The process continues until the shortest path from the start node to the end node is found. Path relaxation is commonly used in algorithms such as Dijkstra's algorithm and Bellman-Ford algorithm to find the shortest path in a weighted graph.

4. Consider a regular grid of size 20 by 20. How many edges will a graph have if the neighbors are a. 4-connected? b. 8-connected?

    a. 4-connected: In a 4-connected graph, each grid cell is connected to its immediate neighbors (north, south, east, and west). So, each grid cell will have at most 4 edges. In a 20 by 20 grid, there will be 20 * 20 = 400 grid cells. So, the number of edges in a 4-connected graph will be 400 * 4 = 1600.

    b. 8-connected: In an 8-connected graph, each grid cell is connected to its diagonally adjacent neighbors as well as the immediate neighbors (north, south, east, and west). So, each grid cell will have at most 8 edges. In a 20 by 20 grid, there will be 20 * 20 = 400 grid cells. So, the number of edges in an 8-connected graph will be 400 * 8 = 3200.

5. Convert a meadow map into a graph using: a. the midpoints of the open boundaries, and b. the midpoints plus the 2 endpoints. Draw a path from A to B on both graphs. Describe the differences.

The conversion of a meadow map into a graph using midpoints of the open boundaries involves selecting the midpoint of each open boundary and treating them as nodes. These nodes are then connected to their neighboring nodes with edges. The resulting graph would have less nodes than the original meadow map, but still retain enough information to represent the open spaces in the map.

On the other hand, the conversion of the meadow map into a graph using midpoints plus the 2 endpoints involves selecting the midpoint and the 2 endpoints of each open boundary and treating them as nodes. These nodes are then connected to their neighboring nodes with edges. The resulting graph would have more nodes than the previous graph, but would provide more detailed information about the open spaces in the meadow map.

To draw a path from A to B on both graphs, a pathfinding algorithm such as Dijkstra's or A* can be used. The path will differ between the two graphs due to the different number of nodes and the differing level of detail represented by the graphs. The path on the graph using midpoints plus the 2 endpoints will likely be more direct, as it provides more detailed information about the open spaces in the meadow map.


6. Apply the A* search algorithm by hand to a small graph to find the optimal path between two locations.

A* search algorithm is a popular pathfinding algorithm used for finding the optimal path between two points in a graph. The algorithm combines the advantages of Dijkstra's algorithm and greedy search algorithm to achieve a better performance.

The basic idea of A* is to use a heuristic function to estimate the distance between the current node and the goal node. The algorithm will prioritize nodes that have a low f(n) value, where f(n) = g(n) + h(n). g(n) is the actual cost from the start node to the current node, and h(n) is the estimated cost from the current node to the goal node.

A - B (cost = 2)
B - C (cost = 3)
B - D (cost = 1)
C - E (cost = 5)
D - E (cost = 4)
D - F (cost = 2)

If we want to find the optimal path from node A to node F, we can apply the A* search algorithm as follows:

    Start by creating a priority queue and adding node A with a cost of 0.
    Remove node A from the priority queue and add its neighbors to the queue. For each neighbor, calculate the cost as the sum of the cost to reach node A and the cost of the edge connecting node A to the neighbor. In this case, the neighbors are B with a cost of 2 and C with a cost of 5.
    Repeat step 2 with node B. Remove node B from the priority queue and add its neighbors. Calculate the cost of each neighbor as the sum of the cost to reach node B and the cost of the edge connecting node B to the neighbor. In this case, the neighbors are C with a cost of 5 and D with a cost of 3.
    Repeat step 2 with node D. Remove node D from the priority queue and add its neighbors. Calculate the cost of each neighbor as the sum of the cost to reach node D and the cost of the edge connecting node D to the neighbor. In this case, the neighbors are E with a cost of 7 and F with a cost of 5.
    Repeat step 2 with node F. Since node F is the target node, we stop the algorithm and return the cost of 5 as the optimal cost from node A to node F.

The optimal path from node A to node F is A - B - D - F.

In conclusion, the A* algorithm is a powerful tool for finding the optimal path in a graph, and it is widely used in many applications such as autonomous navigation, games, and planning.

7. What is a heuristic function?

A heuristic function is a mathematical function that provides a prediction or estimate of the best solution to a problem, based on available information. It is used in algorithms, such as the A* algorithm, to guide the search for a solution by providing an estimation of the cost to reach the goal state. The heuristic function helps the algorithm to prioritize which nodes to explore first, and provides a measure of how close the current node is to the goal state. The accuracy of the heuristic function has a direct impact on the efficiency of the algorithm.

8. Apply wavefront propagation to a regular grid.

Wavefront propagation is a path planning algorithm commonly used in robotics to find the shortest path from a start location to a goal location. In this algorithm, a wavefront is propagated outwards from the start location until it reaches the goal location. The wavefront represents the potential distance from the start location.

In a regular grid, the wavefront can be propagated in four directions: up, down, left, and right. Each grid cell is assigned a value representing the distance from the start location. Initially, the value of the start cell is set to 0 and its neighbors are set to 1. Then, the wavefront is propagated outwards by updating the value of the cells to be the minimum of the values of its neighbors plus 1. This process continues until the wavefront reaches the goal cell.

For example, consider a 4x4 regular grid with the start cell at (1,1) and the goal cell at (4,4). The initial grid would look like this:

0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0

The first iteration would update the values of the neighbors of the start cell to 1:

0 1 0 0
1 0 0 0
0 0 0 0
0 0 0 0

The next iteration would update the values of the neighbors of the cells with value 1:

0 1 0 0
1 2 0 0
0 0 0 0
0 0 0 0

This process continues until the goal cell is reached. The final grid would look like this:

0 1 2 3
1 2 3 4
2 3 4 5
3 4 5 6

The path from start to goal can be found by backtracking from the goal cell to the start cell, following the cells with the lowest values.

9.  Subgoal obsession has been described as a problem for metric planners. Can hybrid systems which use topological planning exhibit subgoal obsession?

Subgoal obsession can occur in both metric and topological planners. In a topological planner, subgoal obsession occurs when the robot becomes fixated on reaching a specific subgoal, such as a landmark or intermediate node, instead of considering the overall path to the final destination. This can lead to inefficiencies and potential obstacles being missed. Therefore, even in a hybrid system that uses topological planning, it is important to implement strategies to avoid subgoal obsession and ensure the robot is considering the most efficient and safe path to the final destination.

10. Trulla uses a dot product of 0 or less to trigger replanning, which corresponds to 90 degree from the desired path. What are the advantages or disadvantages of 90 degree? What would happen if Trulla used 45 degree or 135 degree?

Trulla uses a dot product of 0 or less to trigger replanning, meaning that the angle between the current heading of the robot and the desired path is greater than or equal to 90 degrees. This threshold ensures that replanning occurs only when the robot has deviated significantly from its intended path.

The advantage of using a 90 degree threshold is that it is a conservative approach that reduces the frequency of replanning and minimizes the computational resources required to generate a new path. This can be especially important in real-world environments where processing power is limited.

However, there are also some disadvantages to using a 90 degree threshold. For example, if the environment is cluttered, the robot may not detect obstacles until it is too late and has already deviated from its desired path. In such cases, a more aggressive approach to replanning, such as a 45 degree or 135 degree threshold, may be more appropriate.

If Trulla used a 45 degree threshold, it would trigger replanning more frequently, resulting in a smoother path and a better response to changes in the environment. However, this would also increase the computational requirements, potentially slowing down the robot's performance. If Trulla used a 135 degree threshold, it would trigger replanning less frequently, potentially leading to a less smooth path and a slower response to changes in the environment. Ultimately, the choice of threshold will depend on the specific requirements of the task and the limitations of the hardware and software being used.

11. Describe the difference between continuous and event-driven replanning. Which would be more appropriate for a planetary rover? Justify your answer.

Continuous replanning is the process of continually updating and adjusting the robot's plan in real-time as it moves and gathers information. The robot's current position, sensory input, and potential obstacles are used to continually update its plan to ensure it is on the optimal path.

Event-driven replanning, on the other hand, only occurs when specific trigger events occur, such as a change in the environment, a failure of a component, or a change in the robot's goal. The robot only updates its plan in response to these events and does not continually adjust its plan as it moves.

For a planetary rover, event-driven replanning would be more appropriate. This is because the environment on a planet is often extremely hostile and can change rapidly, making continuous replanning difficult. Additionally, the slow and resource-intensive nature of continuous replanning would limit the rover's ability to explore and gather information. Event-driven replanning allows the rover to conserve resources while still being able to react to changes in its environment as they occur.

12.  [Programming] Obtain a copy of the Trulla simulator suitable for running under Windows. Model at least three different scenarios and see what the path generated is.

-- No answer is provided

13.  [Programming] Program an A* path planner. Compare the results to the results for the Dijkstra’s single source shortest path program from Ch. 9.

> run q13_1.py and q13_2.py

Dijkstra's algorithm and A* algorithm are two of the most widely used algorithms for finding the shortest path between two nodes in a graph. Both algorithms work by maintaining a priority queue of nodes, where the priority is based on the distance from the starting node.

Dijkstra's algorithm works by exploring all the nodes in the graph and updating the distances of their neighbors. It updates the distances of all the neighbors to the starting node until it reaches the goal node. Dijkstra's algorithm is guaranteed to find the shortest path in a graph, but it can be slow in large graphs because it explores all nodes even if they are not on the optimal path.

A* algorithm is an improvement of Dijkstra's algorithm that speeds up the search process by incorporating a heuristic function. The heuristic function is an estimate of the remaining distance from the current node to the goal node. The algorithm uses this estimate to prioritize the nodes that are closer to the goal node and minimize the number of nodes that need to be explored. The heuristic function must be admissible, meaning it must never overestimate the actual distance, and consistent, meaning it must satisfy the triangle inequality.

In conclusion, A* algorithm is faster than Dijkstra's algorithm because it prioritizes nodes that are likely to be on the optimal path. However, it depends on the quality of the heuristic function, so the results of A* algorithm may not be optimal if the heuristic function is not admissible and consistent.

