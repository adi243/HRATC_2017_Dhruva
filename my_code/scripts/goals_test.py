#!/usr/bin/env python


import rospy
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import actionlib
from actionlib_msgs.msg import *
from visualization_msgs.msg import Marker
from visualization_msgs.msg import MarkerArray
from geometry_msgs.msg import Quaternion
import tf

## This script creates the pattern used by the robot to explore the arena. We use loops with move_base goals to achieve patterns.

class newgoals():
    def __init__(self):
	rospy.init_node('nav_commands')
	rospy.sleep(2)	
	rospy.on_shutdown(self.shutdown) ## Dealing with Failure
	self.move_base = actionlib.SimpleActionClient("move_base", MoveBaseAction) ## Creation of move_base client
	rospy.loginfo("Waiting for the action server to come up")
	a=0
	self.move_base.wait_for_server(rospy.Duration(6))
	goal = MoveBaseGoal()
	goal.target_pose.header.frame_id = 'minefield'
	goal.target_pose.header.stamp = rospy.Time.now()
	
## Dealing with Center Line

	goal.target_pose.pose.position.x = 10.7# Extreme of Arena
	goal.target_pose.pose.position.y = 0
	goal.target_pose.pose.position.z = 0
	goal.target_pose.pose.orientation = Quaternion(*tf.transformations.quaternion_from_euler(0, 0, 0))

	
	self.move_base.send_goal(goal)


	success = self.move_base.wait_for_result(rospy.Duration(90)) 


	if not success:
		self.move_base.cancel_goal()
		rospy.loginfo("The rover failed to reach the goal")
	else:
		state = self.move_base.get_state()
		if state == GoalStatus.SUCCEEDED:
			rospy.loginfo("Goal Reached")



	goal.target_pose.pose.position.x = 10.7
	goal.target_pose.pose.position.y = 0
	goal.target_pose.pose.position.z = 0
	goal.target_pose.pose.orientation = Quaternion(*tf.transformations.quaternion_from_euler(0, 0, 1.57))

	
	self.move_base.send_goal(goal)


	success = self.move_base.wait_for_result(rospy.Duration(15)) 


	if not success:
		self.move_base.cancel_goal()
		rospy.loginfo("The rover failed to reach the goal")
	else:
		state = self.move_base.get_state()
		if state == GoalStatus.SUCCEEDED:
			rospy.loginfo("Goal Reached")

