class TreeNode:
    pass
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # for the current node, invert the child nodes and then swap the pointers

    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return

        self.invertTree(root.left)
        self.invertTree(root.right)

        self.left, self.right = self.right, self.left
