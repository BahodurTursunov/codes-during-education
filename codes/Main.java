import java.util.ArrayList;
import java.util.Scanner;


class ElementofList
{
   public int num;

   public ElementofList(int n1) 
   {
       this.num = n1;
   }
   
}

public class Main {

   public static void main(String[] args) 
   {

		ArrayList<ElementofList> list = new ArrayList<ElementofList>();
		ElementofList first = new ElementofList(1);
		ElementofList second = new ElementofList(2);
		ElementofList third = new ElementofList(3);
		
		list.add(first);
		list.add(second);
		list.add(third);
		
		System.out.println("Spisok ");

		
		for(int i=0; i<list.size(); i++)
		{
			System.out.println(list.get(i).num);
		}
		
		
		System.out.println("vvedite chislo dlya dobavleniya v nachalo");
		Scanner scanner = new Scanner(System.in);
		int a = scanner.nextInt();
		
		list.add(0, new ElementofList(a));
		
		System.out.println("Spisok ");

		for(int i=0; i<list.size(); i++)
		{
			System.out.println(list.get(i).num);
		}
		
						
   }
}
