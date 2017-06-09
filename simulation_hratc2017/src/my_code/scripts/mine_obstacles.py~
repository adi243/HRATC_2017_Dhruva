#!/usr/bin/env python
import rospy, math
from teb_local_planner.msg import ObstacleMsg
from geometry_msgs.msg import PolygonStamped, Point32, PoseStamped


class newobstacles():
	def __init__(self):

		rospy.init_node("publish_mine_obstacles")
	
	
		self.listener()    
	

	def publish_obstacle_msg(self,x,y):
		# Adjust the topic for navigation or remap
		pub = rospy.Publisher('/move_base/TebLocalPlannerROS/obstacles', ObstacleMsg, queue_size=1)

		# Create empty obstacle message that will be filled in afterwards
		obstacle_msg = ObstacleMsg() 
		obstacle_msg.header.stamp = rospy.Time.now()
		obstacle_msg.header.frame_id = "minefield" 
  
  		
  
		obstacle_msg.obstacles.append(PolygonStamped())
		v1 = Point32()
		v2 = Point32()
		v3 = Point32()
		v4 = Point32()
		if(x>=0 and y>=0):
			
			v1.x = x+0.2
			v1.y = y+0.2
			v2.x = x-0.2
			v2.y = y+0.2
			v3.x = x-0.2
			v3.y = y-0.2
			v4.x = x+0.2
			v4.y = y-0.2

		if(x>=0 and y<0):
			
			v1.x = x+0.2
			v1.y = -(abs(y)-0.2)
			v2.x = x-0.2
			v2.y = -(abs(y)-0.2)
			v3.x = x-0.2
			v3.y = -(abs(y)+0.2)
			v4.x = x+0.2
			v4.y = -(abs(y)+0.2)

		if(x<0 and y>=0):
			
			v1.x = -(abs(x)+0.2)
			v1.y = y-0.2
			v2.x = -(abs(x)-0.2)
			v2.y = y-0.2
			v3.x = -(abs(x)-0.2)
			v3.y = y+0.2
			v4.x = -(abs(x)+0.2)
			v4.y = y+0.2

		if(x<0 and y<0):
			
			v1.x = -(abs(x)+0.2)
			v1.y = -(abs(y)-0.2)
			v2.x = -(abs(x)-0.2)
			v2.y = -(abs(y)-0.2)
			v3.x = -(abs(x)-0.2)
			v3.y = -(abs(y)+0.2)
			v4.x = -(abs(x)+0.2)
			v4.y = -(abs(y)+0.2)

		


		obstacle_msg.obstacles[0].polygon.points = [v1, v2, v3, v4]
  

	
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


