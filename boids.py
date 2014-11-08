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



def movement (a,b):       
 r = []
 for k in range(50):
  r.append(random.uniform(a,b)) 
 return r

min_x = -450
min_y = 300 
max = 50
min_vel_x = 0
max_vel_x = 10
vel_y=-20
vel_y=-20 
attraction_index = 0.01
speed_tuning_index = 0.125
separation1=100
separation2=10000

 
xs = movement(min_x,max) 
ys = movement(min_y,max)
xvs = movement(min_vel_x,max_vel_x)
yvs = movement(-vel_y,vel_y)
boids=(xs,ys,xvs,yvs)
#boids =["position_x":xs,"position_y":ys,"velocity_x":xvs,"velocity_y":yvs]

def distance(a,i,j):
 b = a[i]-a[j]
 return b 
 
def fly_towards_middle(a,b,i,j):
  b = a[i]+(distance(b,j,i))*attraction_index/len(xs)
  return b
  
def fly_away_from_neighbours(a,b,i,j):
  b = a[i]+(distance(b,j,i))
  return b
  
def match_speed_neighbours(a,i,j):
  b = a[i]+(distance(a,j,i))*speed_tuning_index/len(xs)
  return b
  
def distance_square(a,b,i,j):
  b = (a[j]-a[i])**2 + (b[j]-b[i])**2
  return b
 
  
 
def update_boids(boids):
	#xs,ys,xvs,yvs=boids
	# Fly towards the middle
	for i in range(len(xs)):
		for j in range(len(xs)):
			xvs[i]= fly_towards_middle(xvs,xs,i,j)
			yvs[i]= fly_towards_middle(yvs,ys,i,j)
	# Fly away from nearby boids
	for i in range(len(xs)):
		for j in range(len(xs)):
			if distance_square(xs,ys,i,j) < separation1:
			 xvs[i]= fly_away_from_neighbours(xvs,xs,i,j)
			 yvs[i]= fly_away_from_neighbours(yvs,ys,i,j)
	# Try to match speed with nearby boids
	for i in range(len(xs)):
		for j in range(len(xs)):
			if distance_square(xs,ys,i,j) < separation2:
			   xvs[i]= match_speed_neighbours(xvs,i,j)
			   yvs[i]= match_speed_neighbours(yvs,i,j)
	# Move according to velocities
	for i in range(len(xs)):
		xs[i]=xs[i]+xvs[i]
		ys[i]=ys[i]+yvs[i]


figure=plt.figure()
axes=plt.axes(xlim=(-500,1500), ylim=(-500,1500))
scatter=axes.scatter(boids[0],boids[1])

def animate(frame):
   update_boids(boids)
   scatter.set_offsets(zip(boids[0],boids[1]))


anim = animation.FuncAnimation(figure, animate,
                               frames=50, interval=50)

if __name__ == "__main__":
    plt.show()

