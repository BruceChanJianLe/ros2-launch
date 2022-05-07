#include "ros2-launch/talker.hpp"

namespace ros2_launch
{
    talker::talker()
    :   Node("ros2_launch_talker")
    ,   count_(0)
    {
        pub_ = this->create_publisher<std_msgs::msg::UInt16>("ros2_launch_talker/channel", 1);
        timer_ = this->create_wall_timer(std::chrono::seconds(1), [this](){this->run();});
    }

    talker::talker(const std::string & node_name)
    : Node(node_name)
    ,   count_(0)
    {
        pub_ = this->create_publisher<std_msgs::msg::UInt16>("ros2_launch_talker/channel", 1);
        timer_ = this->create_wall_timer(std::chrono::seconds(1), [this](){this->run();});
    }

    talker::~talker()
    {
    }

    void talker::run()
    {
        // Prepare msg
        auto msg = std_msgs::msg::UInt16();
        msg.data = this->count_++;

        pub_->publish(msg);

        RCLCPP_INFO_STREAM(
            this->get_logger(),
            this->get_name()
            << " "
            << "I have spoken: "
            << msg.data
        );
    }
} // namespace ros2_launch