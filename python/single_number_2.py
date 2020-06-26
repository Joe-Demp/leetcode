from typing import List
from collections import defaultdict

# Solution that uses O(n) space
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counts = defaultdict(lambda: 0)

        for num in nums:
            counts[num] += 1

        for k, v in counts.items():
            if v == 1:
                return k


# arr = [2, 2, 3, 2]
arr = [0, 1, 0, 1, 0, 1, 99]

result = Solution().singleNumber(arr)

print(result)
