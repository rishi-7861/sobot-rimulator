#!/usr/bin/python
# -*- Encoding: utf-8 -*

from utils import linalg2_util as linalg
from pose import *

class ProximitySensor:

  def __init__( self, robot,          # robot this sensor is attached to
                      relative_pose,  # pose of this sensor relative to robot (NOTE: normalized on robot located at origin and with theta 0, i.e. facing east )
                      min_range,      # min sensor range (meters)
                      max_range,      # max sensor range (meters)
                      phi_view ):     # view angle of this sensor (rad from front of robot)
    
    # pose attributes
    self.robot = robot
    self.relative_pose = relative_pose
    self.pose = Pose( 0.0, 0.0, 0.0 ) # initialize pose object
    self.update_pose()                # determine initial global pose
    
    # sensitivity attributes
    self.min_range = min_range
    self.max_range = max_range
    self.phi_view = phi_view

  def update_pose( self ):
    # get the elements of the robot's pose
    robot_vect, robot_theta = self.robot.pose.split()

    # get the elements of this sensor's relative pose
    rel_vect, rel_theta = self.relative_pose.split()
    
    # construct this sensor's global pose
    global_vect_d = linalg.rotate_vector( rel_vect, robot_theta )
    global_vect = linalg.add( robot_vect, global_vect_d ) 
    global_theta = robot_theta + rel_theta

    self.pose.vupdate( global_vect, global_theta )
