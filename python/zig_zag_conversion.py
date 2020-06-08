# COVERT 
# "PAYPALISHIRING"

# TO
# """
# P   A   H   N
# A P L S I I G
# Y   I   R
# """

# AND THEN TO
# "PAHNAPLSIIGYIR"

# 4 ROWS:
#
# """
# P     I     N
# A   L S   I G
# Y A   H R
# P     I
# """

class OscillatingRange:
    def __init__(self, max_number):
        'range will oscillate in range [0, max_number)'
        self.max = max_number
        self.current = 0
        self.going_up = True

    def __iter__(self):
        return self

    def __next__(self):
        value_now = self.current

        if self.current == self.max - 1:
            self.going_up = False
            self.current = max(self.current - 1, 0)
        elif self.current == 0:
            self.going_up = True
            self.current = min(self.current + 1, self.max - 1)
        elif self.going_up:
            self.current += 1
        elif not self.going_up:
            self.current -= 1

        return value_now

# range_1 = OscillatingRange(1)
# range_2 = OscillatingRange(2)
# range_3 = OscillatingRange(3)

# for i in range(10):
#     print(next(range_1), end=' ')

# print()

# for i in range(10):
#     print(next(range_2), end=' ')

# print()

# for i in range(10):
#     print(next(range_3), end=' ')

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        letter_matrix = [[] for _ in range(numRows)]
        o_range = OscillatingRange(numRows)

        for letter in s:
            target_list_index = next(o_range)
            letter_matrix[target_list_index].append(letter)

        flat_matrix = [letter for letter_list in letter_matrix for letter in letter_list]
        return ''.join(flat_matrix)

string_in = "AB"
# string_out = Solution().convert(string_in, 1)

# print(string_out)   # "PAHNAPLSIIGYIR"
