package cabbage;

public class TableCreator {
	private NumberGenerator ng = new NumberGenerator();

	public float[] creator(int length) {
		float[] table = new float[length];
		for(int i = 0; i < table.length; i++) {
			table[i] = ng.generator();
		}
		return table;
	}
}