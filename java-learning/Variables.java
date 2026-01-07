public class Variables {
    public static void main(String[] args) {
        int x = 5;
        int y = 5;
        System.out.println(x == y);

        String name1 = new String("Uluk");
        String name2 = new String("Uluk");
        System.out.println(name1 == name2);
        System.out.println(name1.equals(name2));
    }
}