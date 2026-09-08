#!/usr/bin/env python3
"""
status_node.py - Gator Rover Core Heartbeat & Telemetry Monitor
Demonstrates a ROS 2 Python Node with both Publisher & Subscriber.
"""

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Twist


class RoverStatusNode(Node):
    def __init__(self):
        super().__init__('rover_status_node')

        # Telemetry Heartbeat Publisher
        self.status_publisher = self.create_publisher(String, '/rover/status', 10)
        self.timer = self.create_timer(1.0, self.publish_heartbeat)

        # Velocity Command Subscriber (Listens to /cmd_vel)
        self.cmd_vel_subscriber = self.create_subscription(
            Twist,
            '/cmd_vel',
            self.cmd_vel_callback,
            10
        )

        self.heartbeat_counter = 0
        self.get_logger().info('🐊 Gator Rover Status Node initialized and ready!')

    def publish_heartbeat(self):
        msg = String()
        msg.data = f'Gator Rover Online | Heartbeat: #{self.heartbeat_counter} | System: OK'
        self.status_publisher.publish(msg)
        self.get_logger().info(f'Published: "{msg.data}"')
        self.heartbeat_counter += 1

    def cmd_vel_callback(self, msg: Twist):
        self.get_logger().info(
            f'Received Drive Command -> Linear X: {msg.linear.x:.2f} m/s | Angular Z: {msg.angular.z:.2f} rad/s'
        )


def main(args=None):
    rclpy.init(args=args)
    node = RoverStatusNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Shutting down Rover Status Node...')
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
