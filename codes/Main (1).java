import java.util.ArrayList;
import java.util.Scanner;


class Element
{
   private int num;

   public Element(int n1) 
   {
       this.num = n1;
   }
   
   public int GetElem()
   {
	   return this.num;
   }
}

public class Main {

   public static void main(String[] args) 
   {

		ArrayList<Element> list = new ArrayList<Element>();
		Element first = new Element(1);
		Element second = new Element(2);
		Element third = new Element(3);
		
		list.add(first);
		list.add(second);
		list.add(third);
		
		System.out.println("vvedite chislo dlya poiska v spiske");
		Scanner scanner = new Scanner(System.in);
		int a = scanner.nextInt();
		
		int f = 0;
		
		for(int i=0; i<list.size(); i++)
		{
			if (list.get(i).GetElem() == a)
			{
				System.out.println("chislo naideno");
				
				System.out.println("vvedite chislo dlya dobavleniya");
				
				a = scanner.nextInt();
				list.add(i, new Element(a));
				break;
		
		}
		}
						
		System.out.println("Spisok ");
		for(int i=0; i<list.size(); i++)
		{
			System.out.println(list.get(i).GetElem());
		}

   }
}
