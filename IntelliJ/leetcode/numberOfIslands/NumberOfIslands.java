package leetcode.numberOfIslands;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

public class NumberOfIslands {
    char[][] sea;
    int countIslands = 0;
    Queue<int[]> landToVisit = new LinkedList<>();

    public static final char LAND = '1';
    public static final char VISITED = 'V';

    public int numIslands(char[][] grid) {
        if (grid.length == 0 || grid[0].length == 0) {
            return 0;
        }
        sea = grid;

        for (int row = 0; row < sea.length; row++) {
            for (int col = 0; col < sea[row].length; col++) {
                if (visitable(row, col)) {
                    doBfs(row, col);
                }
            }
        }
        return countIslands;
    }

    public void doBfs(int row, int col) {
        mark(row, col);
        landToVisit.add(new int[]{row, col});
        countIslands++;

        while (!landToVisit.isEmpty()) {
            int[] current = landToVisit.poll();

            int[][] nextSquares = new int[][]{
                    above(current), below(current), right(current), left(current)
            };
            for (int[] square : nextSquares) {
                addIfVisitable(square[0], square[1], landToVisit);
            }
        }
    }

    int[] above(int[] target) { return new int[]{target[0] - 1, target[1]}; }
    int[] below(int[] target) { return new int[]{target[0] + 1, target[1]}; }
    int[] right(int[] target) { return new int[]{target[0], target[1] + 1}; }
    int[] left(int[] target) { return new int[]{target[0], target[1] - 1}; }

    public void addIfVisitable(int row, int col, Queue<int[]> squares) {
        if (visitable(row, col)) {
            mark(row, col);
            squares.add(new int[]{row, col});
        }
    }

    public boolean visitable(int row, int col) {
        if (inRange(row, col)) {
            return sea[row][col] == LAND;
        }
        return false;
    }

    public boolean inRange(int row, int col) {
        return 0 <= row && row < sea.length  && 0 <= col && col < sea[0].length;
    }

    public void mark(int row, int col) {
        sea[row][col] = VISITED;
    }
}
