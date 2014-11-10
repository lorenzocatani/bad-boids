from boids import update_boids, boid
from nose.tools import assert_almost_equal
import os
import yaml

def test_bad_boids_regression():
    regression_data=yaml.load(open(os.path.join(os.path.dirname(__file__),'fixture.yml')))
	
    boid_data_bef=regression_data["before"]
    new_boid_data_bef =[boid(boid_data_bef[0][i],boid_data_bef[1][i],boid_data_bef[2][i],boid_data_bef[3][i]) for i in range(50)]
    update_boids(new_boid_data_bef)
	
    boid_data_aft=regression_data["after"]
    new_boid_data_aft =[boid(boid_data_aft[0][i],boid_data_aft[1][i],boid_data_aft[2][i],boid_data_aft[3][i]) for i in range(50)]
    
    for i in range(50):
            assert_almost_equal(new_boid_data_aft[i].position_x,new_boid_data_bef[i].position_x,delta=0.01)
	    assert_almost_equal(new_boid_data_aft[i].position_y,new_boid_data_bef[i].position_y,delta=0.01)
	    assert_almost_equal(new_boid_data_aft[i].velocity_x,new_boid_data_bef[i].velocity_x,delta=0.01)
	    assert_almost_equal(new_boid_data_aft[i].velocity_y,new_boid_data_bef[i].velocity_y,delta=0.01)
	        
	  
	  
	  #for j in range(4):
	  #for after,before in zip(new_boid_data_aft[i][0],new_boid_data_bef[i][0]):
             #for after_value,before_value in zip(after,before): 
               # assert_almost_equal(after_value,before_value,delta=0.01)
	

	
