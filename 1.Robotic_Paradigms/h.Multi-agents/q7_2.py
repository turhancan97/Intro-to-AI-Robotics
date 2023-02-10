import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Robot:
    def __init__(self, x, y, home_x, home_y, light_x, light_y):
        self.x = x
        self.y = y
        self.home_x = home_x
        self.home_y = home_y
        self.light_x = light_x
        self.light_y = light_y
        self.dx = 0
        self.dy = 0
        self.has_food = False
        
    def phototaxis(self):
        # Phototaxis behavior
        self.light_dx = self.light_x - self.x
        self.light_dy = self.light_y - self.y
        light_distance = np.sqrt(self.light_dx**2 + self.light_dy**2)
        self.dx = self.light_dx / light_distance
        self.dy = self.light_dy / light_distance
        
    def push_to_home(self):
        # Push-to-home behavior
        self.home_dx = self.home_x - self.x
        self.home_dy = self.home_y - self.y
        home_distance = np.sqrt(self.home_dx**2 + self.home_dy**2)
        self.dx = self.home_dx / home_distance
        self.dy = self.home_dy / home_distance
        
    def dead_reckoning(self):
        # Dead reckoning
        self.x += self.dx
        self.y += self.dy
        
    def update(self):
        if self.has_food == False:
            self.phototaxis()
            if abs(self.light_x - self.x) <= 2 and abs(self.light_y - self.y) <= 2:
                self.has_food = True
        else:
            self.push_to_home()
            if abs(self.home_x - self.x) <= 2 and abs(self.home_y - self.y) <= 2:
                self.has_food = False
        self.dead_reckoning()

def update_robots(frame):
    for r in robots:
        r.update()
    xs = [r.x for r in robots]
    ys = [r.y for r in robots]
    ax.clear()
    ax.scatter(xs, ys,c='k',marker='s',linewidths=1)
    ax.scatter([r.light_x], [r.light_y], c='y',marker='o',linewidths=3)
    ax.scatter([r.home_x], [r.home_y], c='g',marker='X',linewidths=3)
    ax.set_title('Cooperating to bring the food home')
    ax.set_ylabel('y [m]')
    ax.set_xlabel('x [m]')
    ax.set_xlim(-k-10,k+10)
    ax.set_ylim(-k-10,k+10)
    ax.legend(['Robot','Light','Home'])
    fig.canvas.draw()

# Initialize robots
num_robots = 5
k = 100
home_x = np.random.randint(0, k)
home_y = np.random.randint(-k,0)
light_x = np.random.randint(0, k)
light_y = np.random.randint(-k,0)
robots = [Robot(np.random.randint(-k, k), np.random.randint(-k, k), home_x, home_y, light_x, light_y) for _ in range(num_robots)]

# Plot robots
fig, ax = plt.subplots()
ani = animation.FuncAnimation(fig, update_robots, 150, interval=200)
# plt.show()
ani.save("home_move.gif", writer="imagemagick")
