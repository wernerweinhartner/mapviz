#!/usr/bin/env python
from codecs import xmlcharrefreplace_errors
import rospy
from nav_msgs.msg import Odometry
from sensor_msgs.msg import NavSatFix, NavSatStatus

def callback(data):
    pose = data.pose
    twist = data.pose
    header = data.header
    frame_id = header.frame_id

    rospy.loginfo('frame id: {}' .format(frame_id))

def convert_msg(data):

    msg_pose = data.pose
    msg_twist = data.twist
    msg_header = data.header
    msg_frameid = data.child_frame_id

    pos = msg_pose.pose.position
    cov = msg_pose.covariance

    cov_convert = cov[:9]

    nav_sat_status = NavSatStatus()
    nav_sat_status.status = 1
    nav_sat_status.service = 1

    new_message = NavSatFix()
    new_message.header=msg_header
    new_message.status = nav_sat_status
    new_message.latitude = cov_convert[0]
    new_message.longitude = cov_convert[1]
    new_message.altitude = cov_convert[2]
    new_message.position_covariance = cov_convert

    pub = rospy.Publisher('navsat_converted', NavSatFix, queue_size=10)
    pub.publish(new_message)

    # rospy.loginfo('x: {}, y:{}, z:{},' .format(x,y, z))


def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('ins_new_node', anonymous=True)

    rospy.Subscriber("ins", Odometry, convert_msg)

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