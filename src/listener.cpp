#include "ros2-launch/listener.hpp"


namespace ros2_launch
{
    listener::listener()
    : rclcpp::Node("ros2_launch_listener_node")
    {
    }

    listener::listener(const std::string & node_name)
    : rclcpp::Node(node_name)
    {
        sub_ = this->create_subscription<std_msgs::msg::UInt16>("ros2_launch_talker/channel", 1, [this](const std_msgs::msg::UInt16::SharedPtr msg){this->subCallback(msg);});
    }

    listener::~listener()
    {
    }

    void listener::subCallback(const std_msgs::msg::UInt16::SharedPtr msg) const
    {
        RCLCPP_INFO_STREAM(
            this->get_logger(),
            this->get_name()
            << " I heard "
            << msg->data
            << "."
        );
    }
} // namespace ros2_launch