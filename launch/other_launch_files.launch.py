from launch import LaunchDescription
from launch_ros.actions import Node

# Launch Args
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

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
]


def generate_launch_description():
    # Launch args
    param1 = LaunchConfiguration("param1")
    param2 = LaunchConfiguration("param2")

    talker_node = Node(
        package="ros2-launch",
        executable="ros2_launch_talker",
        name="ros2_launch_talker_node",
        # namespace='',
        # remappings=[
        #     ('ros2_launch_talker/channel', 'talker')
        # ]
        parameters=[
            {
                "param1": param1,
                "param2": param2,
            }
        ],
    )

    # Define launch description
    ld = LaunchDescription(ARGUMENTS)
    ld.add_action(talker_node)

    # Return launch description
    return ld
