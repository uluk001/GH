public class IsEven {
    public static void main(String[] args) {
        int[] nums = {1, 2, 3, 4, 5};
        for (int num : nums) {
            printResult(num, isEven(num));
        }
    }

    protected static boolean isEven(int num) {
        return num % 2 == 0;
    }

    protected static void printResult(int number, boolean isEven) {
        if (isEven) {
            System.out.printf("%s is even\n", number);
        } else {
            System.out.printf("%s is not even\n", number);
        }
    }
}