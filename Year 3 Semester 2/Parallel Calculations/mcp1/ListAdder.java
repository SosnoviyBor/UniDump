import java.util.ArrayList;

class IRanOutOfNames implements Runnable {
    private ArrayList<String> list;
    private ArrayList<String> text;

    public IRanOutOfNames(ArrayList<String> list, ArrayList<String> text) {
        this.list = list;
        this.text = text;
    }

    public void run() {
        synchronized(text) {
            for(String s : list) {
                text.add(s);
            }
        }
    }
}

// Головний клас
public class ListAdder {
    public static void main(String[] args) {
        ArrayList<String> text = new ArrayList<String>();
        ArrayList<String> list1 = new ArrayList<String>();
        ArrayList<String> list2 = new ArrayList<String>();
        ArrayList<String> list3 = new ArrayList<String>();

        // додати значення до списку list1, list2 та list3

        Thread thread1 = new Thread(new IRanOutOfNames(list1, text));
        Thread thread2 = new Thread(new IRanOutOfNames(list2, text));
        Thread thread3 = new Thread(new IRanOutOfNames(list3, text));

        thread1.start();
        thread2.start();
        thread3.start();

        try {
            thread1.join();
            thread2.join();
            thread3.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}
