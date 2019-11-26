#!/usr/bin/env python
 
import rospy                             #import required messages and libraries
from nav_msgs.msg import Odometry
import time




rospy.init_node('visual_odometry', anonymous=True)        #initialize node

publisher = rospy.Publisher("/mavros/odometry/out", Odometry, queue_size=10)  #create publisher


    

def callback(msg):					#define call back function, when there is data published on /odometry/odom the function will be called and processed data will be published 									on /mavros/odometry/out 
	odom = Odometry()
	odom.header.stamp=rospy.Time.now()
	odom.header.frame_id = "odom_ned"
        odom.child_frame_id = "base_link_frd"
        odom.pose=msg.pose
        odom.twist=msg.twist
        publisher.publish(odom)

while not rospy.is_shutdown():
	sub = rospy.Subscriber('/odometry/odom', Odometry, callback)    #create subscriber
        rospy.spin()
