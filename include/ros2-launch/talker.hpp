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
    class talker : public rclcpp::Node
    {
    public:
        talker();
        talker(const std::string &);
        ~talker();
    private:
        size_t count_;
        // Params
        int param1_, param2_;
        rclcpp::Publisher<std_msgs::msg::UInt16>::SharedPtr pub_;
        rclcpp::TimerBase::SharedPtr timer_;
        void run();
    };

} // namespace ros2_launch
