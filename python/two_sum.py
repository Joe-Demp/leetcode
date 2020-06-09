from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        reciprocal = {}

        for i, num in enumerate(nums):
            reciprocal[target - num] = i

        for i, num in enumerate(nums):
            if num in reciprocal and i != reciprocal[num]:
                return [i, reciprocal[num]]


nums = [2, 7, 11, 15]
target = 9

print(Solution().twoSum(nums, target))
