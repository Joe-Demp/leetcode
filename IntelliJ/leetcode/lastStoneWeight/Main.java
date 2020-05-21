package leetcode.lastStoneWeight;

public class Main {
    static int[] stones = {2, 7, 4, 1, 8, 1};

    public static void main(String[] args) {
        int finalStone = new LastStoneWeight().lastStoneWeight(stones);
        System.out.println(finalStone);
    }
}
