// Shopping Cart

// Класс Product (название, цена)
// Добавить/удалить товары
// Общая сумма, самый дорогой товар
// Применяет: объекты, ArrayList, расчёты
import java.util.ArrayList;
import java.util.Arrays;

public class ShoppingCart {
    int id;
    ArrayList<Product> products;

    public ShoppingCart(int id, ArrayList<Product> products) {
        this.id = id;
        this.products = products;
    }

    public static void main(String[] args) {
        Product laptop = new Product("MacBook Pro 14", 1200);
        Product phone = new Product("Iphone 14", 755);
        Product headphones = new Product("Sony XM5", 300);
        Product powerbank = new Product("Samsung PWR 20000", 120);
        ShoppingCart cart1 = new ShoppingCart(1, new ArrayList<>(Arrays.asList(laptop, powerbank)));
        ShoppingCart cart2 = new ShoppingCart(1, new ArrayList<>(Arrays.asList(laptop, headphones, phone)));
        System.out.println(cart1.addProduct(powerbank));
        System.out.println(cart2.addProduct(powerbank));

        System.out.println(cart1.removeProduct(powerbank));
        System.out.println(cart2.removeProduct(powerbank));
        System.out.println(cart2.removeProduct(powerbank));

        System.out.println(cart1.getTotalSum());
        System.out.println(cart2.getTotalSum());

        Product expensive = cart2.getMostExpensiveProduct();
        if (expensive != null) {
            System.out.println(expensive.productName);
        }
    }

    protected boolean addProduct(Product product) {
        if (this.checkIfExist(product)) {
            System.err.println("this product is already in ur cart");
            return false;
        }
        this.products.add(product);
        return true;
    }

    protected boolean removeProduct(Product product) {
        if (!this.checkIfExist(product)) {
            System.err.println("this product wasn't added in ur cart");
            return false;
        }
        this.products.remove(product);
        return true;
    }

    protected boolean checkIfExist(Product product) {
        return this.products.contains(product);
    }

    protected double getTotalSum() {
        double totalSum = 0;
        for (Product product : this.products) {
            totalSum += product.price;
        }
        return totalSum;
    }

    public Product getMostExpensiveProduct() {
        if (this.products.size() < 1) return null;
        Product mostExpensiveProduct = this.products.get(0);
        for (Product product : this.products) {
            if (product.price > mostExpensiveProduct.price) mostExpensiveProduct = product;
        }
        return mostExpensiveProduct;
    }
}
