package leetcode.NumberComplement;

public class Main {
    static int[] inputs = {0, 1, 2, 3, 4, 45};

    public static void main(String[] args) {
        for (int i : inputs) {
            runTest(i);
        }
    }

    public static void runTest(int in) {
        int result = new NumberComplement().findComplement(in);
        System.out.printf("in: %d, out: %d", in, result);
    }
}
