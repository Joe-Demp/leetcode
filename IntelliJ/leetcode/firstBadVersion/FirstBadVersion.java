package leetcode.firstBadVersion;

public class FirstBadVersion {
    /*
    Find n where isBadVersion(n - 1) = false and isBadVersion(n) = true
     */

    public int firstBadVersion(int n) {
        long greatestGoodVersion = 0L;
        long smallestBadVersion = n;

        while ((smallestBadVersion - greatestGoodVersion) > 1) {
            long partition = (smallestBadVersion + greatestGoodVersion) / 2;

            if (isBadVersion((int) partition)) {
                smallestBadVersion = partition;
            } else {
                greatestGoodVersion = partition;
            }
        }
        return (int) smallestBadVersion;
    }

    public FirstBadVersion(int firstBadVersion) {
        this.fBV = firstBadVersion;
    }

    private int fBV;

    private boolean isBadVersion(int version) {
        return version >= fBV;
    }
}
