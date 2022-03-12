package Extra;

import java.util.Scanner;

public class TreinoChar2 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Insira um texto : ");
        String word = scanner.nextLine();
        char firstLetter = word.charAt(0);
        System.out.println("A primeira letra da palavra escrita é : " + firstLetter);
        System.exit(0);

    }

}
