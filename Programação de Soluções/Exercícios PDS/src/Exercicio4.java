import java.util.Scanner;

public class Exercicio4 {

    // Calculadora com switch case

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("[1] Somar\n[2] Subtrair\n[3] Multiplicar\n[4] Dividir");
        System.out.print("Escolha a opção desejada : ");
        byte option = scanner.nextByte();
        System.out.print("Insira o primeiro número : ");
        int n1 = scanner.nextInt();
        System.out.print("Insira o segundo número : ");
        int n2 = scanner.nextInt();
        int result;

        switch(option){
            case 1:
                result = n1 + n2;
                System.out.println("Resultado da soma : " + result);
                break;
            case 2:
                result = n1 - n2;
                System.out.println("Resultado da subtração : " + result);
                break;
            case 3:
                result = n1 * n2;
                System.out.println("Resultado da multiplicação : " + result);
                break;
            case 4:
                result = n1 / n2;
                System.out.println("Resultado da divisão : " + result);
                break;
            default:
                System.out.println("Erro, valor fora do limite!");
        }

    }

}
