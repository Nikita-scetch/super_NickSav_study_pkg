#!/usr/bin/env python3
import rospy
from std_msgs.msg import UInt8

def callback(msg):
    rospy.loginfo("I heard %s", msg.data)

rospy.init_node('num_listener')
rospy.Subscriber('num_topic', UInt8, callback, queue_size=10)
rospy.spin()
