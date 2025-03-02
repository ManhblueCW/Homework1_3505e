package com.example;

import io.grpc.ManagedChannel;
import io.grpc.ManagedChannelBuilder;
import order.OrderServiceGrpc;
import order.Order;

public class Client {
    public static void main(String[] args) {
        ManagedChannel channel = ManagedChannelBuilder.forAddress("192.168.0.95", 50051)
                .usePlaintext()
                .build();

        OrderServiceGrpc.OrderServiceBlockingStub stub = OrderServiceGrpc.newBlockingStub(channel);

        String productId = "P0";
        int quantity = 3;
        Order.OrderRequest request = Order.OrderRequest.newBuilder()
                .setProductId(productId)
                .setQuantity(quantity)
                .build();

        Order.OrderResponse response = stub.calculateTotal(request);

        System.out.println("Product: " + productId + "\nQuantity: " + quantity + "\nTotal: " + response.getTotalPrice());

        channel.shutdown();
    }
}
