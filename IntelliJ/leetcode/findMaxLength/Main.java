package leetcode.findMaxLength;

import java.util.Arrays;

public class Main {
    public static final int[] numbers = {1, 0, 0, 0, 1, 0, 1, 1, 0};

    public static void main(String[] args) {
        int maxLength = new FindMaxLength().findMaxLength(numbers);
        System.out.println(maxLength);
    }
}
