public class Main {
	public static void main (String[] argv) {
		int initialTableLength = 10;
		
		cabbage.TableCreator tc = new cabbage.TableCreator();
		float[] table = tc.creator(initialTableLength);

		cabbage.DataProcessor dp1 = new cabbage.DataProcessor(new cabbage.DefaultPrinter(), new cabbage.BubbleSort());
		dp1.print(table);
	}
}