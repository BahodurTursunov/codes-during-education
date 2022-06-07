package com.company;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

//Регулярные выражения. Дана строка, проверьте, что в ней содержится корректный email адрес. Будем считать,
// что корректный email состоит из имени пользователя (несколько латинских букв, точек, подчеркиваний, минусов),
// далее следует символ @, далее идет домен (тоже несколько латинских букв, точек, подчеркиваний, минусов),
// в конце должна быть точка и от двух до четырех латинских букв. Т.е. конец должен выглядеть как .com, .ru и т.п.
// Помните, что обычная точка означает любой символ, и ее может понадобиться экранировать. Используйте метод matches()
// класса String

public class Main {

    public static boolean correct(String str){
        Pattern pattern = Pattern.compile("^[_A-Za-z0-9]+(\\.[_A-Za-z0-9-]+)*@[A-Za-z]+\\.[A-Za-z]{2,}$");
        Matcher matcher = pattern.matcher(str);
        if (matcher.find()){
            return true;
        }
        return false;
    }


    public static void main(String[] args) {
	String email = "abdyl@mail.ru";
	System.out.println(correct(email));
    }
}
