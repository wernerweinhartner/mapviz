#!/usr/bin/env python
import rospy
from inertial_sense_ros.msg import GPS
import gps_common.msg

def callback(data):
    x=data.latitude
    y=data.longitude
    z=data.altitude

    # rospy.loginfo('x: {}, y:{}, z:{},' .format(x,y, z))

def convert_msg(data):

    x=data.latitude
    y=data.longitude
    z=data.altitude


    new_message = gps_common.msg.GPSFix()
    new_message.latitude=data.latitude
    new_message.longitude=data.longitude
    new_message.altitude=data.altitude


    pub = rospy.Publisher('gps_converted', gps_common.msg.GPSFix, queue_size=10)
    pub.publish(new_message)

    # rospy.loginfo('x: {}, y:{}, z:{},' .format(x,y, z))


def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('gps_new_node', anonymous=True)

    rospy.Subscriber("gps", GPS, convert_msg)

    # spin() simply keeps python from exiting until this node is stopped
    # rospy.spin()

# def publisher():
    # pub = rospy.Publisher('gps_converted', gps_common.msg.GPSFix, queue_size=10)
    # pub.publish(new_message)
    # rospy.init_node('node_name')
    # r = rospy.Rate(10) # 10hz

# if __name__ == '__main__':
while not rospy.is_shutdown():
    listener()
    r=rospy.Rate(0.00000001)
    # publisher()