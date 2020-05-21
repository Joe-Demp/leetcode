package leetcode.findMaxLength;

import java.util.*;

public class FindMaxLength {
    // map of counts to minimum indices
    public Map<Integer,Integer> map = new HashMap<>();
    public int maxSize = 0;

    public void setMaxSize(int newMax) {
        maxSize = Math.max(maxSize, newMax);
    }

    public boolean noBetterLengthPossible(int index) {
        return index < maxSize;
    }

    public FindMaxLength() {
        // the earliest location of a count of 0 is at index -1
        map.put(0, -1);
    }

    public int findMaxLength(int[] nums) {
        if (nums.length < 2) {
            return 0;
        }

        int[] counts = getCounts(nums);

        int lastIndex = counts.length - 1;
        for (int i = lastIndex;
             i >= 0 && !map.isEmpty();
             i--) {
            int thisCount = counts[i];
            if (map.containsKey(thisCount)) {
                int earliestSisterIndex = map.remove(thisCount);
                setMaxSize(i - earliestSisterIndex);
            }

            if (noBetterLengthPossible(i)) break;
        }

        return maxSize;
    }

    public int[] getCounts(int[] nums) {
        int[] counts = new int[nums.length];
        counts[0] = value(nums[0]);
        checkAndAddCountIndexToMap(counts[0], 0);

        for (int i = 1; i < counts.length; i++) {
            counts[i] = counts[i - 1] + value(nums[i]);
            checkAndAddCountIndexToMap(counts[i], i);
        }

        return counts;
    }

    public int value(int k) {
        return k == 1 ? 1 : -1;
    }

    public void checkAndAddCountIndexToMap(int count, int index) {
        if (map.containsKey(count)) {
            return;
        }
        map.put(count, index);
    }
}
