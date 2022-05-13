from launch import LaunchDescription
# Include other launch files
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
# Namespace
from launch.actions import GroupAction
from launch_ros.actions import PushRosNamespace

def generate_launch_description():
    # Other launch file
    other_launch_file = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            # Path to ohter launch file
            PathJoinSubstitution([
                FindPackageShare('ros2-launch'),
                'launch',
                'other_launch_files.launch.py'
            ])
        ])
    )

    # Namespace Inherit
    namespace_other_launch_file = GroupAction(
        actions=[
            PushRosNamespace('foxy'),
            other_launch_file
        ]
    )

    # Define launch description
    ld = LaunchDescription()
    ld.add_action(namespace_other_launch_file)

    # Return launch description
    return ld