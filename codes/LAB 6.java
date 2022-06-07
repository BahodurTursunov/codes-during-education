package com.company;
//Даны два файла. Прочитайте из первого файла текст и перепишите его во второй файл, исправив ошибки в регистрах букв
import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.Scanner;


public class Main {

    public static void registr () throws IOException {

        List<String> list = new ArrayList<String>();
        Scanner in = new Scanner(new File("C:/Users/registr/1.txt"));
        FileOutputStream fileOutputStream = new FileOutputStream("C:/registr/2.txt", true);
        while (in.hasNextLine())
            list.add(in.nextLine().replaceAll("\\s+", " "));
        for (String line : list){
            String[] words = line.split(" ");

            String word = "";
            word += words[0].substring(0, 1).toUpperCase(Locale.ROOT);
            word += words[0].substring(1).toLowerCase(Locale.ROOT);
            word += " ";
            fileOutputStream.write(word.getBytes());

            for (int i=1; i < words.length; i++)
            {
                String w = "";
                if (words[i-1].charAt(words[i-1].length() - 1 ) == '.' || words[i-1].charAt(words[i-1].length() - 1 ) == '!' || words[i-1].charAt(words[i-1].length() - 1 ) == '?'){
                    w += words[i].substring(0, 1).toUpperCase(Locale.ROOT);
                    w += words[i].substring(1).toLowerCase(Locale.ROOT);
                }
                else{
                    w += words[i].substring(0).toLowerCase(Locale.ROOT);
                }

                if (i == words.length - 1){
                    w += "\n";
                    fileOutputStream.write(w.getBytes());

            }
                else {
                    w += " ";
                    fileOutputStream.write(w.getBytes());
                }

            }

        }
        fileOutputStream.close();

    }


    public static void main(String[] args) throws IOException {
    registr();
    }
}
