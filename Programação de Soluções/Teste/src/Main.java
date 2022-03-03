import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        float number = scanner.nextFloat();
        scanner.close();
        if (number > 20.0f){
            System.out.println(number/2.0);
        }

    }

}
