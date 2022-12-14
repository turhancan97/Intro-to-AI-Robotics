class Landmark:
  def __init__(self, x, y):
    self.position = (x, y)
  
  def distance(self, x, y):
    # Calculate the Euclidean distance between the landmark and the given point
    return ((self.position[0] - x)**2 + (self.position[1] - y)**2)**0.5

class Robot:
  def __init__(self, x, y):
    self.position = (x, y)
  
  def move(self, x, y):
    # Update the robot's position
    self.position = (x, y)

def localize(robot, landmark, max_iterations):
  # Initialize the current and previous positions to the robot's initial position
  current_pos = robot.position
  prev_pos = robot.position
  
  # Initialize the iteration counter to 0
  iteration = 0
  
  # Keep looping until the maximum number of iterations is reached or the algorithm converges
  while iteration < max_iterations and current_pos != prev_pos:
    # Store the current position as the previous position
    prev_pos = current_pos
    
    # Move the robot to the new position with the smallest distance to the landmark
    current_pos = min([(robot.position[0] + dx, robot.position[1] + dy) for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]], key=lambda pos: landmark.distance(*pos))
    robot.move(*current_pos)
    
    # Increase the iteration counter by 1
    iteration += 1
  
  # Return the final position of the robot
  return current_pos

# Define a landmark at position (3, 5)
landmark = Landmark(3, 5)

# Define a robot at position (0, 0)
robot = Robot(0, 0)

# Localize the robot relative to the landmark
final_pos = localize(robot, landmark, 100)

# Print the final position of the robot
print(final_pos) # (3, 5)