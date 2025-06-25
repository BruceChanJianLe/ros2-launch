from launch import LaunchDescription
from launch_ros.actions import Node

# Launch Args
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

# Load Params Yaml
import os
from ament_index_python.packages import get_package_share_directory
from launch.substitutions import PathJoinSubstitution

ARGUMENTS = [
    DeclareLaunchArgument(
        "param1",
        default_value="1",
        description="The param1 arguement, by default has value 1",
    ),
    DeclareLaunchArgument(
        "param2",
        default_value="2",
        description="The param2 arguement, by default has value 2",
    ),
    DeclareLaunchArgument(
        "configuration_selection1",
        default_value="configuration1",
        description="The configuration to be selected.",
    ),
    DeclareLaunchArgument(
        "configuration_selection2",
        default_value="configuration2",
        description="The configuration to be seleted.",
    ),
]


def generate_launch_description():
    talker_node = Node(
        package="ros2-launch",
        executable="ros2_launch_talker",
        name="ros2_launch_talker_node",
        parameters=[
            os.path.join(
                get_package_share_directory("ros2-launch"), "config", "params.yaml"
            )
        ],
    )

    configuration1_talker_node = Node(
        package="ros2-launch",
        executable="ros2_launch_talker",
        name="con1_talker_node",
        parameters=[
            PathJoinSubstitution(
                [
                    get_package_share_directory("ros2-launch"),
                    "config",
                    LaunchConfiguration("configuration_selection1"),
                    "params.yaml",
                ]
            )
        ],
    )

    configuration2_talker_node = Node(
        package="ros2-launch",
        executable="ros2_launch_talker",
        name="con2_talker_node",
        parameters=[
            PathJoinSubstitution(
                [
                    get_package_share_directory("ros2-launch"),
                    "config",
                    LaunchConfiguration("configuration_selection2"),
                    "params.yaml",
                ]
            )
        ],
    )
    # Define launch description
    ld = LaunchDescription(ARGUMENTS)
    ld.add_action(talker_node)
    ld.add_action(configuration1_talker_node)
    ld.add_action(configuration2_talker_node)

    # Return launch description
    return ld
