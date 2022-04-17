public class Main {
	public static void main (String[] argv) {
		int initialTableLength = 10;
		
		cabbage.TableCreator tc = new cabbage.TableCreator();
		float[] table = tc.creator(initialTableLength);

		cabbage.DataProcessor dp1 = new cabbage.DataProcessor(new cabbage.DefaultPrint(), new cabbage.BubbleSort());
		cabbage.DataProcessor dp2 = new cabbage.DataProcessor(new cabbage.DefaultPrint(), new cabbage.SelectionSort());
		cabbage.DataProcessor dp3 = new cabbage.DataProcessor(new cabbage.DefaultPrint(), new cabbage.MergeSort());
		System.out.println("Initial array:");
		dp1.print(table);
		dp1.combiner(table.clone());
		dp2.combiner(table.clone());
		dp3.combiner(table.clone());
	}
}