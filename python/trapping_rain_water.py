def make_gradiants(heights):
    gradiants = [heights[0]]
    for i in range(1, len(heights)):
        gradiants.append(heights[i] - heights[i - 1])
    
    return gradiants

# need a more sophisticated method for finding local maximums: something that can account for plateaus
# e.g. the start of [5, 5, 1, 7, ...] -> g -> [5, 0, -4, 6, ...]
# How can I tell between 0s on a down slope as opposed to 0s on a max plateau? 
def make_local_maximums(gradiants):
    local_maximums = []
    for i in range(1, len(gradiants)):
        if gradiants[i - 1] >= 0 and gradiants[i] < 0:
            local_maximums.append(i - 1)

    if gradiants[-1] > 0:
        local_maximums.append(len(gradiants) - 1)
    
    return local_maximums

class Solution:
    def trap(self, height) -> int:
        self.height = height
        gradiants = make_gradiants(height)
        local_maxes = make_local_maximums(gradiants)
        max_with_heights = [(index, height[index]) for index in local_maxes]

        max_with_heights.sort(key=lambda item: item[1])
        underwater = [max_with_heights.pop()[0], max_with_heights.pop()[0]]
        underwater.sort()
        volume = self.vol(underwater[0], underwater[1])

        while len(max_with_heights) > 0:
            new_max_index = max_with_heights.pop()[0]
            
            if new_max_index < underwater[0]:
                volume += self.vol(new_max_index, underwater[0])
                underwater[0] = new_max_index
            elif underwater[1] < new_max_index:
                volume += self.vol(underwater[1], new_max_index)
                underwater[1] = new_max_index

        return volume

    def vol(self, a, b):
        'Returns the volume of water that settled between points i and j of the heights array'
        max_water_level = min(self.height[a], self.height[b])
        volume = 0
        for i in range(a + 1, b):
            volume += max_water_level - self.height[i]
        return volume
