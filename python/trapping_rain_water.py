# todo submit this

def make_gradiants(heights):
    gradiants = [heights[0]]
    for i in range(1, len(heights)):
        gradiants.append(heights[i] - heights[i - 1])
    
    return gradiants

# This doesn't work -> is max plateau has to be more general
# including plateaus bigger than 2 and including the edge cases
def make_local_maximums(gradiants):
    local_maximums = []
    ascending = True
    for i in range(1, len(gradiants)):
        if gradiants[i] < 0:
            if gradiants[i - 1] > 0:
               local_maximums.append(i - 1)
            elif gradiants[i - 1] == 0 and ascending:
                local_maximums.append(i - 1)
            ascending = False
        elif gradiants[i] > 0:
            ascending = True
    
    # if the last gradiant is positive, consider the final height to also be a local_maximum
    if gradiants[-1] > 0:
        local_maximums.append(len(gradiants) - 1)
    elif gradiants[-1] == 0 and ascending:
        local_maximums.append(len(gradiants) - 1)
    
    return local_maximums

class Solution:
    def trap(self, height) -> int:
        if len(height) < 2:
            return 0
        
        self.height = height
        gradiants = make_gradiants(height)
        local_maxes = make_local_maximums(gradiants)
        max_with_heights = [(index, height[index]) for index in local_maxes]

        max_with_heights.sort(key=lambda item: item[1])
        if len(max_with_heights) < 2:
            return 0
        
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
            volume += max(0, max_water_level - self.height[i])
        return volume
