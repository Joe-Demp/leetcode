package leetcode.findMaxLength;

import java.util.Random;

public class OneZeroArray {
    private static final int UPPER_BOUND = 2;

    private static final int DEFAULT_LENGTH = 10;
    private static final int DEFAULT_SEED = 1920;

    public static int[] makeDefault() {
        int[] array = new int[DEFAULT_LENGTH];
        Random rand = new Random(DEFAULT_SEED);

        for (int i = 0; i < array.length; ++i) {
            array[i] = rand.nextInt(UPPER_BOUND);
        }
        return array;
    }
}
