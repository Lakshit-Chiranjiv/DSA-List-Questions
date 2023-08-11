class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def solve(i,s):
            if s == amount:
                return 1
            if i >= len(coins) or s > amount:
                return 0
            stay = solve(i,s+coins[i])
            move = solve(i+1,s)
            return stay + move

        return solve(0,0)