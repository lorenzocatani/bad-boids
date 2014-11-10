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
# Deliberately terrible code for teaching purposes

#c=yaml.load(open("config.yaml"))

min_x = -450   
min_y = 300 
max_x = 50
max_y=600
min_vel_x = 0    
max_vel_x = 10
vel_y = 20 
attraction_index = 0.01  
speed_tuning_index = 0.125
separation1=100
separation2=10000
boids_num = 50

class boid(object):
 def __init__(self,x,y,xv,yv):
  self.position_x=x
  self.position_y=y
  self.velocity_x=xv
  self.velocity_y=yv
  
 def distance_square(self,other):
  d=(self.position_x - other.position_x)**2 + (self.position_y - other.position_y)**2
  return d
 
 def fly_towards_middle_x(self,other):
  separation=other.position_x - self.position_x
  self.velocity_x = self.velocity_x + (separation)*attraction_index/boids_num
  return self.velocity_x
 def fly_towards_middle_y(self,other):
  separation=other.position_y - self.position_y
  self.velocity_y = self.velocity_y + (separation)*attraction_index/boids_num
  return self.velocity_y
 
 def fly_away_from_neighbours_x(self,other):
  self.velocity_x = self.velocity_x + (self.position_x - other.position_x)
  return self.velocity_x
 def fly_away_from_neighbours_y(self,other):
  self.velocity_y = self.velocity_y + (self.position_y - other.position_y)
  return self.velocity_y
  
 def match_speed_neighbours_x(self,other):
  self.velocity_x = self.velocity_x +(other.velocity_x-self.velocity_x)*speed_tuning_index/boids_num
  return self.velocity_x 
 def match_speed_neighbours_y(self,other):
  self.velocity_y = self.velocity_y +(other.velocity_y-self.velocity_y)*speed_tuning_index/boids_num
  return self.velocity_y 
  
  
 
boids=[boid(random.uniform(min_x,max_x) ,random.uniform(min_y,max_y),
  random.uniform(min_vel_x,max_vel_x),random.uniform(-vel_y,vel_y)) for i in range(boids_num)]

 
 #replace global variable with function argument?
 #togliere i commenti??
 #gli ultimi due sulle classi
 #fai test
 
 
def update_boids(boids): 
	
	# Fly towards the middle
	for i in range(boids_num): #for boid in boids
		for j in range(boids_num):
		   boids[i].fly_towards_middle_x(boids[j])
		   boids[i].fly_towards_middle_y(boids[j])
		   
	# Fly away from nearby boids
	for i in range(boids_num):
		for j in range(boids_num):
		    if  boids[j].distance_square(boids[i]) < separation1:
		     boids[i].fly_away_from_neighbours_x(boids[j])
	             boids[i].fly_away_from_neighbours_y(boids[j])
				 
	# Try to match speed with nearby boids
	for i in range(boids_num):
		for j in range(boids_num):
			if boids[j].distance_square(boids[i]) < separation2:
			 boids[i].match_speed_neighbours_x(boids[j])
	                 boids[i].match_speed_neighbours_y(boids[j])
					 
	# Move according to velocities
	for i in range(boids_num):
		boids[i].position_x = boids[i].position_x + boids[i].velocity_x
		boids[i].position_y = boids[i].position_y + boids[i].velocity_y

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
