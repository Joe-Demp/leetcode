from typing import List
from collections import defaultdict

def prepend_value_to_all(bag_of_lists, value):
    return [[value] + alist for alist in bag_of_lists]

class Solution:
    def __init__(self):
        self.former_cndts = defaultdict(list)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.sum_helper(candidates, target, 0)

    def sum_helper(self, candidates, target, c_start_index):
        if target == 0: return [[]]
        elif target < 0 or c_start_index == len(candidates): return []

        reference_tuple = (target, c_start_index)
        if reference_tuple in self.former_cndts:
            return self.former_cndts[reference_tuple]

        start_element = candidates[c_start_index]
        child_lists = self.sum_helper(candidates, target - start_element, c_start_index)
        lists_with_start_element = prepend_value_to_all(child_lists, start_element)
        
        lists_without_start_element = self.sum_helper(candidates, target, c_start_index + 1)

        total_combination_sums = lists_with_start_element + lists_without_start_element
        self.former_cndts[reference_tuple] = total_combination_sums
        return total_combination_sums


# Note the pattern:

# Have I already computed this result?
#   Yes!    -> return the precomputed result
#   No      -> compute the result
#           -> store the result
#           -> return the result

# Note, it's like rerunning the "Have I already computed this result?" question

# Also note the easy error: returning lists that were to be edited:
#   Lists were returned and values were appended to them.
#   Since the lists had been returned, they had been stored in the dict (former_cndts)
#   The values were also appended to the list in the dict, since these are the same lists (with the same references)


# candidates = [2, 3, 6, 7]
# target = 7

candidates = [1, 2]
target = 4

result = Solution().combinationSum(candidates, target)

print(result)
