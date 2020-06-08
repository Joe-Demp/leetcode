class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        count_of_ones = 0
        while n > 0 and count_of_ones < 2:
            count_of_ones += n % 2
            n = n // 2
        return count_of_ones == 1

# taken from Leetcode
class FasterSolution:
    def isPowerOfTwo(self, n: int) -> bool:
        return (n and not (n & (n - 1)))

# Bitwise operators
# x << y
#     Returns x with the bits shifted to the left by y places (and new bits on the right-hand-side are zeros)
# x >> y
#     Returns x with the bits shifted to the right by y places (new bits on the left-hand-side are zeros)
# x & y
#     Does a "bitwise and". 
# x | y
#     Does a "bitwise or" 
# ~ x
#     Returns the complement of x
# x ^ y
#     Does a "bitwise exclusive or".
