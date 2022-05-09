#pragma once

// ROS2
#include "rclcpp/rclcpp.hpp"

// Msgs
#include "std_msgs/msg/u_int16.hpp"

// STL
#include <string>
#include <chrono>
#include <memory>

namespace ros2_launch
{
    class listener : public rclcpp::Node
    {
    public:
        listener();
        listener(const std::string &);
        ~listener();
    private:
        rclcpp::Subscription<std_msgs::msg::UInt16>::SharedPtr sub_;
        void subCallback(const std_msgs::msg::UInt16::SharedPtr) const;
    };

} // namespace ros2_launch
