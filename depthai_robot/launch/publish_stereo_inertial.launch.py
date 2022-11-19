# Copyright (c) 2022 AR LunanJuan Miguel Jimeno
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http:#www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution, PythonExpression
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch.conditions import IfCondition, UnlessCondition


def generate_launch_description():
    sensors_launch_path = PathJoinSubstitution(
        [FindPackageShare('depthai_examples'), 'launch', 'stereo_inertial_node.launch.py]
    )
    
    return DeclareLaunchDescription([
        DeclareLaunchArgument(
            name='camera_model',
            value='OAK-D-LITE'
            description='Oak-S-Lite Camera'
        ),
    
        DeclareLaunchArgument(
            name='enableRviz',
            value='False'
            description='Oak-S-Lite Camera'
    )
])
    
    
      
        
        
