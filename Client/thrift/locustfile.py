import time
import random
from locust import User, task, events
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from gen_py.order_service.OrderProcessing import Client  # ✅ Import generated Thrift client


class ThriftClient(User):
    wait_time = lambda self: random.uniform(1, 3)  # Simulate realistic user behavior

    def on_start(self):
        """Initialize Thrift connection"""
        self.transport = TSocket.TSocket("192.168.0.95", 9090)  # Change to your server's IP and port
        self.transport = TTransport.TBufferedTransport(self.transport)
        protocol = TBinaryProtocol.TBinaryProtocol(self.transport)
        self.client = Client(protocol)  # ✅ Create Thrift client
        self.transport.open()

    @task
    def calculate_total(self):
        """Simulate a request to the calculateTotal method"""
        product_id = "P" + str(random.randint(0, 999))
        quantity = random.randint(1, 10)

        start_time = time.time()  # Measure response time
        total_price = self.client.calculateTotal(product_id, quantity)  # Call Thrift method
        response_time = (time.time() - start_time) * 1000  # Convert to milliseconds

        events.request.fire(
            request_type="Thrift",
            name="calculateTotal",
            response_time=response_time,
            response_length=len(str(total_price))
        )

    def on_stop(self):
        """Close the Thrift connection"""
        self.transport.close()
