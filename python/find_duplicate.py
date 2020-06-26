from typing import List


# You must not modify the array (assume the array is read only).
# You must use only constant, O(1) extra space.
# Your runtime complexity should be less than O(n2).
# There is only one duplicate number in the array, but it could be repeated more than once.

def make_all_positive(nums):
    for i, num in enumerate(nums):
        nums[i] = abs(num)

# This solution does not obey all of the constraints
class SlySolution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in nums:
            index = abs(i) - 1
            if nums[index] < 0:
                answer = index + 1
                break
            else:
                nums[index] = -nums[index]

        make_all_positive(nums)
        return answer


# Solution from Leetcode
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tortoise = nums[0]
        hare = nums[0]

        tortoise = nums[tortoise]
        hare = nums[nums[hare]]

        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]

        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
        
        return hare


# arr = [1,3,4,2,2]
# arr = [3,1,3,4,2]
# arr = [2,5,9,6,9,3,8,9,7,1]

# result = Solution().findDuplicate(arr)

# print(result)

#################################################
# A Solution from Wikipedia that uses  λ and μ
##############################################
# ###

arr = [8,9,6,3,1,9,9,2,5,7]
def access_arr(index):
    return arr[index]

def floyd(f, x0):
    # Main phase of algorithm: finding a repetition x_i = x_2i.
    # The hare moves twice as quickly as the tortoise and
    # the distance between them increases by 1 at each step.
    # Eventually they will both be inside the cycle and then,
    # at some point, the distance between them will be
    # divisible by the period λ.
    tortoise = f(x0) # f(x0) is the element/node next to x0.
    hare = f(f(x0))
    while tortoise != hare:
        tortoise = f(tortoise)
        hare = f(f(hare))
  
    # At this point the tortoise position, ν, which is also equal
    # to the distance between hare and tortoise, is divisible by
    # the period λ. So hare moving in circle one step at a time, 
    # and tortoise (reset to x0) moving towards the circle, will 
    # intersect at the beginning of the circle. Because the 
    # distance between them is constant at 2ν, a multiple of λ,
    # they will agree as soon as the tortoise reaches index μ.

    # Find the position μ of first repetition.    
    mu = 0
    tortoise = x0
    while tortoise != hare:
        tortoise = f(tortoise)
        hare = f(hare)   # Hare and tortoise move at same speed
        mu += 1
 
    # Find the length of the shortest cycle starting from x_μ
    # The hare moves one step at a time while tortoise is still.
    # lam is incremented until λ is found.
    lam = 1
    hare = f(tortoise)
    while tortoise != hare:
        hare = f(hare)
        lam += 1
 
    return lam, mu

result = floyd(access_arr, 0)

print(result)   # lambda, mu

