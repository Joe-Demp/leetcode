package leetcode.moveZeroes;

import org.jetbrains.annotations.NotNull;

public class MoveZeroes {
    private int[] arr;

    public void moveZeroes(int[] nums) {
        arr = nums;
        zeroSort(0, nums.length);
    }

    public int zeroSort(int min, int max) {
        if (max - min == 1) {
            return (arr[min] == 0) ? min : max;
        }

        int medianIndex = (max + min) / 2;
        int leftRmostZero = zeroSort(min, medianIndex);
        int rightRmostZero = zeroSort(medianIndex, max);

        return merge(leftRmostZero, medianIndex, rightRmostZero);
    }

    public int merge(int leftRmostZero, int startRarray, int rightRmostZero) {
        int i = leftRmostZero, j = startRarray, k = rightRmostZero;
        while (i < j && j < k) {
            swap(i, j);
            i++;
            j++;
        }
        if (j == k) {
            return i;
        } else {
            return k;
        }
    }

    public void swap(int i, int j) {
        int tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
    }
}
