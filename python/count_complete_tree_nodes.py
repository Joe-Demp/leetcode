
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def treeCount(root):
    if not root: return 0

    return 1 + treeCount(root.left) + treeCount(root.right)

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        return treeCount(root)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
# root.right.left = TreeNode(6)


result = Solution().countNodes(root)

print(result)
