# assignment-3_Research_Track-1

##ABSTRACT
This assignment is a robotic simulation on Gazebo and Rviz with our robot being controlled in different ways in the given environment.

##INTRODUCTION
A software architecture to control the robot is being programmed. User can control the robot with three possible ways.
1. Use keyboard keys.
2. Use keyboard keys with obstacle avoidance assistance.
3. Move the robot autonomously just give the coordinate points.

To know more on the operational features of the above three methods refer the sections below.

##INSTALLATION & RUNNING

Create a package using: 

$ mkdir -p catkin_ws/src
$ cd catkin_make
$ git clone https://github.com/aayush11101998/Assignment-3_RT-1.git
$ cd ..

now put "$ source /opt/ros/noetic/setup.bash" in your ".bashrc" file.

The following commands add the above created package into ROS environment :
 
$ catkin_make
and put "$ source catkin_ws/devel/setup.bash" in .bashrc file.

also install the slam_gmapping package in your workspace. Once installed make sure everything is included inside your workspace by using the command:

$ catkin_make

Now open three terminals and run the commands 

1. roslaunch final_assignment simulation_gmapping.launch 
2. roslaunch final_assignment move_base.launch 
3. roslaunch final_assignment main_launch.launch 

The first command opens Gazebo and Rviz with the given map loaded in it given to us for the assignment.
The second command opens the movebase package which is described in the [link](http://wiki.ros.org/move_base).
The third commands runs the programs which are located in the script subfolder of the package. They give user the chance to use the modalities as per his choice, just press "w,s,d" to use them.

if in case user wants to use another modality he/she needs to press ctrl-c and select the modality of his/her choice. For switching to the option of using keyboard from autonomous motion of robot the user should rewrite the third command after pressing ctrl-c.


##  OPERATIONAL FEATURES

# 1. FOR TELEOP_KEYBOARD.
we use the keys "u","i","o","j","k","l","m",",","." 
"u" makes the robot to turn left while moving forward, "i" makes the robot move forward in a straight line, "o" makes the robot turn right while moving forward.
"j" makes robot turn left "k" stops the moving robot and "l" makes the robot turn right.
"m" makes the robot turn left while moving backwards, "," makes the robot go back in a straight line and "." make the robot turn right while going backwards. 
Keys "q" "w" "e" "z" "x" "c" are used to increase and decrease the speed of robot moving forward turning lewft and right.
 
# 2. OBSTACLE AVOIDANCE USING TELEOP.
User chosing this modality can still use the teleop keys that are mentioned above but now the robot stops when it comes close to the obstacles in order to avoid collision.

# 3. AUTONOMOUS ROBOT REACHING THE TARGET POINTS DESCRIBED BY THE USER.
User is asked to give coordinates of x and y where the robot must go the points however they should lie within the map once points are defined the robot autonomously tries to reach to the given coordinates.

## METHODOLOGY

I used three different code structures to define the above modalities:

1. Assignment3.py
2. Move_base.py
3. teleop_keyboard.py

# Assignment3.py:

This program is used to activate the other two programs that contains the control modalities of the robot I used the " $ rospy.set_ param" command to set parameters to store the string values which actives the robot state when i use the "rospy.get_param" ultimately resulting in the activation of modalities.

# move_base.py

This program works using the action server/client. I activate the necessary topics needed for the program to work smoothly using SimpleActionClient. This enables commands like MoveBaseGoal() used to define the goal, send_ goal() used to send goal to server etc.
Once the user press "s" this program is activated else not, it asks user to define the coordinates which are defined as goal. It then waits for the server to listen to the goals and once the server is ready it sends the goal which in turn makes the robot move in the direction of the goal. I also defined the initial distance that robot need to cover and the initial position of the robot as well. 

# teleop_keyboard.py

Most of the code is taken from another github code but using the set_param and get_param commands in main() I enabled the remaining modalities that the user can use to control robot. Since we are using obstacle avoidance I used the laserscan msgs and devided the given data into three parts which scan the three regions of the robot namely left right and center. For the obstacle avoidance part whenever one part of the laserscan data shows less values then a predefined value our robot detects obstacles and immediately stops as i made its velocity in that direction 0, forcing the user to use another key to move the robot. With the use of publish subscribe, the publish can be regarded as a speaker which tells some information that subscriber regarded as listener grabs and works upon accordingly.

## SOFTWARE ARCHITECTURE

put image here.

