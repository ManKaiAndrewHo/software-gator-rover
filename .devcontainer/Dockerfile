FROM osrf/ros:humble-desktop

ENV DEBIAN_FRONTEND=noninteractive

# Install essential dev & robotics tools
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    curl \
    python3-pip \
    python3-colcon-common-extensions \
    python3-rosdep \
    ros-humble-foxglove-bridge \
    ros-humble-teleop-twist-keyboard \
    ros-humble-cv-bridge \
    && rm -rf /var/lib/apt/lists/*

# Automatically source ROS 2 on new terminals
RUN echo "source /opt/ros/humble/setup.bash" >> /root/.bashrc \
    && echo "if [ -f /workspace/install/setup.bash ]; then source /workspace/install/setup.bash; fi" >> /root/.bashrc

WORKDIR /workspace
