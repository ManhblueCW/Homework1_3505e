from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from gen_py.order_service import OrderProcessing
import mysql.connector

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="M@nhbh12345",
    database="blackmarket"
)

class OrderProcessingHandler:
    def calculateTotal(self, productId, quantity):
        cursor = db.cursor()
        cursor.execute("SELECT price FROM products WHERE product_id = %s", (productId,))
        result = cursor.fetchone()

        if result:
            price = result[0]
            total_price = price * quantity
            return total_price
        else:
            return 0.0

handler = OrderProcessingHandler()
processor = OrderProcessing.Processor(handler)
transport = TSocket.TServerSocket(port=9090)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()
server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

print("Starting Thrift server on port 9090...")
server.serve()
