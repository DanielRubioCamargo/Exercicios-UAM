import java.util.Scanner;

public class Exercicio2 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int number = scanner.nextInt();
        if(number >= 50 && number <= 100){
            System.out.println("Está no intervalo!");
        }
        else{
            System.out.println("Não está no intervalo!");
        }
    }

}
