package com.company;

//Регулярные выражения. Дана строка с текстом на русском языке, в которой автор неправильно расставил пробелы перед
// запятыми. Например, Это строка , у которой зачем-то написаны два пробела перед запятой. Нужно найти все пробельные
// символы перед запятыми и удалить их. Должно получиться Это строка, у которой зачем-то написаны два пробела перед запятой.
// Используйте метод replaceAll() класса String.

public class Main {

    public static void probeli(String str){
        String string = str.replaceAll("\\s+", " ");
        String new_string = string.replaceAll("\\s,", ",");
        System.out.println(new_string);
    }

    public static void main(String[] args) {
	String str = "Это строка ,   у которой зачем-то     написаны два пробела перед запятой.";
	probeli(str);
    }
}
