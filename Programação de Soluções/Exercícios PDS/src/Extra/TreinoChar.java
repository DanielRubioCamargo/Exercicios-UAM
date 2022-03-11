package Extra;

import java.util.Scanner;

public class TreinoChar {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Digite um número para ser convertido em um caracter da tabela ASCII : ");
        int number = scanner.nextInt();
        char convertedChar = convert_number_to_char(number);
        System.out.println("O número " + number + " corresponde ao caracter " + convertedChar);
    }

    public static char convert_number_to_char(int number){
        return (char)number;
    }

}
