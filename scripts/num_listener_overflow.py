#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback(error_msg):
    rospy.loginfo("I heard %s", error_msg.data)

rospy.init_node('num_listener_overflow')
rospy.Subscriber('num_topic_overflow', String, callback, queue_size=10)
rospy.spin()