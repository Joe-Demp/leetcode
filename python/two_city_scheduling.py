class Solution:
    def twoCitySchedCost(self, costs) -> int:
        costs.sort(key=lambda x: abs(x[0] - x[1]))

        countA = 0
        countB = 0
        count_per_city = len(costs) // 2
        total_cost = 0

        while countA < count_per_city and countB < count_per_city:
            cost = costs.pop()
            
            if cost[0] <= cost[1]:
                total_cost += cost[0]
                countA += 1
            else:
                total_cost += cost[1]
                countB += 1

        while countA < count_per_city:
            cost = costs.pop()
            total_cost += cost[0]
            countA += 1

        while countB < count_per_city:
            cost = costs.pop()
            total_cost += cost[1]
            countB += 1

        return total_cost
