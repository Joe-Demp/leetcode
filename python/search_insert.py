from bisect import bisect_left
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect_left(nums, target)

nums = [1,3,5,6]
# target = 5
# target = 2
# target = 7
target = 0

result = Solution().searchInsert(nums, target)
print(result)
