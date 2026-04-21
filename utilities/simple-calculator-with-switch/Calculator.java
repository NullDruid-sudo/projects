import java.util.Scanner;

public class Calculator {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        System.out.println("Calculator \n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Remainder");
        int choice = scanner.nextInt();
        System.out.println("first number: ");
        int num1 = scanner.nextInt();
        System.out.println("second number: ");
        int num2 = scanner.nextInt();

        switch (choice) {
            case 1:
                System.out.println(num1 + " + " + num2 + " = " + (num1 + num2));
                break;
            case 2:
                System.out.println(num1 + " - " + num2 + " = " + (num1 - num2));
                break;
            case 3:
                System.out.println(num1 + " x " + num2 + " = " + (num1 * num2));
                break;
            case 4:
                if (num2 != 0) {
                    System.out.println(num1 + " / " + num2 + " = " + (num1 / num2));
                } else {
                    System.out.println("Error! zero is not allowed.");
                }
                break;
            case 5:
                System.out.println(num1 + " % " + num2 + " = " + (num1%num2));
                break;
            default:
                System.out.println("Invalid ");
        }
    }
}