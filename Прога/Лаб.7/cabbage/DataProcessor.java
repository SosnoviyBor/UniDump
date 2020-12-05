package cabbage;

public class DataProcessor {
    private Printer printer;
    private SortChooser algorithm;

    public DataProcessor(Printer printer, SortChooser algorithm) {
        this.printer = printer;
        this.algorithm = algorithm;
    }
    public void print(float[] list) {
        printer.print(list);
    }
    public void sort(float[] list) {
        algorithm.sort(list);
	}
	public void combiner(float[] list) {
        System.out.println("\n Let`s sort our array with "+algorithm.toString());
        sort(list);
        print(list);
	}
}