## Loop Here

	while a<=1.5:
		goal.target_pose.pose.position.x = 10.7
		goal.target_pose.pose.position.y = a+0.5
		goal.target_pose.pose.position.z = 0
		goal.target_pose.pose.orientation = Quaternion(*tf.transformations.quaternion_from_euler(0, 0, 1.57))

	
		self.move_base.send_goal(goal)


		success = self.move_base.wait_for_result(rospy.Duration(30)) 


		if not success:
			self.move_base.cancel_goal()
			rospy.loginfo("The rover failed to reach the goal")
		else:
			state = self.move_base.get_state()
			if state == GoalStatus.SUCCEEDED:
				rospy.loginfo("Goal Reached")

	    	goal.target_pose.pose.position.x = 10.7
		goal.target_pose.pose.position.y = a+0.5
		goal.target_pose.pose.position.z = 0
		goal.target_pose.pose.orientation = Quaternion(*tf.transformations.quaternion_from_euler(0, 0, 3.14))

	
		self.move_base.send_goal(goal)


		success = self.move_base.wait_for_result(rospy.Duration(15)) 


		if not success:
			self.move_base.cancel_goal()
			rospy.loginfo("The rover failed to reach the goal")
		else:
			state = self.move_base.get_state()
			if state == GoalStatus.SUCCEEDED:
				rospy.loginfo("Goal Reached")

		goal.target_pose.pose.position.x = -10.8 # Extreme of arena
		goal.target_pose.pose.position.y = a+0.5
		goal.target_pose.pose.position.z = 0
		goal.target_pose.pose.orientation = Quaternion(*tf.transformations.quaternion_from_euler(0, 0, 3.14))

	
		self.move_base.send_goal(goal)


		success = self.move_base.wait_for_result(rospy.Duration(90)) 


		if not success:
			self.move_base.cancel_goal()
			rospy.loginfo("The rover failed to reach the goal")
		else:
			state = self.move_base.get_state()
			if state == GoalStatus.SUCCEEDED:
				rospy.loginfo("Goal Reached")

		goal.target_pose.pose.position.x = -10.8
		goal.target_pose.pose.position.y = a+0.5
		goal.target_pose.pose.position.z = 0
		goal.target_pose.pose.orientation = Quaternion(*tf.transformations.quaternion_from_euler(0, 0, 4.71))

	
		self.move_base.send_goal(goal)


		success = self.move_base.wait_for_result(rospy.Duration(15)) 


		if not success:
			self.move_base.cancel_goal()
			rospy.loginfo("The rover failed to reach the goal")
		else:
			state = self.move_base.get_state()
			if state == GoalStatus.SUCCEEDED:
				rospy.loginfo("Goal Reached")

		goal.target_pose.pose.position.x = -10.8
		goal.target_pose.pose.position.y = -(a+0.5)
		goal.target_pose.pose.position.z = 0
		goal.target_pose.pose.orientation = Quaternion(*tf.transformations.quaternion_from_euler(0, 0, 4.71))

	
		self.move_base.send_goal(goal)


		success = self.move_base.wait_for_result(rospy.Duration(30)) 


		if not success:
			self.move_base.cancel_goal()
			rospy.loginfo("The rover failed to reach the goal")
		else:
			state = self.move_base.get_state()
			if state == GoalStatus.SUCCEEDED:
				rospy.loginfo("Goal Reached")

		goal.target_pose.pose.position.x = -10.8
		goal.target_pose.pose.position.y = -(a+0.5)
		goal.target_pose.pose.position.z = 0
		goal.target_pose.pose.orientation = Quaternion(*tf.transformations.quaternion_from_euler(0, 0, 0))

	
		self.move_base.send_goal(goal)


		success = self.move_base.wait_for_result(rospy.Duration(15)) 


		if not success:
			self.move_base.cancel_goal()
			rospy.loginfo("The rover failed to reach the goal")
		else:
			state = self.move_base.get_state()
			if state == GoalStatus.SUCCEEDED:
				rospy.loginfo("Goal Reached")

		goal.target_pose.pose.position.x = 10.7# Change to 10.4 in Test Code
		goal.target_pose.pose.position.y = -(a+0.5)
		goal.target_pose.pose.position.z = 0
		goal.target_pose.pose.orientation = Quaternion(*tf.transformations.quaternion_from_euler(0, 0, 0))

	
		self.move_base.send_goal(goal)


		success = self.move_base.wait_for_result(rospy.Duration(90)) 


		if not success:
			self.move_base.cancel_goal()
			rospy.loginfo("The rover failed to reach the goal")
		else:
			state = self.move_base.get_state()
			if state == GoalStatus.SUCCEEDED:
				rospy.loginfo("Goal Reached")
	
		goal.target_pose.pose.position.x = 10.7# Change to 10.4 in Test Code
		goal.target_pose.pose.position.y = -(a+0.5)
		goal.target_pose.pose.position.z = 0
		goal.target_pose.pose.orientation = Quaternion(*tf.transformations.quaternion_from_euler(0, 0, 1.57))

	
		self.move_base.send_goal(goal)


		success = self.move_base.wait_for_result(rospy.Duration(15)) 


		if not success:
			self.move_base.cancel_goal()
			rospy.loginfo("The rover failed to reach the goal")
		else:
			state = self.move_base.get_state()
			if state == GoalStatus.SUCCEEDED:
				rospy.loginfo("Goal Reached")
		a+=0.5

	b=4
	while b>1.5:    
		goal.target_pose.pose.position.x = 10.9# Change to 10.4 in Test Code
		goal.target_pose.pose.position.y = b
		goal.target_pose.pose.position.z = 0
		goal.target_pose.pose.orientation = Quaternion(*tf.transformations.quaternion_from_euler(0, 0, 1.57))

	
		self.move_base.send_goal(goal)


		success = self.move_base.wait_for_result(rospy.Duration(30)) 


		if not success:
			self.move_base.cancel_goal()
			rospy.loginfo("The rover failed to reach the goal")
		else:
			state = self.move_base.get_state()
			if state == GoalStatus.SUCCEEDED:
				rospy.loginfo("Goal Reached")


		goal.target_pose.pose.position.x = 10.9# Change to 10.4 in Test Code
		goal.target_pose.pose.position.y = b
		goal.target_pose.pose.position.z = 0
		goal.target_pose.pose.orientation = Quaternion(*tf.transformations.quaternion_from_euler(0, 0, 3.14))

	
		self.move_base.send_goal(goal)


		success = self.move_base.wait_for_result(rospy.Duration(15)) 


		if not success:
			self.move_base.cancel_goal()
			rospy.loginfo("The rover failed to reach the goal")
		else:
			state = self.move_base.get_state()
			if state == GoalStatus.SUCCEEDED:
				rospy.loginfo("Goal Reached")


		goal.target_pose.pose.position.x = -10.9
		goal.target_pose.pose.position.y = b
		goal.target_pose.pose.position.z = 0
		goal.target_pose.pose.orientation = Quaternion(*tf.transformations.quaternion_from_euler(0, 0, 3.14))

	
		self.move_base.send_goal(goal)


		success = self.move_base.wait_for_result(rospy.Duration(90)) 


		if not success:
			self.move_base.cancel_goal()
			rospy.loginfo("The rover failed to reach the goal")
		else:
			state = self.move_base.get_state()
			if state == GoalStatus.SUCCEEDED:
				rospy.loginfo("Goal Reached")


		goal.target_pose.pose.position.x = -10.9
		goal.target_pose.pose.position.y = b
		goal.target_pose.pose.position.z = 0
		goal.target_pose.pose.orientation = Quaternion(*tf.transformations.quaternion_from_euler(0, 0, 4.71))

	
		self.move_base.send_goal(goal)


		success = self.move_base.wait_for_result(rospy.Duration(15)) 


		if not success:
			self.move_base.cancel_goal()
			rospy.loginfo("The rover failed to reach the goal")
		else:
			state = self.move_base.get_state()
			if state == GoalStatus.SUCCEEDED:
				rospy.loginfo("Goal Reached")

		goal.target_pose.pose.position.x = -10.9
		goal.target_pose.pose.position.y = a
		goal.target_pose.pose.position.z = 0
		goal.target_pose.pose.orientation = Quaternion(*tf.transformations.quaternion_from_euler(0, 0, 4.71))

	
		self.move_base.send_goal(goal)


		success = self.move_base.wait_for_result(rospy.Duration(30)) 


		if not success:
			self.move_base.cancel_goal()
			rospy.loginfo("The rover failed to reach the goal")
		else:
			state = self.move_base.get_state()
			if state == GoalStatus.SUCCEEDED:
				rospy.loginfo("Goal Reached")

		goal.target_pose.pose.position.x = -10.9
		goal.target_pose.pose.position.y = a
		goal.target_pose.pose.position.z = 0
		goal.target_pose.pose.orientation = Quaternion(*tf.transformations.quaternion_from_euler(0, 0, 0))

	
		self.move_base.send_goal(goal)


		success = self.move_base.wait_for_result(rospy.Duration(15)) 


		if not success:
			self.move_base.cancel_goal()
			rospy.loginfo("The rover failed to reach the goal")
		else:
			state = self.move_base.get_state()
			if state == GoalStatus.SUCCEEDED:
				rospy.loginfo("Goal Reached")

		goal.target_pose.pose.position.x = 10.9
		goal.target_pose.pose.position.y = a
		goal.target_pose.pose.position.z = 0
		goal.target_pose.pose.orientation = Quaternion(*tf.transformations.quaternion_from_euler(0, 0, 0))

	
		self.move_base.send_goal(goal)


		success = self.move_base.wait_for_result(rospy.Duration(90)) 


		if not success:
			self.move_base.cancel_goal()
			rospy.loginfo("The rover failed to reach the goal")
		else:
			state = self.move_base.get_state()
			if state == GoalStatus.SUCCEEDED:
				rospy.loginfo("Goal Reached")

		
		goal.target_pose.pose.position.x = 10.9
		goal.target_pose.pose.position.y = a
		goal.target_pose.pose.position.z = 0
		goal.target_pose.pose.orientation = Quaternion(*tf.transformations.quaternion_from_euler(0, 0, 1.57))

	
		self.move_base.send_goal(goal)


		success = self.move_base.wait_for_result(rospy.Duration(15)) 


		if not success:
			self.move_base.cancel_goal()
			rospy.loginfo("The rover failed to reach the goal")
		else:
			state = self.move_base.get_state()
			if state == GoalStatus.SUCCEEDED:
				rospy.loginfo("Goal Reached")
		

		b-=0.5
		a+=0.5
    
    def shutdown(self):
        rospy.loginfo("Stop")


if __name__ == '__main__':
    try:
        newgoals()
    except rospy.ROSInterruptException:
        rospy.loginfo("Unable to Call Class")

