package leetcode.binaryTreeDiameter;

public class BinaryTreeDiameter {
    public int diameterOfBinaryTree(TreeNode root) {
        if (root == null) {
            return 0;
        }

        int diameterAtRoot = treeDepth(root.left) + treeDepth(root.right);
        return Math.max(
                Math.max(diameterOfBinaryTree(root.left), diameterOfBinaryTree(root.right)),
                diameterAtRoot);
    }

    public int treeDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        return 1 + Math.max(treeDepth(root.left), treeDepth(root.right));
    }

    /**
     * Definition for a binary tree node.
     * public class TreeNode {
     * int val;
     * TreeNode left;
     * TreeNode right;
     * TreeNode() {}
     * TreeNode(int val) { this.val = val; }
     * TreeNode(int val, TreeNode left, TreeNode right) {
     * this.val = val;
     * this.left = left;
     * this.right = right;
     * }
     * }
     */
    public interface TreeNode {
        TreeNode left = null;
        TreeNode right = null;
    }
}
