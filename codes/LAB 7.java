package com.company;

import java.util.Arrays;

public class Main {

    private static char[][] createTable(int i, char c) {
        char [][] Table = new char[i][i];
        for (int j = 0; j < i; j++){
            Arrays.fill(Table[j], c);
        }return Table;
    }

    private static void fillFirstAndLastLines(char[][] Table, char c) {
        Arrays.fill(Table[0], c);
        Arrays.fill(Table[Table.length - 1], c);
    }

    private static void printTable(char[][] Table) {
        for (int i = 0; i < Table.length; i++) {
            for (int j = 0; j < Table[0].length; j++) {
                System.out.print(Table[i][j] + " ");
            }
            System.out.println();
        }
    }


    private static void fillFirstAndLastColumns(char[][] Table, char c) {
        for (int i = 0; i < Table.length; i++) {
            Table[i][0] = c;
            Table[i][Table[0].length - 1] = c;
        }
    }

    public static void main(String[] args) {

        char[][] c = createTable(20, '.');
        printTable(c);

        System.out.println("");
        System.out.println("============ Заполним строки: ==========");
        fillFirstAndLastLines(c, '#');
        printTable(c);

        System.out.println("");
        System.out.println("============ Заполним столбцы: =========");
        fillFirstAndLastColumns(c, '#');
        printTable(c);

    }


}
