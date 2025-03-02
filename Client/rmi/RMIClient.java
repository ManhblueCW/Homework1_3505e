import java.rmi.registry.Registry;
import java.rmi.registry.LocateRegistry;

public class RMIClient {
    public static void main(String[] args) {
        try {
            Registry registry = LocateRegistry.getRegistry("192.168.0.95", 1099);
            OrderProcessing stub = (OrderProcessing) registry.lookup("OrderService");
            String productId = "P2";
            int quantity = 2;
            stub.calculateTotal(productId, quantity);
            // System.out.println("Product: " + productId + "\nQuantity: " + quantity + "\nPrice: " + stub.calculateTotal(productId, quantity));
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}