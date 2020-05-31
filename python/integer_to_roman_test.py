import unittest
from integer_to_roman import Solution 

class IntegerToRomanTest(unittest.TestCase):
    def setUp(self):
        self.sln = Solution()
    
    def test_zero(self):
        self.assertEqual("", self.sln.intToRoman(0))

    def test_one_to_five(self):
        # self.assertEqual("I", self.sln.intToRoman(1))
        self.assertEqual("II", self.sln.intToRoman(2))
        self.assertEqual("III", self.sln.intToRoman(3))
        self.assertEqual("IV", self.sln.intToRoman(4))
        self.assertEqual("V", self.sln.intToRoman(5))

    def test_leetcode(self):
        self.assertEquals("IX", self.sln.intToRoman(9))
        self.assertEquals("LVIII", self.sln.intToRoman(58))
        self.assertEquals("MCMXCIV", self.sln.intToRoman(1994))
        self.assertEquals("MMMCMXCIX", self.sln.intToRoman(3999))

    def test_leetcode_fails(self):
        self.assertEquals("X", self.sln.intToRoman(10))

if __name__ == '__main__':
    unittest.main()