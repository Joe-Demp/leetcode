package leetcode.productExceptSelf;

public class ProductExceptSelf {
    public int[] productExceptSelf(int[] nums) {
        int[] rightProducts = makeRightProducts(nums);
        int leftProduct = 1;

        int[] answer = new int[nums.length];
        for (int i = 0; i < answer.length; i++) {
            answer[i] = leftProduct * rightProducts[i + 1];
            leftProduct *= nums[i];
        }

        return answer;
    }

    public int[] makeRightProducts(int[] nums) {
        int[] rightProducts = new int[nums.length + 1];
        int lastIndex = rightProducts.length - 1;

        rightProducts[lastIndex] = 1;
        for (int i = lastIndex - 1; i >= 0; i--) {
            rightProducts[i] = rightProducts[i + 1] * nums[i];
        }
        return rightProducts;
    }
}
