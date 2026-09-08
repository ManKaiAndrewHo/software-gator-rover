FROM osrf/ros:humble-desktop

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-colcon-common-extensions \
    python3-rosdep \
    ros-humble-foxglove-bridge \
    ros-humble-teleop-twist-keyboard \
    ros-humble-cv-bridge \
    && rm -rf /var/lib/apt/lists/*
