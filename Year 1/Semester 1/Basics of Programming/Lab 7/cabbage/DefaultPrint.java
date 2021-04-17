package cabbage;

public class DefaultPrint implements Printer{
    @Override
    public void print(float[] table) {
        for (float i: table) {
            System.out.print(i+"\n");
        }
	}
}