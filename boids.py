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

 
x =random.uniform(min_x,max) 
y = random.uniform(min_y,max)
xv = random.uniform(min_vel_x,max_vel_x)
yv = random.uniform(-vel_y,vel_y)
#boids=(xs,ys,xvs,yvs)

#class boids (object):
# def __init__(self,x,y,xv,yv)
boids=[{"position_x":x,"position_y":y,"velocity_x":xv,"velocity_y":yv} for i in range(50)]

def distance(a,i,j):
 b = a[i]-a[j]
 return b 
 
def fly_towards_middle(a,b,i,j):
  b = a[i]+(distance(b,j,i))*attraction_index/len(x)
  return b
  
def fly_away_from_neighbours(a,b,i,j):
  b = a[i]+(distance(b,j,i))
  return b
  
def match_speed_neighbours(a,i,j):
  b = a[i]+(distance(a,j,i))*speed_tuning_index/len(x)
  return b
  
def distance_square(a,b,i,j):
  b = (a[j]-a[i])**2 + (b[j]-b[i])**2
  return b
 
  
 
def update_boids(boids):
	#xs,ys,xvs,yvs=boids
	# Fly towards the middle
	for i in range(len(x)):
		for j in range(len(x)):
			xv[i]= fly_towards_middle(xv,x,i,j)
			yv[i]= fly_towards_middle(yv,y,i,j)
	# Fly away from nearby boids
	for i in range(len(x)):
		for j in range(len(x)):
			if distance_square(x,y,i,j) < separation1:
			 xv[i]= fly_away_from_neighbours(xv,x,i,j)
			 yv[i]= fly_away_from_neighbours(yv,y,i,j)
	# Try to match speed with nearby boids
	for i in range(len(x)):
		for j in range(len(x)):
			if distance_square(x,y,i,j) < separation2:
			   xv[i]= match_speed_neighbours(xv,i,j)
			   yv[i]= match_speed_neighbours(yv,i,j)
	# Move according to velocities
	for i in range(len(x)):
		x[i]=x[i]+xv[i]
		y[i]=y[i]+yv[i]


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

