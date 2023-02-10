import numpy as np
import matplotlib.pyplot as plt

# Define the landmark location
landmark = np.array([5, 5])

# Define the robot's starting position
robot_start = np.array([0, 0])

# Define the steps for the hill-climbing algorithm
steps = np.array([[1, 0], [0, 1], [-1, 0], [0, -1]])

# Initialize the robot's position
robot_pos = robot_start

# Define a function to calculate the distance between the robot and the landmark
def distance(robot_pos, landmark):
    return np.linalg.norm(robot_pos - landmark)

pos_x = []
pos_y = []


# Define the hill-climbing algorithm
while True:
    # Initialize the minimum distance to infinity
    min_distance = float('inf')
    
    # Check the distance for each step
    for step in steps:
        pos_x.append(robot_pos[0])
        pos_y.append(robot_pos[1])
        new_pos = robot_pos + step
        new_distance = distance(new_pos, landmark)
        
        # Update the minimum distance and the new position if the distance is smaller
        if new_distance < min_distance:
            min_distance = new_distance
            robot_pos = new_pos
    
    # Stop the loop if the robot reaches the landmark
    if min_distance <= 0:
        break

# Plot the results
plt.scatter(landmark[0], landmark[1], color='red', marker='x', label='Landmark')
plt.scatter(robot_start[0], robot_start[1], color='blue', marker='o', label='Start')
plt.scatter(robot_pos[0], robot_pos[1], color='green', marker='o', label='End')
plt.plot(pos_x,pos_y,c='b',alpha=0.5, label='Trajectory')
plt.xlim(-10,10)
plt.ylim(-10,10)
plt.legend()
plt.show()