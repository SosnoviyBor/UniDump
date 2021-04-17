package cabbage;

import java.util.Random;

public class NumberGenerator {
	float generator() {
		float min = -20;
		float max = 20;
		Random randomFloat = new Random();
		return randomFloat.nextFloat() * (max - min) + min;
	}
}
