package com.company;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

//Дан файл. Прочитайте из него все целые числа и выведите на экран их сумму.
//Измените метод так, чтобы он игнорировал все слова, которые не являются целыми числами.
// (используйте hasNextInt(), не используйте scanner.useDelimiter()).

public class Main {

    public static void read_sum () throws IOException {
    int sum = 0;
        List<String> list = new ArrayList<String>();
        Scanner in = new Scanner(new File("C:/Users/numbers.txt"));
        while (in.hasNextLine())
            list.add(in.nextLine());
        for (String line : list){
            Pattern pattern = Pattern.compile("\\b\\d\\b");
            Matcher matcher = pattern.matcher(line);
            while (matcher.find()){
                int number = Integer.parseInt(line.substring(matcher.start(), matcher.end()));
                sum +=number;

            }

        }

        System.out.println(sum);
    }


    public static void main(String[] args) throws IOException{
	read_sum();
    }
}
