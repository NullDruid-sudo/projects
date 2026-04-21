package passgen;
import java.awt.Color;
import java.util.*;
import javax.swing.*;
public class pin {

	public static void main(String[] args) {
		
		Scanner scan =new Scanner(System.in);
		Random rand = new Random();
		JFrame window = new JFrame("Pin Generator");
		JLabel text = new JLabel();
		int pass=4;
		int n=1;
		int pin=0;
		while(n<=pass) {
			pin*=10;
			pin+=rand.nextInt(10);
			n++;
			
		}
		//System.out.println("\n5");
		System.out.println(pin);
		
		window.setSize(500,100);
		window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    window.setResizable(false);
    window.setLocationRelativeTo(null);
    window.setVisible(true);
		window.setBackground(Color.black);
		window.add(text);
		text.setText("Your 4 digit pin is : "+ String.valueOf(pin));
			
	}

}
