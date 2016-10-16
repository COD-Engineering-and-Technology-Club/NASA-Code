#include <ros/ros.h>
#include "sensor_msgs/Joy.h"
#include "std_msgs/String.h"

#include <fcntl.h>
#include <unistd.h>
#include <termios.h>
#include <string>
#include <vector>
#include <cmath>

using namespace std;


//*****START HERE********
void joyCallback(const sensor_msgs::Joy::ConstPtr&);

int main (int argc, char **argv)
{
	ros::init(argc, argv, "joy_test");
	
	ros::NodeHandle nh;

	ros::Subscriber sub = nh.subscribe("joytopic", 1000, &joyCallback);
	ros::spin();
}

void joyCallback(const sensor_msgs::Joy::ConstPtr& joy)
{
	ros::NodeHandle nh2;
	ros::Publisher pub = nh2.advertise<std_msgs::String>("joyDigger", 1000);
	
	std_msgs::String msg1;
	std_msgs::String msg2;

	if(joy->buttons[0] == 1) //wheel actuators reverse
	{
		//ROS_INFO_STREAM("You pressed A!");
			msg1.data = "@03!G 1 -1000\r";
			msg2.data = "@03!G 2 -1000\r";
	}

	if(joy->buttons[1] == 1) //arm actuators reverse
	{
		//ROS_INFO_STREAM("You pressed B!");
			msg1.data = "@02!G 1 -1000\r";
			msg2.data = "@02!G 2 -1000\r";
	}
	if(joy->buttons[2] == 1) //wheel actuators forward
	{
		//ROS_INFO_STREAM("You pressed X!");
			msg1.data = "@03!G 1 1000\r";
			msg2.data = "@03!G 2 1000\r";
	}
	if(joy->buttons[3] == 1)
	{
		ROS_INFO_STREAM("You pressed Y!"); //arm actuators forward
			msg1.data = "@02!G 1 1000\r";
			msg2.data = "@02!G 2 1000\r";
	}
	if(joy->buttons[5] == 1)
	{
		msg1.data = "^RWD 500\r";
		ROS_INFO_STREAM("FULL STOP");
	}

	if(joy->axis[7] == 1) //auger forward(?)
	{
		msg1.data = "@04!G 1 1000\r";
	}

	if(joy->axis[7] == -1) //auger backward(?)
	{
		msg1.data = "@04!G 1 -1000\r";
	}
		pub.publish(msg1);
		pub.publish(msg2);


}
