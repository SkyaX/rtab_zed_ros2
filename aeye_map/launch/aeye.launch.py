import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch_ros.substitutions import FindPackageShare
from launch.launch_description_sources import PythonLaunchDescriptionSource
from pathlib import Path

def generate_launch_description():

    # Get the launch directory
    zed_dir = get_package_share_directory('zed_wrapper')
    zed_launch_dir = os.path.join(zed_dir, 'launch')

    zed_wrapper_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            zed_launch_dir + '/zed2i.launch.py'
        ),
    )
    # Get the launch directory
    rtab_dir = get_package_share_directory('rtabmap_launch')
    rtab_launch_dir = os.path.join(rtab_dir, 'launch')
    
    rtabmap_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            rtab_launch_dir + '/rtabmap.launch.py'
        ),
        launch_arguments=[
            ("rtabmap_args", "--delete_db_on_start"),
            ("rgb_topic", "/zed2i/zed_node/rgb/image_rect_color"),
            ("depth_topic", "/zed2i/zed_node/depth/depth_registered"),
            ("camera_info_topic", "/zed2i/zed_node/rgb/camera_info"),
            ("imu_topic", "/zed2i/zed_node/imu/data"),
            ("frame_id", "base_link"),
            ("approx_sync", "false"),
            ("wait_imu_to_init", "true"),
            ("qos", "1"),
            ("rviz", "true")
        ]
    )

    return LaunchDescription([
        zed_wrapper_launch,
        rtabmap_launch,
    ])