"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

import matplotlib

matplotlib.use('TkAgg')

from matplotlib import pyplot as plt
from matplotlib import animation
import random

from numpy import array
# Deliberately terrible code for teaching purposes

min_x = -450   #configuration file for these constants?
min_y = 300 
max = 50
min_vel_x = 0    #replace global variable with function argument?
max_vel_x = 10
vel_y=-20
vel_y=-20 
attraction_index = 0.01  
speed_tuning_index = 0.125
separation1=100
separation2=10000

class boid(object):
 def __init__(self,x,y,xv,yv):
  self.position_x=x
  self.position_y=y
  self.velocity_x=xv
  self.velocity_y=yv

  
boids=[boid(random.uniform(min_x,max) ,random.uniform(min_y,max),
  random.uniform(min_vel_x,max_vel_x),random.uniform(-vel_y,vel_y)) for i in range(50)]

boids_num = len(boids)  
  
def distance(a,b):
 c = a-b
 return c
 
def fly_towards_middle(a,b,d):
  c = a+(distance(b,d))*attraction_index/boids_num
  return c
  
def fly_away_from_neighbours(a,b,d):
  c = a + distance(b,d)
  return c
  
def match_speed_neighbours(a,b):
  c = a +(distance(b,a))*speed_tuning_index/boids_num
  return c
  
def distance_square(a,b,d,e):
  c = (a-b)**2 + (d-e)**2
  return c
 
 #togliere i commenti??
 
def update_boids(boids): 
	
	# Fly towards the middle
	for i in range(boids_num):
		for j in range(boids_num):
		   boids[i].velocity_x = fly_towards_middle(boids[i].velocity_x,boids[j].position_x,boids[i].position_x)
		   boids[i].velocity_y = fly_towards_middle(boids[i].velocity_y,boids[j].position_y,boids[i].position_y)
	# Fly away from nearby boids
	for i in range(boids_num):
		for j in range(boids_num):
		    if distance_square(boids[j].position_x,boids[i].position_x,boids[j].position_y,boids[i].position_y) < separation1:
			boids[i].velocity_x = fly_away_from_neighbours(boids[i].velocity_x,boids[i].position_x,boids[j].position_x)
		        boids[i].velocity_y = fly_away_from_neighbours(boids[i].velocity_y,boids[i].position_y,boids[j].position_y)
	# Try to match speed with nearby boids
	for i in range(boids_num):
		for j in range(boids_num):
			if distance_square(boids[j].position_x,boids[i].position_x,boids[j].position_y,boids[i].position_y) < separation2:
			 boids[i].velocity_x = match_speed_neighbours(boids[i].velocity_x,boids[j].velocity_x)
		         boids[i].velocity_y = match_speed_neighbours(boids[i].velocity_y,boids[j].velocity_y)
	# Move according to velocities
	for i in range(len(boids)):
		boids[i].position_x =boids[i].position_x + boids[i].velocity_x
		boids[i].position_y =boids[i].position_y + boids[i].velocity_y

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
