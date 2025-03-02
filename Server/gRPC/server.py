import grpc
import mysql.connector
from concurrent import futures
import order_pb2
import order_pb2_grpc

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="M@nhbh12345",
    database="blackmarket"
)

class OrderServiceServicer(order_pb2_grpc.OrderServiceServicer):
    def CalculateTotal(self, request, context):
        cursor = db.cursor()
        cursor.execute("SELECT price FROM products WHERE product_id = %s", (request.product_id,))
        result = cursor.fetchone()
        
        if result:
            price = result[0]
            total_price = price * request.quantity
            return order_pb2.OrderResponse(total_price=total_price)
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Product not found")
            return order_pb2.OrderResponse(total_price=0.0)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    order_pb2_grpc.add_OrderServiceServicer_to_server(OrderServiceServicer(), server)
    server.add_insecure_port("[::]:50051")
    print("Server running on port 50051...")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
