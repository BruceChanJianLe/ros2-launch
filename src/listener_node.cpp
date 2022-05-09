#include "ros2-launch/listener.hpp"

constexpr auto ROS2NODENAME = "ros2_launch_listener_node";

int main(int argc, char * argv[])
{
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<ros2_launch::listener>(ROS2NODENAME));
    rclcpp::shutdown();

    return 0;
}