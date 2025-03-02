import grpc
import random
import time
from locust import User, task, events
from order_pb2 import OrderRequest
from order_pb2_grpc import OrderServiceStub


class GrpcClient(User):
    wait_time = lambda self: random.uniform(1, 3)

    def on_start(self):
        """Initialize gRPC channel and stub on start"""
        self.channel = grpc.insecure_channel("192.168.0.95:50051")  # Server IP and gRPC port
        self.stub = OrderServiceStub(self.channel)

    @task
    def place_order(self):
        """Simulate gRPC Order request with response time measurement"""
        request = OrderRequest(
            product_id="P" + str(random.randint(0, 999)),
            quantity=random.randint(1, 10)
        )

        start_time = time.time()
        response = self.stub.CalculateTotal(request)
        response_time = (time.time() - start_time) * 1000  # Convert to milliseconds

        events.request.fire(
            request_type="gRPC",
            name="CalculateTotal",
            response_time=response_time,
            response_length=len(str(response))
        )