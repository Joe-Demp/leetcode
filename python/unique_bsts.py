unique_bsts = {0: 1, 1: 1}

def count_trees(num_nodes):
    if num_nodes in unique_bsts:
        return unique_bsts[num_nodes]

    total_num_trees = 0
    for i in range(num_nodes):
        total_num_trees += count_trees(i) * count_trees(num_nodes - 1 - i)

    unique_bsts[num_nodes] = total_num_trees
    return total_num_trees

class Solution:
    def numTrees(self, n: int) -> int:
        if not n: return 1
        return count_trees(n)

print(Solution().numTrees(1))
print(Solution().numTrees(2))
print(Solution().numTrees(3))
print(Solution().numTrees(4))
print(Solution().numTrees(5))
print(Solution().numTrees(6))
