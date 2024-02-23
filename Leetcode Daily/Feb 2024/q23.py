class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')]*n
        prices[src] = 0

        for i in range(k+1):
            tmp = prices.copy()

            for s, d, p in flights:
                if prices[s] == float('inf'):
                    continue
                if tmp[d] > (prices[s] + p):
                    tmp[d] = prices[s] + p
            prices = tmp
        if prices[dst] == float('inf'):
            return -1
        return prices[dst]

# 787. Cheapest Flights Within K Stops
# Time complexity: O(N*K)
# Space complexity: O(N)
    
# Approach: We can use the Bellman-Ford algorithm to solve this problem. We can keep track of the minimum price to reach each node. We can iterate through the flights k+1 times and update the minimum price to reach each node. Finally, we can return the price to reach the destination node. If the price is infinity, we return -1.