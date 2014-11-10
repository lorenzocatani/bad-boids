"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""
import yaml
import matplotlib

matplotlib.use('TkAgg')

from matplotlib import pyplot as plt
from matplotlib import animation
import random

from numpy import array

c=yaml.load(open("config.yaml"))



class boid(object):
 def __init__(self,x,y,xv,yv):
  self.position_x=x
  self.position_y=y
  self.velocity_x=xv
  self.velocity_y=yv
  
 def distance_square(self,other):
  d = (self.position_x - other.position_x)**2 + (self.position_y - other.position_y)**2
  return d
 
 def fly_towards_middle_x(self,other):
  separation = other.position_x - self.position_x
  self.velocity_x = self.velocity_x + (separation)*c['attraction_index']/c['boids_num']
  return self.velocity_x
 def fly_towards_middle_y(self,other):
  separation = other.position_y - self.position_y
  self.velocity_y = self.velocity_y + (separation)*c['attraction_index']/c['boids_num']
  return self.velocity_y
 
 def fly_away_from_neighbours_x(self,other):
  separation = self.position_x - other.position_x
  self.velocity_x = self.velocity_x + (separation)
  return self.velocity_x
 def fly_away_from_neighbours_y(self,other):
  separation = self.position_y - other.position_y
  self.velocity_y = self.velocity_y + (separation)
  return self.velocity_y
  
 def match_speed_neighbours_x(self,other):
  separation = other.velocity_x-self.velocity_x
  self.velocity_x = self.velocity_x +(separation)*c['speed_tuning_index']/c['boids_num']
  return self.velocity_x 
 def match_speed_neighbours_y(self,other):
  separation = other.velocity_y-self.velocity_y
  self.velocity_y = self.velocity_y +(separation)*c['speed_tuning_index']/c['boids_num']
  return self.velocity_y 
  
  
 
boids=[boid(random.uniform(c['min_x'],c['max_x']) ,random.uniform(c['min_y'],c['max_y']),
  random.uniform(c['min_vel_x'],c['max_vel_x']),random.uniform(c['min_vel_y'],c['max_vel_y'])) for i in range(c['boids_num'])]

 
 
def update_boids(boids): 
	
	# Fly towards the middle
	for boid1 in boids:
	    for boid2 in boids:
	      boid1.fly_towards_middle_x(boid2)
              boid1.fly_towards_middle_y(boid2)
		   
	# Fly away from nearby boids
	for boid1 in boids:
	    for boid2 in boids:
		    if  boid2.distance_square(boid1) < c['separation1']:
		     boid1.fly_away_from_neighbours_x(boid2)
	             boid1.fly_away_from_neighbours_y(boid2)
				 
	# Try to match speed with nearby boids
	for boid1 in boids:
	    for boid2 in boids:
			if boid2.distance_square(boid1) < c['separation2']:
			 boid1.match_speed_neighbours_x(boid2)
	                 boid1.match_speed_neighbours_y(boid2)
					 
	# Move according to velocities
	for boid in boids:
		boid.position_x = boid.position_x + boid.velocity_x
		boid.position_y = boid.position_y + boid.velocity_y

		
# view boids
		
positions_x = [boids[i].position_x for i in range(50)]
positions_y = [boids[i].position_y for i in range(50)]

figure=plt.figure()
axes=plt.axes(xlim=(-500,1500), ylim=(-500,1500))
scatter=axes.scatter(positions_x,positions_y)

def animate(frame):
   positions_x = [boids[i].position_x for i in range(50)]
   positions_y = [boids[i].position_y for i in range(50)]
   update_boids(boids)
   scatter.set_offsets(zip(positions_x,positions_y))


anim = animation.FuncAnimation(figure, animate,
                               frames=50, interval=50)

if __name__ == "__main__":
    plt.show()
