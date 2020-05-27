package leetcode.minimumPathSum;

public class MinimumPathSum {
    public int minPathSum(int[][] grid) {
        sumUp(grid);
        return grid[0][0];
    }

    public void sumUp(int[][] grid) {
        int height = grid.length - 1;
        int width = grid[0].length - 1;

        for (int row = height; row >= 0; row--) {
            for (int col = width; col >= 0; col--) {
                if (row != height && col != width) {
                    grid[row][col] = grid[row][col] + Integer.min(grid[row + 1][col], grid[row][col + 1]);
                } else if (row == height && col < width) {
                    grid[row][col] = grid[row][col] + grid[row][col + 1];
                } else if (col == width && row < height) {
                    grid[row][col] = grid[row][col] + grid[row + 1][col];
                }
            }
        }
    }
}
