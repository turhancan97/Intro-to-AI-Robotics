import numpy as np
import random
import matplotlib.pyplot as plt

# Define the size of the unknown area
rows = 20
cols = 20

# Initialize the unknown area with all values set to 0
unknown_area = np.zeros((rows, cols))

# Place some obstacles in the unknown area
num_obstacles = 10
for i in range(num_obstacles):
    obstacle_row = random.randint(0, rows-1)
    obstacle_col = random.randint(0, cols-1)
    unknown_area[obstacle_row][obstacle_col] = 1

# Define the starting location of the robot
robot_row = random.randint(0, rows-1)
robot_col = random.randint(0, cols-1)

# Calculate the centroid of the unknown area
centroid_row = int(np.mean(np.where(unknown_area == 0)[0]))
centroid_col = int(np.mean(np.where(unknown_area == 0)[1]))

# Define the movement steps for the robot
row_step = 0
col_step = 0

if robot_row > centroid_row:
    row_step = -1
elif robot_row < centroid_row:
    row_step = 1

if robot_col > centroid_col:
    col_step = -1
elif robot_col < centroid_col:
    col_step = 1

# Move the robot towards the centroid
while robot_row != centroid_row or robot_col != centroid_col:
    plt.scatter(robot_row, robot_col)
    print(robot_row, robot_col)
    robot_row += row_step
    robot_col += col_step
plt.show()
# The robot has reached the centroid
print("The robot has reached the centroid at", (robot_row, robot_col))
