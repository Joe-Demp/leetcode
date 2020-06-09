from typing import List

# a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
# b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
from functools import reduce
from collections import defaultdict

def xor_memoise(arr):
    memo = [0]
    for i, num in enumerate(arr):
        memo.append(memo[i] ^ num)
    return memo

def make_buckets_from_memos(memos):
    'Returns buckets of i, grouped by memo[i]'
    buckets = defaultdict(list)
    
    for i, num in enumerate(memos):
        buckets[num].append(i)
    return buckets

def get_pairs(arr):
    return [(i, j) for i in arr for j in arr if i < j]

class Solution:
    def xor_range(self, i, j):
        'returns xor of elements i up to j (inclusive) in the original array'
        return self.memo[i] ^ self.memo[j + 1]

    def countTriplets(self, arr: List[int]) -> int:
        self.memo = xor_memoise(arr)
        buckets = make_buckets_from_memos(self.memo)
        count = 0

        for indices in buckets.values():
            index_pairs = get_pairs(indices)
            for pair in index_pairs:
                i, k = pair[0], pair[1] - 1
                for j in range(i + 1, k + 1):
                    # note that this if is always true: can simplify
                    if self.xor_range(i, j - 1) == self.xor_range(j , k):
                        count += 1

        return count

# Taken from Leetcode
class FasterSolution:
    def countTriplets(self, arr: List[int]) -> int:
        if not arr: return 0
        curr = 0
        rec = {0:(1, 0)}
        ans = 0
        
        for i, num in enumerate(arr):
            curr ^= num
            n, rdc = rec.get(curr, (0, 0))
            ans += n * i - rdc
            rec[curr] = (n + 1, rdc + i + 1)
            
        return ans

class MyFasterSolution:
    def countTriplets(self, arr: List[int]) -> int:
        self.memo = xor_memoise(arr)
        buckets = make_buckets_from_memos(self.memo)
        count = 0

        for indices in buckets.values():
            index_pairs = get_pairs(indices)
            for pair in index_pairs:
                i, k = pair[0], pair[1] - 1
                count += k - i

        return count

arr = result = buckets = soln = None

arr = [2, 3, 1, 6, 7]
# arr = [7,11,12,9,5,2,7,17,22]
# arr = [3,3,1,14,4,6,8,5]
# arr = [1, 3, 5, 7, 9]
# arr = [2, 3]
# arr = [1 for _ in range(5)]
# result = xor_memoise(arr)
# buckets = make_buckets_from_memos(result)
soln = MyFasterSolution().countTriplets(arr)

print(arr)
print(result)
print(buckets)
print(soln)