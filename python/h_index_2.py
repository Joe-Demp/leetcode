from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations: return 0

        citlen = len(citations)
        left = 0
        right = citlen - 1
        if citations[right] is 0: return 0

        while right - left > 1:
            median = left + ((right - left) // 2)
            medianH = self.h(citlen, median)
            minCitations = citations[median]

            if medianH <= minCitations:
                right = median
            else:
                left = median

        leftH = self.h(citlen, left)
        if citations[left] >= leftH:
            return leftH
        
        return self.h(citlen, right)

    def h(self, N, index):
        return N - index


# citations = [11, 15]
citations = [0, 1, 2, 2, 2]
# citations = [0, 1, 2, 4, 6, 8, 8, 10]


result = Solution().hIndex(citations)

print(result)
