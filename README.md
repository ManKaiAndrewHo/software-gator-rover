# Gator Rover Software

Software stack for the Gator Rover robotics team competing in the NASA Lunabotics Challenge. Built on **ROS 2 Humble** and **Ubuntu 22.04 LTS**.

## Getting Started

### Option A: VS Code Dev Container (Recommended)
Requires [Docker](https://www.docker.com/) and [VS Code](https://code.visualstudio.com/) with the **Dev Containers** extension.

1. Open this folder in VS Code.
2. Click **Reopen in Container** when prompted (or open the Command Palette `Ctrl+Shift+P` / `Cmd+Shift+P` and run `Dev Containers: Reopen in Container`).
3. VS Code will spin up the environment with ROS 2 Humble and all core dependencies pre-installed.

### Option B: Local Setup (Ubuntu 22.04 / WSL 2)
Requires a native [ROS 2 Humble](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html) desktop installation.

```bash
# Clone the repository
git clone https://github.com/MonishB123/software-gator-rover.git
cd software-gator-rover

# Install package dependencies
rosdep update
rosdep install --from-paths src --ignore-src -r -y

# Build the workspace
colcon build --symlink-install
source install/setup.bash
```

## Running the Core Node

Launch the status heartbeat node:
```bash
ros2 launch rover_core rover_core.launch.py
```

In a separate terminal, test publishing velocity commands:
```bash
ros2 topic pub /cmd_vel geometry_msgs/msg/Twist "{linear: {x: 0.5}, angular: {z: 0.0}}" --once
```

## Repository Layout

```
software-gator-rover/
├── .devcontainer/       # Dev container configuration (ROS 2 Humble)
├── src/
│   └── rover_core/      # Telemetry, heartbeat, and base status node
└── README.md
```

## Contributing

1. Always create a branch off `main`:
   ```bash
   git checkout main
   git pull origin main
   git checkout -b feature/<your-name>-<feature-description>
   ```
2. Build and verify your code locally before pushing.
3. Commit with concise messages and submit a Pull Request (PR) to `main`.
