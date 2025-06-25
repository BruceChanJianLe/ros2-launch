from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription(
        [
            Node(
                package="ros2-launch",
                executable="ros2_launch_talker",
                name="ros2_launch_talker_node",
                # namespace='',
                # remappings=[
                #     ('ros2_launch_talker/channel', 'talker')
                # ]
            )
        ]
    )
