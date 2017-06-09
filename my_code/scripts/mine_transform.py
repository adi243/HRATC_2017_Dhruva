#!/usr/bin/env python  
import roslib
import rospy
import math
import tf
import time
import numpy as np
import geometry_msgs.msg
from metal_detector_msgs.msg._Coil import Coil
from std_msgs.msg import Float32
from std_msgs.msg import String
from std_msgs.msg import Bool
from geometry_msgs.msg import Twist, Pose, PoseStamped, PoseWithCovariance, PoseWithCovarianceStamped
a=0
b=0

## Code to Detect Mines. Reads the coil signals and when the coils strike 1, a mine is detected.

def callback(data):
		global a
		global b
		dtd_mine  = rospy.Publisher('/HRATC_FW/set_mine', PoseStamped, queue_size=1) # Publisher for Judge
		#dyn_mine  = rospy.Publisher('/dynamic_obstacles', PoseStamped, queue_size=1)
		mineposition=PoseStamped()		
		leftCoil=data.left_coil 
		# now=data.header.stamp
		rightCoil=data.right_coil 
		if (leftCoil==1):
		
			
	
			try:			
				
	
				(trans1,rot1) = listener.lookupTransform('/minefield', '/left_coil', rospy.Time(0))
				x1=trans1[0]   
				y1=trans1[1]    
				z1=trans1[2]    
				c=abs(x1)-abs(a)
				d=abs(y1)-abs(b)         
				mineposition.pose.position.x=x1    
				mineposition.pose.position.y=y1    
				mineposition.pose.position.z=z1
				if(abs(c)>=0.6 or abs(d)>=0.6):
					dtd_mine.publish(mineposition)
					#dyn_mine.publish(mineposition)
					print x1,y1,z1
					a=x1
					b=y1


					

			except: pass   

		if (rightCoil==1):
	
		

			try:			
				
				
				(trans2,rot2) = listener.lookupTransform('/minefield', '/right_coil', rospy.Time(0))
				x2=trans2[0]   
				y2=trans2[1]    
				z2=trans2[2]    
				c=abs(x2)-abs(a)
				d=abs(y2)-abs(b)          
				
				mineposition.pose.position.x=x2    
				mineposition.pose.position.y=y2    
				mineposition.pose.position.z=z2
				if(abs(c)>=0.6 or abs(d)>=0.6):
					dtd_mine.publish(mineposition)
					#dyn_mine.publish(mineposition)
					print x2,y2,z2
					a=x2
					b=y2
					

			except: pass   
	
		if (leftCoil==1 and rightCoil==1):
		
	
			try:			
				
				
				(trans3,rot3) = listener.lookupTransform('/minefield', '/right_coil', rospy.Time(0))
				(trans4,rot4) = listener.lookupTransform('/minefield', '/left_coil', rospy.Time(0))
				x3=trans3[0]   
				y3=trans3[1]    
				z3=trans3[2]
				
				x4=trans4[0]   
				y4=trans4[1]    
				z4=trans4[2]  
			  	c=abs((x3+x4)/2)-abs(a)
				d=abs((y3+y4)/2)-abs(b)
				mineposition.pose.position.x=(x3+x4)/2    
				mineposition.pose.position.y=(y3+y4)/2    
				mineposition.pose.position.z=(z3+z4)/2
				if(abs(c)>=0.6 or abs(d)>=0.6):
					dtd_mine.publish(mineposition)
					#dyn_mine.publish(mineposition)
					print x3,y3,z3,x4,y4,z4
					a=(x3+x4)/2
					b=(y3+y4)/2

					
			except: pass    
		
		
		
	
def sub():

	rospy.Subscriber("/coils",Coil,callback) ## Subscribe from Coils
	
	rospy.spin()


	

if __name__ == '__main__':
	rospy.init_node('mine_detection')##initializing node
	listener = tf.TransformListener()
	sub()
