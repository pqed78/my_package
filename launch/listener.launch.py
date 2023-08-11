from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LauchDescription([
        Node(
            package='demo_nodes_py',
            executable='listener'
        )
    ])