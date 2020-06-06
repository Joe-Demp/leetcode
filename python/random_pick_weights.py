from random import Random

class Solution:

    def __init__(self, w: List[int]):
        self.rando = Random()
        self.w_sums = [0]

        # in the expanded array, i starts at position w_sums[i], if w[i] > 0
        for i in range(len(w)):
            self.w_sums.append(self.w_sums[i] + w[i])

        self.total_sum = self.w_sums[-1]

    def pickIndex(self) -> int:
        j = self.rando.randrange(self.total_sum)

        # left always points to a sum that is less than or equal to j
        # right always points to a sum that is greater than j
        left = 0
        right = len(self.w_sums)

        while left != right - 1:
            median = left + ((right - left) // 2)
            if self.w_sums[median] > j:
                right = median
            else:
                left = median

        return left
