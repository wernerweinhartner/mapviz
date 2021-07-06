#!/usr/bin/env python
import rospy
from nav_msgs.msg import Odometry


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

    new_message = Odometry()
    new_message.header=msg_header
    new_message.child_frame_id = "body"
    new_message.pose=msg_pose
    new_message.twist=msg_twist


    pub = rospy.Publisher('ins_converted', Odometry, queue_size=10)
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
    r=rospy.Rate(100)
    # publisher()