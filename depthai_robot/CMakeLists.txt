cmake_minimum_required (VERSION 3.10.2)  # CMake version in Ubuntu 18.04 LTS
project(depthai_robot)

find_package(ament_cmake REQUIRED)

install
  DIRECTORY launch
  DESTINATION share($PROJECT_NAME)

ament_package()
