// Shopping Cart

// Класс Product (название, цена)
// Добавить/удалить товары
// Общая сумма, самый дорогой товар
// Применяет: объекты, ArrayList, расчёты
public class Product {
    String productName;
    double price;

    public Product(String productName, double price) {
        this.productName = productName;
        this.price = price;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || obj.getClass() != getClass()) return false;

        Product product = (Product) obj;
        return Double.compare(product.price, price) == 0 && productName.equals(product.productName);
    }
}
