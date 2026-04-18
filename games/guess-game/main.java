import java.util.*;
import javax.swing.*;
import java.awt.color.*;

public class main {

    public static void main(String[] args) {

        // variables for image window
        final int width = 250;
        final int height = 250;

        // objects
        JFrame window = new JFrame();
        Scanner sc = new Scanner(System.in);
        Random rx = new Random();
        ImageIcon img = new ImageIcon("1.jpg");// replace 1.jpg with image location
        JLabel lb = new JLabel(img);

        System.out.println("Enter a number from 1 to 10 to try:");
        int in = sc.nextInt();
        if (in > 0 && in < 10) { // out of scope check
            int x = rx.nextInt(10) + 1;
            System.out.println(x);
            if (in == x) {
                System.out.println("same");
                window.setSize(width, height);
                window.setVisible(true);
                window.setResizable(false);
                window.setLocationRelativeTo(null);
                window.setAlwaysOnTop(true);
                window.setTitle("You won!!");
                window.add(lb);
            } else {
                System.out.println("not same! Try Again.");
            }
        } else {
            System.out.println("Enter a valid input");
        }

    }

}
