#include "ros2-launch/talker.hpp"

namespace ros2_launch
{
    talker::talker()
    :   Node("ros2_launch_talker")
    ,   count_(0)
    ,   param1_(0)
    ,   param2_(0)
    {
        // Declare params
        this->declare_parameter<int>("param1", 0);
        this->declare_parameter<int>("param2", 0);

        pub_ = this->create_publisher<std_msgs::msg::UInt16>("ros2_launch_talker/channel", 1);
        timer_ = this->create_wall_timer(std::chrono::seconds(1), [this](){this->run();});

        // Get params
        this->get_parameter<int>("param1", param1_);
        this->get_parameter<int>("param2", param2_);
    }

    talker::talker(const std::string & node_name)
    : Node(node_name)
    ,   count_(0)
    ,   param1_(0)
    ,   param2_(0)
    {
        // Declare params
        this->declare_parameter<int>("param1", 0);
        this->declare_parameter<int>("param2", 0);

        pub_ = this->create_publisher<std_msgs::msg::UInt16>("ros2_launch_talker/channel", 1);
        timer_ = this->create_wall_timer(std::chrono::seconds(1), [this](){this->run();});

        // Get params
        this->get_parameter("param1", param1_);
        this->get_parameter("param2", param2_);
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
            << ", with param1 "
            << param1_
            << ", param2 "
            << param2_
        );
    }
} // namespace ros2_launch