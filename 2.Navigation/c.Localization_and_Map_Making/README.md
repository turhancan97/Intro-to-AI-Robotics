# Exercises - Chapter 11

## Localization and Map Making

---

1. An important property of an occupancy grid is that it supports sensor fusion. Define sensor fusion in one or two sentences and give two examples.

Sensor fusion is the process of combining multiple sources of information to produce a more accurate and complete representation of a given situation. An example of sensor fusion in robotics is the combination of data from lidar, radar, and camera sensors to produce a more complete map of the environment. Another example is the use of inertial measurement units and GPS data to estimate the position and orientation of a robot with higher accuracy.
   
2. What is the difference between an occupancy grid, a certainty grid, and an evidence grid?

An occupancy grid is a 2D map representation of the environment in which each cell represents the probability of that cell being occupied by an obstacle. A certainty grid, on the other hand, is a 2D map representation of the environment in which each cell has a binary value of either occupied (1) or unoccupied (0) with no probability values in between. An evidence grid is a 2D map representation of the environment in which each cell stores the accumulated sensor data that contributes to the cell's occupancy value. The occupancy value for each cell in an evidence grid can range from 0 to 1, representing the probability of the cell being occupied.

In summary, an occupancy grid provides a probabilistic representation of the environment, a certainty grid provides a binary representation, and an evidence grid provides a more detailed representation of the sensor data that contributes to the occupancy value of each cell.
   
3. What is the difference between iconic and feature-based localization?

Iconic and feature-based localization are two different approaches to robot localization. Iconic localization refers to the use of an iconic map, or an image-based representation of the environment, as the basis for localization. This approach is typically used when the robot has an overhead view of the environment, and uses image processing techniques to match the current image with the iconic map.

Feature-based localization, on the other hand, refers to the use of landmarks or features within the environment as the basis for localization. This approach is typically used when the robot does not have an overhead view, and instead relies on sensors such as lidar or sonar to detect and identify distinctive landmarks. The robot then uses the positions of these landmarks to estimate its position relative to the environment.

In summary, iconic localization is based on image processing, while feature-based localization is based on the detection and identification of distinctive landmarks.

4. List the desirable attributes of a landmark. Discuss why or why not each of the following might make a good landmark for feature-based localization: a. Corner b. Intersection of hallways c. Open doorway

The desirable attributes of a landmark include:

    Distinctiveness: The landmark should be unique and distinguishable from other objects in the environment.

    Robustness: The landmark should be easily recognizable and robust against changes in the environment.

    Reliability: The landmark should be consistent and reliable for the robot to be able to identify it every time.

    Visibility: The landmark should be easily visible from different angles and viewpoints.

    Location: The landmark should be placed in a convenient and accessible location.

a. Corner: Corners could make good landmarks for feature-based localization because they are distinctive and robust. They can also be easily visible from different angles and viewpoints, making them reliable landmarks. However, the consistency of corners might be affected by changes in the environment, which could cause difficulties in recognizing them.

b. Intersection of hallways: Intersections of hallways could make good landmarks because they are distinctive, reliable, and visible from different angles. However, they may not be as robust as other landmarks, as changes in the environment could alter their appearance and reduce their reliability.

c. Open doorway: Open doorways could make good landmarks for feature-based localization because they are distinctive and easily visible from different angles and viewpoints. However, the consistency and reliability of open doorways might be affected by changes in the environment, such as the door being closed or the hallway being blocked, which could make it difficult for the robot to recognize them.

5. Name three applications where metric map-making might be useful.

**Autonomous Driving:** Metric map-making can be useful in autonomous driving, as it can provide a map of the driving environment with precise measurements, which can be used for navigation and route planning.

**Robotics:** In robotics, metric maps can be used for navigation, obstacle avoidance, and task planning.

**Augmented Reality:** Metric map-making can also be used in augmented reality applications, where it can provide a high-resolution, 3D model of a real-world environment for virtual objects to be overlaid onto. This can improve the accuracy and reliability of AR applications.

6. Why is localization important in map-making?

Localization is important in map-making because it is the process of determining the location of the robot within the environment. This information is crucial for building a map of the environment as it allows the robot to identify where it is relative to the objects and landmarks it observes. This allows the robot to correlate the data it collects about the environment with its position, thereby allowing the creation of a accurate and useful map. In addition, localization also helps the robot to refine its map as it moves through the environment and collects more information. Overall, localization plays a critical role in enabling the creation of high-quality maps and is an essential component of map-making.

7. Suppose a localization algorithm had an order complexity of O(m x n), where m is the number of columns and n is the number of rows in the occupancy grid. Therefore if the algorithm operated over a 10 x 10 grid, approximately 100 operations would be executed for localization. What would be the number of operations if the grid were: a. 100 x 100? b. 1000 x 1000? c. 5000 x 2000?

a. 100 x 100 grid: 100 operations * 100 columns * 100 rows = 100,000 operations

b. 1000 x 1000 grid: 100 operations * 1000 columns * 1000 rows = 100,000,000 operations

c. 5000 x 2000 grid: 100 operations * 5000 columns * 2000 rows = 100,000,000,000 operations
   
8. Repeat the previous problem where the order complexity is O((m x n)^2)

