# 🐊 Gator Rover — Software Subteam Workspace

Welcome to the official **Gator Rover** software repository! This repository hosts the ROS 2 packages, simulation pipelines, and autonomy stack for our NASA Lunabotics rover.

---

## 🚀 Quickstart for Team Members

### Option 1: VS Code Dev Containers (Recommended — Zero Configuration)
1. Install **Docker Desktop** (Windows/Mac) or Docker Engine (Linux) and **VS Code**.
2. Install the **Dev Containers** extension in VS Code.
3. Open this repository folder in VS Code.
4. When prompted (or press `Ctrl+Shift+P` / `Cmd+Shift+P` $\rightarrow$ **"Dev Containers: Reopen in Container"**).
5. Open an integrated terminal (``Ctrl + ` ``). ROS 2 Humble and all dependencies are pre-installed!

### Option 2: Native WSL 2 / Ubuntu 22.04 LTS
If you already set up **ROS 2 Humble** natively in Ubuntu:
```bash
# 1. Clone this repository into your workspace
cd ~/rover_ws  # or your preferred folder
git clone https://github.com/your-org/gator-rover.git
cd gator-rover

# 2. Install package dependencies
rosdep update
rosdep install --from-paths src --ignore-src -r -y

# 3. Build workspace
colcon build --symlink-install

# 4. Source the built workspace
source install/setup.bash
```

---

## 🧪 Testing the Starter Node

Launch the starter rover heartbeat node:
```bash
ros2 launch rover_core rover_core.launch.py
```

In a second terminal, send a test drive command to verify subscriber communication:
```bash
ros2 topic pub /cmd_vel geometry_msgs/msg/Twist "{linear: {x: 0.5}, angular: {z: 0.2}}" --once
```

You should see the node acknowledge the command and output its telemetry heartbeat!

---

## 🗂️ Repository Structure

```
gator-rover/
├── .devcontainer/               # VS Code Docker development container
├── Dashboard.md                 # Obsidian Map of Content & System Hub
├── Tasks/                       # New member task guides & roster
├── Subsystems/                  # System architecture & hardware specs
├── Competition/                 # NASA Lunabotics 2026 specs & rules
├── src/                         # ROS 2 Source Packages
│   └── rover_core/              # Core status, heartbeat, & telemetry node
└── README.md
```

---

## 🌿 Git Contribution Workflow

1. Always branch from `main`:
   ```bash
   git checkout main
   git pull origin main
   git checkout -b feature/your-feature-name
   ```
2. Commit your changes with clear messages.
3. Push to your branch and open a **Pull Request (PR)** on GitHub.
