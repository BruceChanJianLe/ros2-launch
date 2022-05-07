#include "ros2-launch/talker.hpp"

constexpr auto ROS2NODENAME = "ros2_launch_talker_node";

int main(int argc, char * argv[])
{
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<ros2_launch::talker>(ROS2NODENAME));
    rclcpp::shutdown();

    return 0;
}