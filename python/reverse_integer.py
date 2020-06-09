class Solution:
    MAX_VALUE = (2**31)
    MIN_VALUE = -(2**31)

    def reverse_digits(self, num):
        return int(str(num)[::-1])

    def reverse(self, x: int) -> int:
        if x >= 0:
            value = self.reverse_digits(x)
        else:
            value = -self.reverse_digits(-x)

        return value if value in range(self.MIN_VALUE, self.MAX_VALUE) else 0