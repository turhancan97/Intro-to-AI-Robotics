import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.light_x = None
        self.light_y = None
        self.in_light = False
    
    def set_light_location(self, x, y):
        self.light_x = x
        self.light_y = y
    
    def phototaxis(self):
        if self.light_x is None or self.light_y is None:
            return 'No light Source'
        
        # Move towards the light
        if not self.in_light:
            if self.x < self.light_x:
                self.x += 1
            elif self.x > self.light_x:
                self.x -= 1
            
            if self.y < self.light_y:
                self.y += 1
            elif self.y > self.light_y:
                self.y -= 1
            # print('Move')
    
    def dead_reckoning(self, obstacles):
        # Avoid obstacles
        while True:
            if not self.in_light:
                dx = random.uniform(-0.5, 0.5)
                dy = random.uniform(-0.5, 0.5)
                new_x = self.x + dx
                new_y = self.y + dy
                
                if (new_x, new_y) in obstacles:
                    continue
                # print('No Light')
                self.x = new_x
                self.y = new_y
                break
            else:
                # print('Arrived light')
                break
    def check_position(self):
         if abs(self.light_x - self.x) <= 5 and abs(self.light_y - self.y) <= 5:
            self.in_light = True

fig, ax = plt.subplots()
# Example usage
k = 100
light = (np.random.randint(-k, k),np.random.randint(-k, k))
robots = [Robot(np.random.randint(-k, k),np.random.randint(-k, k)),Robot(np.random.randint(-k, k),np.random.randint(-k, k)),Robot(np.random.randint(-k, k),np.random.randint(-k, k)),Robot(np.random.randint(-k, k),np.random.randint(-k, k)),Robot(np.random.randint(-k, k),np.random.randint(-k, k))]

obstacles = [(np.random.randint(-k, k),np.random.randint(-k, k)) for _ in range(6)]

o_x = []
o_y = []
for obstacle in obstacles:
    o_x.append(obstacle[0])
    o_y.append(obstacle[1])
    
for robot in robots:
    robot.set_light_location(*light)

def update(frame):
    ax.clear()
    for robot in robots:
        robot.phototaxis()
        robot.dead_reckoning(obstacles)
        robot.check_position()
        ax.scatter(robot.x, robot.y, c='b',marker='s',linewidths=1)
        ax.scatter(robot.light_x, robot.light_y,c='y',marker='o',linewidths=3)
        ax.scatter(x=o_x,y=o_y,c='k',marker='x',linewidths=3)
        ax.legend(['Robot','light_location','Obstacles'])
        ax.set_title('Multi-agent foraging')
        ax.set_ylabel('y [m]')
        ax.set_xlabel('x [m]')
        fig.canvas.draw()

ani = animation.FuncAnimation(fig, update, frames=150, interval=50,repeat=False)
# plt.show()
ani.save("ligh_move.gif", writer="imagemagick")

