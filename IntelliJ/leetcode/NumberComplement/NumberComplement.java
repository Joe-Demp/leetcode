package leetcode.NumberComplement;

public class NumberComplement {
    public int findComplement(int num) {
        if (num < 2) {
            return num == 1 ? 0 : 1;
        }
        int a = num;
        int b = 0;
        while (a > 0) {
            a >>>= 1;
            b <<= 1;
            b |= 1;
        }
        return num ^ b;
    }
}
