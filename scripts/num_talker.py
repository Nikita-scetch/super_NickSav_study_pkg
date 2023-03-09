#!/usr/bin/env python3
import rospy
from std_msgs.msg import UInt8
from std_msgs.msg import String

rospy.init_node('num_talker')
pub = rospy.Publisher('num_topic', UInt8, queue_size=10)
pub_overflow = rospy.Publisher('num_topic_overflow', String, queue_size=10)
rate = rospy.Rate(10)

def numbers():
    num_msg = UInt8()
    error_msg = String()
    error_msg.data = 'ERROR! Overflaw! n > 100!'
    num = 0

    while not rospy.is_shutdown():
        rospy.loginfo(num)
        num = num + 2

        if num > 100:
            pub_overflow.publish(error_msg)
            num = 0

        num_msg.data = num
        pub.publish(num_msg)

        rate.sleep()
        
try:
    numbers()
except (rospy.ROSInterruptException, KeyboardInterrupt):
    rospy.logerr('Exception catched')
