import java.util.Scanner;

public class Exercicio1 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Digite um número : ");
        int number1 = scanner.nextInt();
        System.out.print("Digite outro número : ");
        int number2 = scanner.nextInt();
        if(number1 == number2){
            System.out.println("São iguais!");
        }
        else{
            int difference = Math.abs(number1 - number2);
            System.out.println("Diferença : " + difference);
        }
    }
}
