Mapviz [![Build Status](https://travis-ci.org/swri-robotics/mapviz.svg?branch=master)](https://travis-ci.org/swri-robotics/mapviz)
======

Mapviz is a [ROS](http://www.ros.org/) based visualization tool with a plug-in system similar to [RVIZ](http://wiki.ros.org/rviz) focused on visualizing 2D data.

![](https://github.com/swri-robotics/mapviz/wiki/mapviz.png)

Usage
-----

[View the documentation](https://swri-robotics.github.io/mapviz/) for usage information.
https://github.com/danielsnider/MapViz-Tile-Map-Google-Maps-Satellite
http://docs.ros.org/en/noetic/api/nav_msgs/html/msg/Odometry.html
http://docs.ros.org/en/kinetic/api/gps_common/html/msg/GPSFix.html
http://docs.ros.org/en/melodic/api/inertial_sense/html/msg/GPS.html

Change this later into nicer words lol

In all separate termials, run:

`cd ~/catkin_ws`
`
catkin_make`

`roscore`

Runs the docker and the server

`sudo docker run -p 8080:8080 -d -t -v ~/mapproxy:/mapproxy danielsnider/mapproxy`

Runs the IMU

`rosrun inertial_sense_ros inertial_sense_node`

Run the python / listener file that I created

`rosrun mapviz listener_gps.py`

If it says that it's not an executable, or can't be found, do (in the right file folder):

`chmod +x listener_gps.py`

Echo the topic that I publish to, make sure that messages get sent

`rostopic echo gps_converted`

Run MapViz

`roslaunch mapviz mapviz.launch`

Make sure that it's map and map for the fixed frame and the other frame

Do all the instructions in the Google Maps Offline capability github mentioned above

Then click 'Add'
Select 'gps' in the pop-up, and click OK.
Then, in the Topic, select 'gps_converted'.
--> Mapviz will only show topics that are compatible to be interpreted (they must be the same message type).
Click OK on selected topic.
There should be no errors when it runs --> should just say status is OK.

Make sure that the gps is below the tile_map, since the order matters. It will draw from top to bottom
