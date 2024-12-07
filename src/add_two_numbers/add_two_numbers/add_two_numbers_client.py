Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import rclpy
... from rclpy.node import Node
... from example_interfaces.srv import AddTwoInts
... 
... class AddTwoNumbersClient(Node):
...     def __init__(self):
...         super().__init__('add_two_numbers_client')
...         self.client = self.create_client(AddTwoInts, 'add_two_numbers')
...         while not self.client.wait_for_service(timeout_sec=1.0):
...             self.get_logger().info('Waiting for service to become available...')
...         self.request = AddTwoInts.Request()
... 
...     def send_request(self, number):
...         self.request.a = number
...         self.request.b = 0
...         self.future = self.client.call_async(self.request)
...         rclpy.spin_until_future_complete(self, self.future)
...         return self.future.result()
... 
... def main(args=None):
...     rclpy.init(args=args)
...     node = AddTwoNumbersClient()
... 
...     number = int(input("Enter a number: "))
...     response = node.send_request(number)
... 
...     if response is not None:
...         node.get_logger().info(f"Result: {response.sum}")
...     else:
...         node.get_logger().error("Service call failed.")
... 
...     node.destroy_node()
...     rclpy.shutdown()
... 
... if __name__ == '__main__':
...     main()