If the order complexity of the localization algorithm is O((m x n)^2), then the number of operations for the 10 x 10 grid would be approximately 100^2 = 10,000 operations.

For the 100 x 100 grid, the number of operations would be approximately 100^2 * 100^2 = 10,000,000,000 operations.

For the 1000 x 1000 grid, the number of operations would be approximately 1000^2 * 1000^2 = 100,000,000,000,000 operations.

For the 5000 x 2000 grid, the number of operations would be approximately 5000^2 * 2000^2 = 50,000,000,000,000 operations.

9.  Construct a series of readings that using the HIMM update rule would produce the same final grid as produced by GRO in Fig. 11.13.

-- No answer is provided

10. Consider how the robot moves from one frontier to another in frontier-based exploration. What are the advantages and disadvantages of explicitly planning a path between frontier centroids versus using a purely reactive move-to-goal and avoid set of behaviors?

In frontier-based exploration, the robot moves from one frontier to another in order to gather more information about its environment. When planning a path between frontier centroids, the algorithm explicitly plans a path between the two frontiers, which can result in more efficient and effective exploration. This approach can lead to fewer wasted movements and a more comprehensive coverage of the environment.

However, explicitly planning a path between frontier centroids can be computationally expensive and may require more processing power, which may be problematic for systems with limited computational resources. Additionally, if the frontiers are far apart, the path between them may be long and complex, which can result in increased risk of failure or obstacles that the robot may encounter along the way.

On the other hand, using a purely reactive move-to-goal and avoid set of behaviors is a more simple and efficient approach. The robot uses local information to move directly towards the goal, avoiding any obstacles along the way. This approach is more reactive, meaning that the robot will quickly adapt to changes in the environment and can be less computationally intensive.

However, the disadvantage of this approach is that the robot may waste energy and time by taking unnecessarily long or indirect paths. Additionally, this approach may be less effective in environments with large, complex obstacles, as the robot may be unable to effectively navigate around these obstacles without additional information or sensing capabilities.

In summary, both approaches have their advantages and disadvantages, and the choice between them will depend on the specific requirements and constraints of the exploration task.

11. Compare frontier-based exploration with GVG (Generalized Voronoi graph) exploration. Is one better suited for certain environments than the other?

Frontier-based exploration and GVG exploration are two different approaches for mapping and exploring unknown environments. Frontier-based exploration focuses on finding and mapping the boundaries between known and unknown areas, while GVG exploration is based on the idea of mapping and exploring areas where the distance to known points is equal.

Each approach has its own advantages and disadvantages, and one may be better suited for certain environments than the other.

Advantages of Frontier-based exploration:

    Frontier-based exploration is well suited for environments with sparse or isolated unknown areas as it can quickly identify these frontiers and plan an efficient path to explore them.
    It is a simple and intuitive approach that can be easily implemented with a small set of behaviors.

Disadvantages of Frontier-based exploration:

    Frontier-based exploration can be inefficient in dense environments with many unknown areas as it may prioritize exploring the wrong frontiers.
    It can also be computationally expensive as it requires continuous computation of the frontiers.

Advantages of GVG exploration:

    GVG exploration is well suited for dense environments with many unknown areas as it can explore areas of equal distance to known points in a systematic manner.
    It is a more efficient approach as it does not require continuous computation of frontiers.

Disadvantages of GVG exploration:

    GVG exploration is a more complex approach that requires a sophisticated algorithm and data structure to implement.
    It may also become computationally expensive in large environments as it requires continuous computation of the GVG.

In conclusion, the choice between frontier-based exploration and GVG exploration depends on the characteristics of the environment and the desired efficiency and accuracy of the mapping process.

12. Consider how both exploration strategies (frontier and GVG) often have to choose between possible areas to explore and then save the choices not taken for further exploration. Which data structure do you think would be better to store the choices, a stack or a priority queue? Why?

A priority queue is better suited to store the choices in exploration strategies. A priority queue stores elements based on priority, allowing elements with higher priority to be processed before those with lower priority. In frontier-based exploration, the priority could be assigned based on the estimated utility of exploring an area, such as the expected information gain or reward. The same could be applied for GVG exploration, where the priority could be based on the estimated distance to the frontier or the expected information gain.

A stack, on the other hand, processes elements in a last-in-first-out manner, which may not be ideal for exploration. In frontier-based exploration, choosing the last area added to the stack may not necessarily be the best choice, as it may have low utility or information gain. The same could be applied for GVG exploration, where choosing the last area added to the stack may not be the best choice, as it may not be the closest or most valuable frontier.

In summary, a priority queue is more suitable for exploration strategies as it allows elements with higher priority to be processed first, ensuring that the best choices are made.

13. [Programming] Write a program for a robot which moves to the centroid of an unknown area. Test it for a variety of room configurations, and describe where it stops in each case.

> run q13.py

14. [Advanced Reading] Read “Dervish: An Office-Navigating Robot,” by Illah Nourbakhsh, and “Xavier: A Robot Navigation Architecture Based on Partially Observable Markov Decision Process Models,” by Sven Koenig and Reid Simmons in Artificial Intelligence and Mobile Robots: Case Studies of Succesful Robot System, ed. Kortenkamp, Bonasso, Murphy. Describe how these approaches would work for the example in Fig. 11.21. Comment on the similarities and differences

-- No answer is provided