from boids import update_boids
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
    update_boids(new_boid_data_aft)
    
    for after,before in zip(regression_data["after"],boid_data):
        for after_value,before_value in zip(after,before): 
            assert_almost_equal(after_value,before_value,delta=0.01)
	

	
