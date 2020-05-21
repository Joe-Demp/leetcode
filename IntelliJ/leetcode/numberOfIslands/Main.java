package leetcode.numberOfIslands;

public class Main {
    public static char[][] ocean = Ocean.OCEAN;

    public static void main(String[] args) {
        System.out.printf("length = %d width = %d", ocean.length, ocean[0].length);

        long start = System.currentTimeMillis();
        int result = new NumberOfIslands().numIslands(ocean);
        long end = System.currentTimeMillis();

        System.out.println(result);
        System.out.printf("Time = %d\n", end - start);
    }
}
