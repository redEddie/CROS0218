#!/usr/bin/env python3

import sys
import rclpy
from rclpy.node import Node
from my_interface.srv import DogResponse


class VoiceInteractionClient(Node):
    def __init__(self):
        super().__init__("interaction_client")
        self.cli = self.create_client(DogResponse, "dog_response")

        while not self.cli.wait_for_service(timeout_sec=0.1):
            self.get_logger().info("service not available, waiting again...")

        self.req = DogResponse.Request()

    def send_request(self):
        self.req.command = sys.argv[1]
        self.future = self.cli.call_async(self.req)


def main(args=None):
    if len(sys.argv) != 2:
        print("Usage: voice_command_client <command>")
        print("Example: voice_command_client play/treat/pat")
        sys.exit(1)

    # command = sys.argv[1]

    rclpy.init()
    client = VoiceInteractionClient()
    client.send_request()

    while rclpy.ok():
        rclpy.spin_once(client)
        if client.future.done():
            try:
                response = client.future.result()
            except Exception as e:
                client.get_logger().error(f"Service call failed {e}")
            else:
                client.get_logger().info(f"Response: {response.response}")
            break

    client.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
