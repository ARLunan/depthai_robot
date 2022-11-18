depthai Launch and configuration Packages for publishing depthai Camera rgb and pointcloud image msg data generated on a Robot SBC

Visit Depthai ROS Github for details https://github.com/luxonis/depthai-ros


This main branch supports ROS2 Humble ros-base sudo apt install ros-humble-ros-base on a Raspberry Pi Ubuntu 22.04 Server or lightweight desktop such as Ubuntu Mate,  with an OAK-D-Lite connected, to a USB3-A port with a USB-C Power Splitter.

If Installed from ros binaries, add USB rules to your system

echo 'SUBSYSTEM=="usb", ATTRS{idVendor}=="03e7", MODE="0666"' | sudo tee /etc/udev/rules.d/80-movidius.rules
sudo udevadm control --reload-rules && sudo udevadm trigger

Install depthai-ros. (Available for Noetic, foxy, galactic and humble) 
    sudo apt install ros-humble-depthai-ros
    
This repository adds specfic launch files to publish message pointcloud2 and laserscan data to be displayed on the rviz display package installed on a Ubuntu 22.04 Desktop and ros Desktop or Desktop Full. (sudo apt install ros-humble-desktop or sudo apt install ros-humble-desktop_full)

Robot launch files (Repository ARLunan/depthai_robot) sets parameters to non-default enableRviz=False and camera_model="OAK-D-LITE" values.

Desktop launch files (Repository ARLunan/depthai_desktop) runs the Rviz ROS Display package specfically configured to display sensor_msg/pointcloud2 and sensor_msg/msg/LaserScan messages
