from multiprocessing import Condition
from launch import LaunchDescription
from launch_ros.actions import Node
# Shell Commands
from launch.actions import ExecuteProcess
from launch.conditions import IfCondition, UnlessCondition
from launch.substitutions import PythonExpression
# Launch Args
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

ARGUMENTS = [
    DeclareLaunchArgument(
        'set_param2',
        default_value='False',
        description='Set param2 to 88 if True',
    ),
]

def generate_launch_description():
    # Launch args
    set_param2 = LaunchConfiguration('set_param2')

    # Echo something
    say_something = ExecuteProcess(
        cmd=[[
            'echo ',
            'say_something'
        ]],
        shell=True
    )

    # Set param
    # ros2 param set <node_name> <param>
    set_param1 = ExecuteProcess( cmd=[[
            'ros2 param set',
            ' ros2_launch_talker_node',
            ' param1',
            ' 77'
        ]],
        shell=True
    )

    talker_node = Node(
        package='ros2-launch',
        executable='ros2_launch_talker',
        name='ros2_launch_talker_node',
    )

    # Conditional set param
    conditional_set_param2 = ExecuteProcess(
        # Condition
        condition=IfCondition(
            PythonExpression([
                set_param2,
                ' == True'
            ])
        ),
        cmd=[[
            'ros2 param set'
            ' ros2_launch_talker_node',
            ' param2',
            ' 88'
        ]],
        shell=True
    )

    ld = LaunchDescription(ARGUMENTS)
    ld.add_action(say_something)
    ld.add_action(talker_node)
    ld.add_action(set_param1)
    ld.add_action(conditional_set_param2)

    return ld