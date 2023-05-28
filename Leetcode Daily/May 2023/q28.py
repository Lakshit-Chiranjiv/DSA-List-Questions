class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        c = len(cuts)
        cuts = [0] + cuts + [n]

        @cache
        def solve(i,j):
            if i > j:
                return 0
            mn = float('inf')
            for k in range(i, j+1):
                mn = min(mn, solve(i, k-1) + solve(k+1, j) + cuts[j+1] - cuts[i-1])
            return mn

        return solve(1,c)
    
# intuition:
# 1. Its a partition DP problem. We can cut the rod at any point and then solve the subproblems.
# 2. For each subproblem, we try to cut the rod at all given cut points and calculate the cost.
# 3. We take the minimum of all the costs and return it.

# solution:
# 1. We sort the cuts array and add 0 and n to it. This is because we need to consider the cost of cutting the rod at the ends. Sorting is done to make sure that the cuts are in increasing order.
# 2. We define a recursive function solve(i,j) which returns the minimum cost of cutting the rod from i to j.
# 3. If i > j, we return 0.
# 4. We iterate from i to j and try to cut the rod at each point. We calculate the cost by adding the cost of cutting the rod from i to k-1, k+1 to j and the cost of cutting the rod at k. Then we take the minimum of previous minimum and the current cost.
# 5. We return the minimum cost.
# 6. Finally, we call the solve function with i = 1 and j = len(cuts). 

