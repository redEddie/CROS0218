#!/usr/bin/env python3

import time
from my_interface.srv import DogResponse

import rclpy
from rclpy.node import Node
from rclpy.callback_groups import ReentrantCallbackGroup
from rclpy.executors import MultiThreadedExecutor


class DogResponseServer(Node):
    def __init__(self):
        super().__init__("dog_behavior_server")
        self.callback_group = ReentrantCallbackGroup()

        self.service_server = self.create_service(
            DogResponse,
            "dog_response",
            self.get_dog_behavior,
            callback_group=self.callback_group,
        )

    def get_dog_behavior(self, request, response):
        self.get_logger().info(f"Request: {request.command}")
        if request.command == "play":
            response.response = "bark! bark!"
        elif request.command == "treat":
            response.response = "gentle-woof"
        elif request.command == "pat":
            response.response = "happy-yelp"
        else:
            response.response = "..."
        self.get_logger().info(f"Response: {response.response}")
        return response


def main(args=None):
    rclpy.init(args=args)
    try:
        server = DogResponseServer()
        executor = MultiThreadedExecutor(num_threads=4)
        executor.add_node(server)
        try:
            executor.spin()
        except KeyboardInterrupt:
            server.get_logger().info("Keyboard Interrupt (SIGINT)")
        finally:
            executor.shutdown()
            server.destroy_node()
    finally:
        rclpy.shutdown()


if __name__ == "__main__":
    main()
