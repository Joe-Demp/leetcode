package leetcode.moveZeroes;

import java.util.Arrays;

public class Main {
    static int[] numbers = {0, 1, 0, 3, 12};

    public static void main(String[] args) {
        new MoveZeroes().moveZeroes(numbers);

        System.out.println(Arrays.toString(numbers));
    }
}
