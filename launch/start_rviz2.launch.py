from launch import LaunchDescription
from launch_ros.actions import Node

# Load RVIZ config
import os
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    start_rviz2 = Node(
        package="rviz2",
        executable="rviz2",
        output="screen",
        arguments=[
            "-d",
            os.path.join(
                get_package_share_directory("ros2-launch"), "rviz2", "config.rviz"
            ),
        ],
    )

    ld = LaunchDescription()
    ld.add_action(start_rviz2)

    return ld
