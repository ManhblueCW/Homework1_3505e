import java.rmi.*;
import java.rmi.server.*;
import java.sql.*;

public class OrderProcessingImpl extends UnicastRemoteObject implements OrderProcessing {
    protected OrderProcessingImpl() throws RemoteException {}

    public double calculateTotal(String productId, int quantity) throws RemoteException {
        double price = 0;
        try {
            Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/blackmarket", "root", "M@nhbh12345");
            PreparedStatement stmt = conn.prepareStatement("SELECT price FROM products WHERE product_id = ?");
            stmt.setString(1, productId);
            ResultSet rs = stmt.executeQuery();

            if (rs.next()) {
                price = rs.getDouble("price");
            }
            conn.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
        return price * quantity;
    }
}
