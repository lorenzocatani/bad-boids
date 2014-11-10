from boids import update_boids, boid
from nose.tools import assert_almost_equal,assert_equal
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
	        
	 
	 

def test_fly_towards_middle_x():
        boid1 = boid(2,5,7,9)
	boid2 = boid(3,4,7,2)  
	value = boid.fly_towards_middle_x(boid1,boid2)
	expected =7
	assert_almost_equal(value,expected,delta=0.01)
	
def test_fly_towards_middle_y():
        boid1 = boid(2,5,7,9)
	boid2 = boid(3,4,7,2)  
	value = boid.fly_towards_middle_y(boid1,boid2)
	expected =9
	assert_almost_equal(value,expected,delta=0.01)
	
def test_fly_away_from_neighbours_x():
        boid1 = boid(2,5,7,9)
	boid2 = boid(3,4,7,2)  
	value = boid.fly_away_from_neighbours_x(boid1,boid2)
	expected =6
	assert_equal(value,expected)
	
def test_fly_away_from_neighbours_y():
        boid1 = boid(2,5,7,9)
	boid2 = boid(3,4,7,2)  
	value = boid.fly_away_from_neighbours_y(boid1,boid2)
	expected =10
	assert_equal(value,expected)
	
def test_match_speed_neighbours_x():
        boid1 = boid(2,5,7,9)
	boid2 = boid(3,4,7,2)  
	value = boid.match_speed_neighbours_x(boid1,boid2)
	expected =7
	assert_almost_equal(value,expected,delta=0.01)
	
def test_match_speed_neighbours_y():
        boid1 = boid(2,5,7,5)
	boid2 = boid(3,2,7,2)  
	value = boid.match_speed_neighbours_y(boid1,boid2)
	expected =5
	assert_almost_equal(value,expected,delta=0.01)
	

	
