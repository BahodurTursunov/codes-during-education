package com.company;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;



//Дан массив строк lines и имя файла. Запишите в файл заданные строки построчно. Не забудьте, что есть цикл “for each”.

public class Main {

    public static void write (String[] lines) throws IOException {



            FileOutputStream fileOutputStream = new FileOutputStream("C:/Users/запись/write.txt", true);

           for (String str : lines){
               str +="\n";
               fileOutputStream.write(str.getBytes());
           }


            fileOutputStream.close();



    }


    public static void main(String[] args)  throws IOException {
    String[] lines = new String[] {"one, two", "three", "four"};
    write(lines);
    }
}
