class Solution:
    def maxArea(self, height):
        self.height = height
        i, j = 0, len(height) - 1

        max_area = 0
        while i < j:
            max_area = max(max_area, self.area(i, j))

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area

    def area(self, a, b):
        return (b - a) * min(self.height[a], self.height[b])

my_heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
result = Solution().maxArea(my_heights)
print(result)
