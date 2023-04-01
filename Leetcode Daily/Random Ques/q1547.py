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