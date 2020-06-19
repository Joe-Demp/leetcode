from typing import List
from collections import defaultdict

class SlowSolution:
    def canJump(self, nums: List[int]) -> bool:
        # origins[x] = a list of the indices that can reach x by jump
        if not nums: return False
        elif len(nums) == 1: return True

        origins = defaultdict(list)
        pos_stack = [len(nums) - 1]

        for i, jump_length in enumerate(nums):
            for j in range(jump_length):
                origins[i + j + 1].append(i)

        while pos_stack:
            curr = pos_stack.pop()
            for origin in origins[curr]:
                if origin == 0: return True
                pos_stack.append(origin)

        return False


nums = [2,3,1,1,4]
# nums = [3,2,1,0,4]
# nums = [0]
# nums = [3]

result = SlowSolution().canJump(nums)

print(result)


# Solution was too slow: complexity O(n**2) and space complexity O(n)
# Greedy approach:
# i = len(nums) - 1 is a winning position
# if I can jump from position j to a winning position, then j is a winning position

# Strategy, iterate backwards through the array, keeping track of the *lowest* winning index.
# if this becomes 0, then 0 is a winning index

# Taken from Leetcode
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_pos = len(nums) - 1
        for i, num in reversed(list(enumerate(nums))):
            if i + num >= last_pos:
                last_pos = i

        return last_pos == 0
