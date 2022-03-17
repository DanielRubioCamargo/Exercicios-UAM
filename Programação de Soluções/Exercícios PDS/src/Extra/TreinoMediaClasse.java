package Extra;

import java.util.Scanner;

public class TreinoMediaClasse {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double[][] grades = new double[5][2];
        double[] totalGrade = new double[5];
        double classCont = 0.0;
        double classGrade;
        int classmateNumber = 0;
        for(int i = 0; i < 5; i++) {
            classmateNumber += 1;
            System.out.println("---------------------------");
            System.out.println("\t\t" + classmateNumber + "º aluno");
            System.out.println("---------------------------");
            for (int j = 0; j < 2; j++) {
                System.out.print("Digite a primeira nota : ");
                grades[i][j] = scanner.nextDouble();
            }
            totalGrade[i] = (grades[i][0] + grades[i][1]) / 2;
            classCont+=totalGrade[i];
            System.out.println("Média do aluno(a) : " + totalGrade[i]);
            System.out.println("---------------------------");
        }

        classGrade = classCont / 5;

        System.out.println("Média da sala : " + classGrade);
    }

}
