from typing import List
# Given a sorted array nums, remove the duplicates in-place such that each element appear only once
# and return the new length.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        current = ""
        k = 0

        for value in nums:
            if value != current:
                current = value
                nums[k] = current
                k += 1

        return k


# mynums = [1, 1, 2]
mynums = [0,0,1,1,1,2,2,3,3,4]

result = Solution().removeDuplicates(mynums)

print(mynums)
print(result)
