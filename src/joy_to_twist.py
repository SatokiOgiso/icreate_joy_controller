#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy

vel = Twist()

def callback(message):
    print message.axes
    print 'straight'
    print message.axes[1]
    print 'turn'
    print message.axes[2]
    global vel
    vel = Twist()
    vel.linear.x = message.axes[1]
    vel.angular.z = message.axes[2]

rospy.init_node('joy_to_twist')
pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
sub = rospy.Subscriber('joy', Joy, callback)
rate = rospy.Rate(10)

while not rospy.is_shutdown():
    pub.publish(vel)
    rate.sleep()
