package Fundamentos;
import java.util.Scanner;

public class percorrendo_array2 {
	public static void main(String[] args) {
		int[] numArray = new int[10];
		int[] Array2 = new int[10];
		int[] Array3 = new int[10];
		int[] Array4 = new int[10];
		
		
		Scanner scan = new Scanner(System.in);
		
		for(int i = 0 ; i < numArray.length; i++) {
			System.out.println("digite um numero:");
			numArray [i]= scan.nextInt();
		}
		
		System.out.println("______________________________");
		
		for (int j = 0; j < Array2.length; j++) {
			System.out.println("digite um numero:");
			Array2[j]= scan.nextInt();			
		}
		
		System.out.println("______________________________");

		for (int y = 0; y < Array3.length; y++) {
			System.out.println("digite um numero:");
			Array3 [y]= scan.nextInt();			
		}
		
		System.out.println("______________________________");
		for (int z = 0; z < Array4.length; z++) {
			System.out.println("digite um numero:");
			Array4 [z]= scan.nextInt();			
		}
		
		System.out.println("______________________________");
		
		for (int i : numArray) {
			System.out.print(i + " ");
		}
		
		System.out.println();
		
		for (int i : Array2) {
			System.out.print(i + " ");
		}
		
		System.out.println();
		
		for (int y : Array3) {
			System.out.print(y + " ");
		}
		
		System.out.println();
		
		for (int z : Array4) {
			System.out.print(z + " ");
			}
		
		scan.close();
	}
}
