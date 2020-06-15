from typing import List

class NotWorkingSolution:
    def swap(self, i, j):
        self.nums[i], self.nums[j] = self.nums[j], self.nums[i]

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.nums = nums
        nums_len = len(nums)
        i, j, k = 0, nums_len, 0
        
        # i always points to the next place to put a 0
        # j always points to the last place a 2 was put
        while k < nums_len:
            if nums[k] == 0:
                self.swap(i, k)
                i += 1
            elif nums[k] == 2:
                j -= 1
                self.swap(k, j)
            k += 1


# my_list = [2,0,2,1,1,0]
my_list = [1,2,0]

print(my_list)

NotWorkingSolution().sortColors(my_list)

print(my_list)


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroes = ones = twos = 0
        
        for num in nums:
            if num == 0:
                zeroes += 1
            elif num == 1:
                ones += 1
            else:
                twos += 1
        
        for i in range(zeroes):
            nums[i] = 0
        for i in range(zeroes, zeroes + ones):
            nums[i] = 1
        for i in range(zeroes + ones, zeroes + ones + twos):
            nums[i] = 2
