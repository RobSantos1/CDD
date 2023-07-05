package Fundamentos;

public class String_Java {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String str = "Hello";
		String resultado = str.replace("l", "w");
		System.out.println(resultado);
		
		String phrase = "Hello World";
		String s1 = "Hello";
		String s2 = "HELLO";
		boolean b1 = s1.equals("Hello");
		boolean b2 = s1.equals(s2);
		boolean b3 = s1.equalsIgnoreCase(s2);
		boolean b4 = s1.equalsIgnoreCase("azul");
		
		
		String subString = phrase.substring(6);
		String interString = phrase.substring(3, 8);
		String espacoString = phrase.trim( );
		char caractString = phrase.charAt(1);
		
		
		
		
		System.out.println(subString);
		System.out.println(interString);
		System.out.println(espacoString);
		System.out.println(caractString);
		
		System.out.println("");
		
		System.out.println(s1);
		System.out.println(s2);
		System.out.println(b1);
		System.out.println(b2);
		System.out.println(b3);
		System.out.println(b4);
		
	}

}
