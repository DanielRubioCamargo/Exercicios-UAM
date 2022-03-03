import java.util.Scanner;

public class Exercicio3 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        float n1 = scanner.nextFloat();
        float n2 = scanner.nextFloat();
        float n3 = scanner.nextFloat();
        float higher = 0.0f;
        float medium = 0.0f;
        float lower = 0.0f;

        if(n1 == n2 && n2 == n3){
            higher = n1;
            medium = n2;
            lower = n3;
        }
        else if(n1 > n2 && n1 > n3){
            higher = n1;
            if(n2 > n3){
                medium = n2;
                lower = n3;
            }
            else{
                medium = n3;
                lower = n2;
            }
        }
        else if(n2 > n1 && n2 > n3){
            higher = n2;
            if(n1 > n3){
                medium = n1;
                lower = n3;
            }
            else{
                medium = n3;
                lower = n1;
            }
        }
        else if(n3 > n1 && n3 > n2) {
            higher = n3;
            if (n1 > n2) {
                medium = n1;
                lower = n2;
            } else {
                medium = n2;
                lower = n1;
            }
        }
        System.out.println(higher + " > " + medium + " > " + lower);
    }

}
