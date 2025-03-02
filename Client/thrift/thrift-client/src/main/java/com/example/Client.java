package com.example;

import org.apache.thrift.protocol.TBinaryProtocol;
import org.apache.thrift.protocol.TProtocol;
import org.apache.thrift.transport.TSocket;
import org.apache.thrift.transport.TTransport;
import com.example.order.OrderProcessing;

public class Client {
    public static void main(String[] args) {
        try (TTransport transport = new TSocket("192.168.0.95", 9090)) {
            transport.open();
            TProtocol protocol = new TBinaryProtocol(transport);
            OrderProcessing.Client client = new OrderProcessing.Client(protocol);
            String productId = "P200";
            int quantity = 5;
            double total = client.calculateTotal(productId, quantity);
            System.out.println("Product: " + productId +
                               "\nQuantity: " + quantity +
                               "\nTotal: " + total);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
