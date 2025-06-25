from launch import LaunchDescription
from launch_ros.actions import Node

# Launch Args
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

# Event Handler
from launch.actions import RegisterEventHandler
from launch.event_handlers import (
    OnExecutionComplete,
    OnProcessExit,
    OnProcessIO,
    OnProcessStart,
    OnShutdown,
)
from launch.actions import ExecuteProcess, LogInfo, EmitEvent
from launch.substitutions import EnvironmentVariable, LocalSubstitution
from launch.events import Shutdown

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
        parameters=[
            {
                "param1": param1,
                "param2": param2,
            }
        ],
    )

    listener_node = Node(
        package="ros2-launch",
        executable="ros2_launch_listener",
        name="ros2_launch_listener_node",
    )

    # On Process Start
    on_process_start = RegisterEventHandler(
        OnProcessStart(
            target_action=talker_node,
            on_start=[
                LogInfo(msg="Talker node has started, launching listener node."),
                listener_node,
            ],
        )
    )

    trigger_exec = ExecuteProcess(
        cmd=[['echo "I am just a trigger"']],
        shell=True,
        output={"stderr": "screen", "stdout": "screen"},
    )

    # On Process Input Output
    on_process_io = RegisterEventHandler(
        OnProcessIO(
            target_action=trigger_exec,
            on_stdout=lambda event: LogInfo(
                msg='Trigger process says: "{}"'.format(event.text.decode().strip())
            ),
        )
    )

    # On Process Complete, WARNING: This example is not working as expected
    on_process_complete = RegisterEventHandler(
        OnExecutionComplete(
            target_action=on_process_io,
            on_completion=[
                LogInfo(msg="Trigger has been called!"),
                # TimerAction(period=2.0, actions=[ExecuteProcess(cmd=[['ros2 topic pub /ros2_launch_talker/channel std_msgs/msg/UInt16 "data: 99" --once']], shell=True)]),
                ExecuteProcess(
                    cmd=[
                        [
                            'ros2 topic pub /ros2_launch_talker/channel std_msgs/msg/UInt16 "data: 99" --once'
                        ]
                    ],
                    shell=True,
                ),
            ],
        )
    )

    # On Process Exit
    on_process_exit = RegisterEventHandler(
        OnProcessExit(
            target_action=listener_node,
            on_exit=[
                LogInfo(
                    msg=(
                        EnvironmentVariable(name="USERNAME"),
                        " closed the listener_node.",
                    )
                ),
                EmitEvent(event=Shutdown(reason="nodes killed.")),
            ],
        )
    )

    # On Shutdown
    on_shutdown = RegisterEventHandler(
        OnShutdown(
            on_shutdown=[
                LogInfo(
                    msg=[
                        "Launch was asked to shutdown: ",
                        LocalSubstitution("event.reason"),
                    ]
                )
            ]
        )
    )

    # Define launch description
    ld = LaunchDescription(ARGUMENTS)
    ld.add_action(talker_node)
    ld.add_action(on_process_start)
    ld.add_action(trigger_exec)
    ld.add_action(on_process_io)
    ld.add_action(on_process_complete)
    ld.add_action(on_process_exit)
    ld.add_action(on_shutdown)

    # Return launch description
    return ld
