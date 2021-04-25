import java.util.Scanner;

public class BinaryHeapTest
{
    public static void main(String[] args)
    {
        Scanner scan = new Scanner(System.in);

        System.out.println("Binary Heap Test\n\n");
        System.out.println("Enter size of Binary heap");
        BinaryHeap bh = new BinaryHeap(scan.nextInt() );

        System.out.println("\nChoose filling method\n");
        System.out.println("1. empty");
        System.out.println("2. sorted");
        System.out.println("3. random");

        int choice1 = scan.nextInt();
        switch (choice1) {
            case 1:
                System.out.println("Heap remains empty");
                break;

            case 2:
                try {
                    System.out.println("Enter first integer element");
                    bh.sortedFill(scan.nextInt());
                }
                catch (Exception e) {
                    System.out.println(e.getMessage());
                }
                break;

            case 3:
                try {
                    System.out.println("Enter max and max values. Example: \"4 90\"");
                    String kostyl = scan.nextLine();
                    bh.randomFill(scan.nextLine());
                }
                catch (Exception e) {
                    System.out.println(e.getMessage());
                }
                break;

            default:
                System.out.println("Wrong input. Heap remains empty");
                break;
        }

        char ch;
        do {
            System.out.println("\nBinary Heap Operations\n");
            System.out.println("1. insert ");
            System.out.println("2. delete");
            System.out.println("3. get index by value");
            System.out.println("4. sorted view");
            System.out.println("5. check full");
            System.out.println("6. check empty");
            System.out.println("7. clear");

            int choice2 = scan.nextInt();
            switch (choice2) {
                case 1 :
                    try {
                        System.out.println("Enter integer element to insert");
                        bh.insert( scan.nextInt() );
                    }
                    catch (Exception e) {
                        System.out.println(e.getMessage() );
                    }
                    break;

                case 2 :
                    try {
                        System.out.println("Element : "+ bh.delete(scan.nextInt()));
                    }
                    catch (Exception e) {
                        System.out.println(e.getMessage() );
                    }
                    break;

                case 3:
                    try {
                        System.out.println("Enter integer to be found");
                        int val = scan.nextInt();
                        int pos = bh.findPosition(val);
                        System.out.println("Value " + val + " is stored at position: " + pos);
                    }
                    catch (Exception e) {
                        System.out.println(e.getMessage());
                    }
                    break;

                case 4:
                    bh.printSorted();
                    break;

                case 5 :
                    System.out.println("Full status = "+ bh.isFull());
                    break;

                case 6 :
                    System.out.println("Empty status = "+ bh.isEmpty());
                    break;

                case 7 :
                    bh.makeEmpty();
                    System.out.println("Heap Cleared\n");
                    break;

                default :
                    System.out.println("Wrong Entry \n ");
                    break;
            }
            /** Display heap **/
            bh.printHeap();

            System.out.println("\nDo you want to continue (Type y or n) \n");
            ch = scan.next().charAt(0);
        } while (ch == 'Y'|| ch == 'y');
    }
}
