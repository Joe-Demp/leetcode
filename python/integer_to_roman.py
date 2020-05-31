# I     1
# V     5
# X     10
# L     50
# C     100
# D     500
# M     1000

# I placed before V (5) and X (10) to make 4 and 9. 
# X placed before L (50) and C (100) to make 40 and 90. 
# C placed before D (500) and M (1000) to make 400 and 900.

# range 1 to 3999

# iteration 1: range 1 to 5

# todo iteration 2...

subtractions = {
    4: "IV",
    9: "IX",
    40: "XL",
    90: "XC",
    400: "CD",
    900: "CM"
}

roman_digits = {
    # small digit, big digit
    # where big_digit == 5 * small_digit
    1: ("I", "V"),
    10: ("X", "L"),
    100: ("C", "D"),
    1000: ("M", "$")    # $, a dummy symbol here. Never used since num in range [1, 4000)
}

def over_thousand(num):
    x = num // 1000
    return x * "M"

def roman(int_pair):
    x, y = int_pair
    if is_subtraction(x):
        return subtractions[x * y]

    small_digit, big_digit = roman_digits[y]
    result = ""

    if x >= 5:
        result += big_digit
        x -= 5

    result += x * small_digit
    return result

def is_subtraction(num):
    'returns true for values of 4 or 9'
    return (num % 5) == 4

def reduce_to_pair(num):
    dec = 1
    while num >= 10:
        num //= 10
        dec *= 10

    return (num, dec)

class Solution:
    def intToRoman(self, num: int) -> str:
        result = ""
        
        if num >= 1000:
            result += over_thousand(num)
            num %= 1000

        while num > 0:
            reduced = reduce_to_pair(num)
            result += roman(reduced)
            num -= reduced[0] * reduced[1]

        return result

result = Solution().intToRoman(58)
print(result)   
