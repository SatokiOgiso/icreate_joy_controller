# icreate_joy_controller
Controll iRobot Create using joystick over ROS

## Environment

- iRobot Create
- ROS indigo
- /dev/ttyUSB* which is connected to the Create is accessible(r/w) from user.

## Dependencies

- joy
- create_node

if you have not installed them, please run 

```
sudo apt-get install ros-indigo-joy
sudo apt-get install ros-indigo-create-node
```

## Usage

The node joy_to_twist.py converts Joy topic to Twist topic.
It maps Joy.axes[1] and Joy.axes[2] to Twist.linear.x and Twist.angular.z

```
rosrun icreate_joy_controller joy_to_twist.py
```

If you use iRobot Create, you can also do the following.

```
# plug in iRobot Create and gamepad to your PC before.
sudo chmod 766 /dev/ttyUSB0 # the device which represents iRobot Create
roslaunch icreate_joy_controller create_joy_demo.launch
```

Then you can controll the robot using gamepad.

