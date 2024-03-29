cmake_minimum_required(VERSION 3.5)
project(ros2-launch)

# Default to C99
if(NOT CMAKE_C_STANDARD)
  set(CMAKE_C_STANDARD 99)
endif()

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)

include_directories(
  include
)

# Talker node
add_executable(ros2_launch_talker
  src/talker_node.cpp
  src/talker.cpp
)
ament_target_dependencies(ros2_launch_talker
  rclcpp
  std_msgs
)

# Listener node
add_executable(ros2_launch_listener
  src/listener_node.cpp
  src/listener.cpp
)
ament_target_dependencies(ros2_launch_listener
  rclcpp
  std_msgs
)

# Install executables
install(TARGETS
  ros2_launch_talker
  ros2_launch_listener
  DESTINATION lib/${PROJECT_NAME}
)

# Install directories
install(DIRECTORY
  launch
  config
  rviz2
  DESTINATION share/${PROJECT_NAME}/
)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # uncomment the line when a copyright and license is not present in all source files
  #set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # uncomment the line when this package is not in a git repo
  #set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
