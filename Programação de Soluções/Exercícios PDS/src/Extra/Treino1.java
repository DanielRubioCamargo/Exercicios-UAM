package Extra;

import java.util.Scanner;

public class Treino1 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Digite o valor de x1 : ");
        float x1 = scanner.nextFloat();
        System.out.print("Digite o valor de y1 : ");
        float y1 = scanner.nextFloat();
        System.out.print("Digite o valor de x2 : ");
        float x2 = scanner.nextFloat();
        System.out.print("Digite o valor de y2 : ");
        float y2 = scanner.nextFloat();

        double distance = Math.sqrt(Math.pow((x1-x2),2) + Math.pow((y1-y2),2));

        //System.out.println("A distância entre esses dois pontos é de " + distance + " pixels");
        System.out.printf("A distância entre esses dois pontos é de %.2f pixels",distance);

    }

}
