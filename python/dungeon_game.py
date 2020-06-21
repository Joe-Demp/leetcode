from typing import List

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        rows = len(dungeon)
        if rows > 0:
            cols = len(dungeon[0])
        else: return 1
        if cols == 0: return 1

        minimum_health = [[0 for _ in range(cols)] for _ in range(rows)]
        minimum_health[rows - 1][cols - 1] = max(1, 1 - dungeon[rows - 1][cols - 1])

        # fill the far right column
        for row in reversed(range(rows - 1)):
            effect_in_square = dungeon[row][-1]
            minimum_health[row][-1] = max(1, minimum_health[row + 1][-1] - effect_in_square)

        # fill in the bottom row
        for col in reversed(range(cols - 1)):
            effect_in_square = dungeon[-1][col]
            minimum_health[-1][col] = max(1, minimum_health[-1][col + 1] - effect_in_square)

        # fill in the bit in between
        for row in reversed(range(rows - 1)):
            for col in reversed(range(cols - 1)):
                min_health = min(minimum_health[row + 1][col], minimum_health[row][col + 1])
                effect_in_square = dungeon[row][col]
                minimum_health[row][col] = max(1, min_health - effect_in_square)

        return minimum_health[0][0]


dungeon = [
    [-2, -3, 3],
    [-5, -10, 1],
    [10, 30, -5]
]

result = Solution().calculateMinimumHP(dungeon)

print(result)
