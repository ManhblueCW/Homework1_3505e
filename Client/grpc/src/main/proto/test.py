import grpc
import random
import time
from order_pb2 import OrderRequest
from order_pb2_grpc import OrderServiceStub

channel = grpc.insecure_channel("192.168.0.95:50051")  # Server IP and gRPC port
stub = OrderServiceStub(channel)

request = OrderRequest(
            product_id="P" + str(random.randint(0, 999)),
            quantity=random.randint(1, 10)
        )

start_time = time.time()
response = stub.CalculateTotal(request)
response_time = (time.time() - start_time) * 1000
print(response)