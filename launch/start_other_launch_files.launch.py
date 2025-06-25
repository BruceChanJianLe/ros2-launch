from launch import LaunchDescription
# Include other launch files
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

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
        )

        # Define launch description
        ld = LaunchDescription()
        ld.add_action(other_launch_file)

        # Return launch description
        return ld
