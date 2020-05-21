package leetcode.firstBadVersion;

public class Main {
    public static void main(String[] args) {
        int firstBadVersion = 1702766719;
        int n = 2126753390;

        int result = new FirstBadVersion(firstBadVersion).firstBadVersion(n);

        System.out.println(result);
    }
}
