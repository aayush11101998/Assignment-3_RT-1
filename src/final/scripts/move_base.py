#!/usr/bin/env python
from time import sleep
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import os
import time
import math
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist, Point
from nav_msgs.msg import Odometry
from tf import transformations


def movebase():
    
    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    
    # defining initial position of robot
    position = rospy.wait_for_message("/odom",Odometry)
    xr = position.twist.twist.linear.x
    yr = position.twist.twist.linear.y
    print("value of initial robot x_position:", xr)
    print("value of initial robot x_position:", yr)
    # Creates a new goal 
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    # goal position asked from user
    x = float(input("Enter goal position x: "))
    goal.target_pose.pose.position.x = x
    y = float(input("Enter goal y position: "))
    goal.target_pose.pose.position.y = y
    goal.target_pose.pose.orientation.w = 1.0
    
    dist = ((x-xr)**2 + (y-yr)**2)**0.5 
    print("distance left =", dist)
    #waits for the server to listen for goals
    client.wait_for_server()
    #sends the goal to action server
    client.send_goal(goal)
    
    print("wait for the robot to reach to your given position")
    result = client.wait_for_result(timeout = rospy.Duration(30))
    print ("give new coordinates for the robot")
    
    
    
def main():
    
    rospy.init_node('move_base')
    rospy.set_param('robot_state','0')
    rate = rospy.Rate(20)
   
    while not rospy.is_shutdown():
         if rospy.get_param('robot_state')=='s':
             movebase()
         else:
             rate.sleep()
             continue
         rate.sleep()
if __name__ == '__main__':
    main()
            



            

