from launch import LaunchDescription
from launch_ros.actions import Node
# Launch Args
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
# Load Params Yaml
import os
from ament_index_python.packages import get_package_share_directory

ARGUMENTS = [
    DeclareLaunchArgument(
        'param1',
        default_value='1',
        description='The param1 arguement, by default has value 1',
    ),
    DeclareLaunchArgument(
        'param2',
        default_value='2',
        description='The param2 arguement, by default has value 2',
    ),
]

def generate_launch_description():
        # Launch args
        param1 = LaunchConfiguration('param1')
        param2 = LaunchConfiguration('param2')

        talker_node = Node(
            package='ros2-launch',
            executable='ros2_launch_talker',
            name='ros2_launch_talker_node',
            parameters=[os.path.join(get_package_share_directory('ros2-launch'), 'config', 'params.yaml')],
        )

        # Define launch description
        ld = LaunchDescription(ARGUMENTS)
        ld.add_action(talker_node)

        # Return launch description
        return ld