from typing import List
from collections import defaultdict, deque
import math

# The number of nodes n will be in range [1, 100], with nodes labeled from 0 to n - 1.
# The size of flights will be in range [0, n * (n - 1) / 2].

# The format of each flight will be (src, dst, price).

# The price of each flight will be in the range [1, 10000].
# k is in the range of [0, n - 1].
# There will not be any duplicated flights or self cycles.

def preprocess_graph(flights):
    graph = defaultdict(list)
    for flight in flights:
        src = flight[0]
        graph[src].append(flight[1:])
    
    return graph

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = preprocess_graph(flights)
        cheapest_costs = defaultdict(lambda: math.inf, {src: 0})
        
        # queue contains [node_number, hops]
        bfs_queue = deque([[src, 0]])
        max_hops = K + 1

        while bfs_queue:
            p_node_number, p_hops = bfs_queue.popleft()
            for c_node_number, p_to_c_cost in graph[p_node_number]:
                c_cost = cheapest_costs[p_node_number] + p_to_c_cost
                c_hops = p_hops + 1
                if c_cost < cheapest_costs[c_node_number]:
                    cheapest_costs[c_node_number] = c_cost
                    if c_hops < max_hops:
                        bfs_queue.append([c_node_number, c_hops])

        return cheapest_costs[dst] if cheapest_costs[dst] < math.inf else -1


# my_flights = [[0,1,100],[1,2,100],[0,2,500]]
my_flights = [[0,1,1],[0,2,5],[1,2,1],[2,3,1]]

result = Solution().findCheapestPrice(4, my_flights, 0, 3, 1)

print(result)
