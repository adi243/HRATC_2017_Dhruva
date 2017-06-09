#!/usr/bin/env python
import rospy, math
from teb_local_planner.msg import ObstacleMsg
from geometry_msgs.msg import PolygonStamped, Point32, PoseStamped
import numpy as np

## Code to create virtual obstacles around detected mines. Uses Teb Local Planner to create circular virtual objects over detected mines.

class newobstacles():
	def __init__(self):

		rospy.init_node("publish_mine_obstacles")
	
	
		self.listener()    
	

	def publish_obstacle_msg(self,x,y):
		## Adjust the topic for navigation or remap
		pub = rospy.Publisher('/move_base/TebLocalPlannerROS/obstacles', ObstacleMsg, queue_size=1)

		## Create empty obstacle message that will be filled in afterwards
		obstacle_msg = ObstacleMsg() 
		obstacle_msg.header.stamp = rospy.Time.now()
		obstacle_msg.header.frame_id = "minefield" 
  
  		
  
		obstacle_msg.obstacles.append(PolygonStamped())
		v1 = Point32()
		v2 = Point32()
		v3 = Point32()
		v4 = Point32()
		v5 = Point32()
		v6 = Point32()
		v7 = Point32()
		v8 = Point32()
		v9 = Point32()
		v10 = Point32()
		v11 = Point32()
		# v8 = Point32()
		# v7 = Point32()
		# if(x>=0 and y>=0):
			
		# 	v1.x = x+0.2
		# 	v1.y = y+0.2
		# 	v2.x = x-0.2
		# 	v2.y = y+0.2
		# 	v3.x = x-0.2
		# 	v3.y = y-0.2
		# 	v4.x = x+0.2
		# 	v4.y = y-0.2

		# if(x>=0 and y<0):
			
		# 	v1.x = x+0.2
		# 	v1.y = -(abs(y)-0.2)
		# 	v2.x = x-0.2
		# 	v2.y = -(abs(y)-0.2)
		# 	v3.x = x-0.2
		# 	v3.y = -(abs(y)+0.2)
		# 	v4.x = x+0.2
		# 	v4.y = -(abs(y)+0.2)

		# if(x<0 and y>=0):
			
		# 	v1.x = -(abs(x)+0.2)
		# 	v1.y = y-0.2
		# 	v2.x = -(abs(x)-0.2)
		# 	v2.y = y-0.2
		# 	v3.x = -(abs(x)-0.2)
		# 	v3.y = y+0.2
		# 	v4.x = -(abs(x)+0.2)
		# 	v4.y = y+0.2

		# if(x<0 and y<0):
		

		theta = np.linspace(0, 2*np.pi, 10)
		r = np.sqrt(0.05)
		x1 = r*np.cos(theta)
		y1 = r*np.sin(theta)
		h = [x,x,x,x,x,x,x,x,x,x]
		k = [y,y,y,y,y,y,y,y,y,y]
		cx=h-x1
		cy=k-y1
		print cx

		v1.x = cx[0]
		v1.y = cy[0]
		v2.x = cx[1]
		v2.y = cy[1]
		v3.x = cx[2]
		v3.y = cy[2]
		v4.x = cx[3]
		v4.y = cy[3]
		v5.x = cx[4]
		v5.y = cy[4]
		v6.x = cx[5]
		v6.y = cy[5]
		v7.x = cx[6]
		v7.y = cy[6]
		v8.x = cx[7]
		v8.y = cy[7]
		v9.x = cx[8]
		v9.y = cy[8]
		v10.x = cx[9]
		v10.y = cy[9]
	
		

		# v8.x = cx[7]
		# v8.y = cy[7]
		# v9.x = cx[8]
		# v9.y = cy[8]
		# v10.x = cx[9]
		# v10.y = cy[9]




		obstacle_msg.obstacles[0].polygon.points = [v1,v2,v3,v4,v5,v6,v7,v8,v9,v10]
 
  

	
		seconds = rospy.Duration(3)
 		now = rospy.Time.now()+seconds
		while rospy.Time.now()<now:
    
    			pub.publish(obstacle_msg)
    
    		

	def callback(self,data):

		a=data.pose.position.x
		b=data.pose.position.y
		self.publish_obstacle_msg(a,b)


	def listener(self):

    		rospy.Subscriber("/HRATC_FW/set_mine", PoseStamped, self.callback)
	
		rospy.spin()




if __name__ == '__main__':
	try:
		newobstacles()
	except rospy.ROSInterruptException:
		rospy.loginfo("Unable to Call Class")
		pass


