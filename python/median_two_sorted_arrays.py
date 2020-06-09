from typing import List


# Do in O(log(m + n)) time
# i.e. cannot combine the lists O(m + n) and then sort O((m + n) * log(m + n))

"""
Could try taking medians and keeping track of 
#(numbers g.t. the median) and #(numbers l.t. the median)

e.g. take the middle number from nums1, find it (or the next highest element) in nums2
use the indices to calculate the count of 'gte_median' and 'lte_median'
risk: doing a search is O(log(m)) followed by O(log(n)) = O(log(m * n))
"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        pass
