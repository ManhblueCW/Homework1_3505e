import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class Server {
    public static void main(String[] args) {
        try {
            System.setProperty("java.rmi.server.hostname", "192.168.0.95");
            OrderProcessing service = new OrderProcessingImpl();
            Registry registry = LocateRegistry.createRegistry(1099);
            registry.rebind("OrderService", service);
            System.out.println("RMI Server is running...");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}