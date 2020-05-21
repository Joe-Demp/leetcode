package leetcode.minimumPathSum;

public class Main {
    public static final int[][] grid = {
            {1, 3, 1},
            {1, 5, 1},
            {4, 2, 1}
    };

    public static void main(String[] args) {
        int result = new MinimumPathSum().minPathSum(grid);
        System.out.println(result);
    }
}
