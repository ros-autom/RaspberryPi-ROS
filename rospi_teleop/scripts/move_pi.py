#!/usr/bin/env python
import sys, tty, termios, time  
from time import sleep
import pifacedigitalio as pfio  #Library for Pi-Face Digital Board (Only for us,you could use GPIO only)
from geometry_msgs.msg import Twist
import rospy
from std_msgs.msg import String

pfd = pfio.PiFaceDigital()    
pfio.init()


def mlfr():       #Motor left, move front
  pfio.digital_write(2,1)
  return;
def mrfr():       #Motor right, move front 
  pfio.digital_write(4,1)
  return;
def mlb():        #Motor left, move back
  pfio.digital_write(3,1)
  return;
def mrb():        #Motor right, move back
  pfio.digital_write(5,1)
  return;
def res():        #Reset all motor movements
  pfio.digital_write(2,0)
  pfio.digital_write(3,0)
  pfio.digital_write(4,0)
  pfio.digital_write(5,0)
  return;

move1=0
move2=0

dream=0.030      #Sleep time for restraint of movement, change this according to your communication latency

def callback(msg): 
        move1 = msg.linear.x;  #Read Twist data from ROS Twist teleoperation keyboard
        move2 = msg.angular.z;

	if(move1 > 0 and move2 == 0):
		mlfr()
		mrfr()
		sleep(dream)
		res()
		
	if(move1 < 0):
		mlb()
		mrb()
		sleep(dream)
		res()
	
	if(move1 > 0 and move2 > 0 ):
		mrfr()
		sleep(dream)
		res()
	
	if(move1 > 0 and move2 < 0):
		mlfr()
		sleep(dream)
		res()
	
        if(move1 ==0 and move2 < 0):
		print("\n Teleoperation Ended Successfully!") 
		pfio.init()
                rospy.signal_shutdown("Teleoperation ended remotely")
#Pressing "L" on Twist keyboard ends the teleoperation and shuts down the remote node.
	
def listener():

    rospy.init_node('move_pi')
    rospy.Subscriber('cmd_vel', Twist, callback)
    rospy.loginfo("Waiting for data...")
    rospy.spin()

if __name__ == '__main__':
    listener()

