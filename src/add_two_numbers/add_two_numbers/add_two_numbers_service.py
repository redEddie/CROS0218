Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import rclpy
... from rclpy.node import Node
... from example_interfaces.srv import AddTwoInts
... 
... class AddTwoNumbersService(Node):
...     def __init__(self):
...         super().__init__('add_two_numbers_service')
...         self.srv = self.create_service(AddTwoInts, 'add_two_numbers', self.handle_request)
...         self.get_logger().info('Service ready.')
... 
...     def handle_request(self, request, response):
...        
...         if request.a > 50:
...             response.sum = 0  
...             self.get_logger().info(f"Received: {request.a}, Responding with: 119에 신고했습니다")
...         else:
...             response.sum = request.a + request.b  
...             self.get_logger().info(f"Received: {request.a} + {request.b} = {response.sum}")
...         return response
... 
... def main(args=None):
...     rclpy.init(args=args)
...     node = AddTwoNumbersService()
...     try:
...         rclpy.spin(node)
...     except KeyboardInterrupt:
...         pass
...     finally:
...         rclpy.shutdown()
... 
... if __name__ == '__main__':
...     main()
