import java.util.Random;

public class Main {

    static BinaryOrderedTree<Integer> dataStructure = new BinaryOrderedTree<>();
    public static void main(String[] args) throws Exception {

        testInsert(5);
        dataStructure.inorder();
        System.out.println("\n"+dataStructure.findSum() +" - cумма всех елементов");
        System.out.println();
        testInsert(1000);
        testFindElement(1000);
        testDelete(1000);
        System.out.println();
        testInsert(10_000);
        testFindElement(10_000);
        testDelete(10_000);
        System.out.println();
        testInsert(100_000);
        testFindElement(100_000);
        testDelete(100_000);
    }
    public static void testInsert(int times) throws Exception {
        long start  = System.nanoTime();
        Random random = new Random(10);
        for (int i = 0; i < times; i++) {
            dataStructure.insert(random.nextInt());
        }
        System.out.printf("Добавление %d элементов в дерево заняло: %d наносекунд\n",times,System.nanoTime()-start);
    }
    public static void testDelete(int times) throws Exception {
        long start  = System.nanoTime();
        Random random = new Random(10);
        for (int i = 0; i < times; i++) {
            dataStructure.delete(random.nextInt());
        }
        System.out.printf("Удаление %d элементов в дереве заняло: %d наносекунд\n",times,System.nanoTime()-start);
    }
    public static void testFindElement(int times) throws Exception {
        long start  = System.nanoTime();
        Random random = new Random(10);
        for (int i = 0; i < times; i++) {
            dataStructure.searchByValue(random.nextInt());
        }
        System.out.printf("Нахождение  %d элементов по их значению в дереве заняло: %d наносекунд\n",times,System.nanoTime()-start);
    }
}
