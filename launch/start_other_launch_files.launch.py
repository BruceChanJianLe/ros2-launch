from launch import LaunchDescription
from launch_ros.actions import Node
# Launch Args
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
# Include other launch files
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

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

        # Other launch file
        other_launch_file = IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                # Path to other launch file
                PathJoinSubstitution([
                    FindPackageShare('ros2-launch'),
                    'launch',
                    'other_launch_files.launch.py'
                ])
            ]),
            launch_arguments={
                'param1' : param1,
                'param2' : param2,
            }.items()
        )

        # Define launch description
        ld = LaunchDescription(ARGUMENTS)
        ld.add_action(other_launch_file)

        # Return launch description
        return ld