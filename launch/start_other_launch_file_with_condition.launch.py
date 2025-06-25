from launch import LaunchDescription
# Launch Args
from launch.actions import DeclareLaunchArgument
# Include other launch files
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
# Launch condition
from launch.conditions import IfCondition
from launch.substitutions import EqualsSubstitution, LaunchConfiguration

ARGUMENTS = [
    DeclareLaunchArgument(
        'start_other_launch',
        default_value='false',
        description='If true launch other launch file, otherwise do not launch other launch file',
    ),
]

def generate_launch_description():

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
            condition=IfCondition(EqualsSubstitution(LaunchConfiguration('start_other_launch'), 'true'))
        )

        # Define launch description
        ld = LaunchDescription(ARGUMENTS)
        ld.add_action(other_launch_file)

        # Return launch description
        return ld
