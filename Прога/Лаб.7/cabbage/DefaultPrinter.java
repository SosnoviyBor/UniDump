package cabbage;

public class DefaultPrinter implements Printer{
    @Override
    public void print(float[] table) {
        for (float i: table) {
            System.out.print(i);
        }
        System.out.println();
	}
}