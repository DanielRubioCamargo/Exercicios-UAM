package Extra;

import java.util.Scanner;

public class TreinoExtra {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        byte[][] matrix = new byte[3][3];
        System.out.println("Digite 9 valores : ");
        for(int i = 0; i < 3; i++){
            for(int j = 0; j < 3; j++){
                matrix[i][j] = scanner.nextByte();
            }
        }
        for(int i = 0; i < 3; i++){
            for(int j = 0; j < 3; j++){
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println();
        }
    }

}
