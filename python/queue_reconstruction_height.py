from typing import List
from bisect import bisect_left

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        emptyIndices = [i for i in range(len(people))]
        new_queue = [None for _ in range(len(people))]
        people.sort(key=lambda p: p[1])
        people.sort(key=lambda p: p[0], reverse=True) # sort by descending height

        while people:
            person = people.pop()
            person_index = person[1]    # the index of the indices that are left in empty_indices
            place_to_put_person = emptyIndices[person_index]

            new_queue[place_to_put_person] = person
            del emptyIndices[person_index]
        
        return new_queue

peeps = [[9,0],[7,0],[1,9],[3,0],[2,7],[5,3],[6,0],[3,4],[6,2],[5,2]]

# print(peeps)
# new_peeps = Solution().reconstructQueue(peeps)
# print(new_peeps)
# Expected: [[3,0],[6,0],[7,0],[5,2],[3,4],[5,3],[6,2],[2,7],[9,0],[1,9]]

# Key points: 
# heights need to be sorted in descending order
# for people of equal height, they need to be sorted in ascending k


# this solution works, the following is faster
class FasterSolution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # Key: Place everybody one by one *in order*. To do that, you can place each person
        # in order first by height, then by num of people in front. 
        people.sort(key = lambda x: (-x[0], x[1]))
        # print(people)
        output = []
        for p in people:
            # You've ensured, at time of insertion, everything in front of p is really taller than p
            # (as everything taller or further in line than p has already been placed)
            output.insert(p[1], p)
        return output

print(peeps)
new_peeps = FasterSolution().reconstructQueue(peeps)
print(new_peeps)
