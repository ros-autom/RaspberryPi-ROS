At first, you must install ROS Kinetic on your Raspberry Pi, following this [documentation](http://wiki.ros.org/kinetic/Installation/Ubuntu "documentation").

After you are finished, make sure your controlling computer is connected to the same network that the RaspberryPi is.
Then you must edit the hosts file of **each** machine, so they can communicate with each other with hostnames linking to IPs.
To edit the hosts file, run this command:
````
sudo nano /etc/hosts
````
Make sure you place the correct addresses and hostnames, according to this formation:
````
192.168.0.100 mypc
192.168.0.101 raspberrypi
````
Then hit Ctrl+X, press "y" to save, and Enter.

After that, the Raspberry Pi must be able to "see" the PC as a master. To accomplish that, in the Raspberry Pi you must run this command:
````
export ROS_MASTER_URI=http://mypc:11311/
````
in order to be able to accept the controlling computer as the ROS Master.
You can confirm that, by opening a terminal in the controlling PC, and typing:
````
roscore
````
and then, running on the Raspberry Pi this command:
````
rosnode list
````
you should be able to "see" the running nodes, on the Master. The output should be:
````
/rosout
````
When this is confirmed, you can proceed with the installation of the Twist Teleoperation Keyboard:
````
sudo apt-get install ros-kinetic-teleop-twist-keyboard
````
and run it:
````
rosrun teleop_twist_keyboard teleop_twist_keyboard.py
````
Following the on-screen instructions, you can send commands to control the Raspberry Pi.
The Raspberry Pi must "listen" to them, and do something, so you must run:
````
rosrun rospi_teleop move_pi.py
````
after you edit your move_pi.py accordingly, to match your motor control pins and preferences.
