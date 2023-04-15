class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)
        @cache
        def solve(i,coins):
            if i >= n:
                return 0

            res = solve(i+1,coins)
            curPile = 0
            for j in range(min(coins,len(piles[i]))):
                curPile += piles[i][j]
                res = max(res, curPile + solve(i+1, coins-j-1))
            return res

        return solve(0, k)
    
# intuition:
# 1. Backtracking is the first thing that comes to mind.
# 2. At each step, we can either take the top of the current pile or move to the next pile and take the top of that pile.
# 3. We can use memoization to store the results of the subproblems.
# 4. The changing parameters here are the index of the current pile and the number of coins we have left.

# solution:
# 1. Get the length of the piles array and store it in a variable n.
# 2. Create a recursive function solve(i,coins) which returns the maximum number of coins we can get if we start from the ith pile and have coins coins left.
# 3. If i >= n, return 0 as we have reached the end of the piles array.
# 4. Create a variable res and initialize it to the result of the recursive call solve(i+1,coins) which means we are not taking the top of the current pile and moving to the next pile.
# 5. Create a variable curPile and initialize it to 0.
# 6. Create a for loop which iterates from 0 to min(coins,len(piles[i])) and in each iteration, we add piles[i][j] to curPile and update res to the maximum of res and curPile + solve(i+1, coins-j-1). Here, we are taking the top j+1 coins from the current pile and moving to the next pile. We are subtracting j+1 from coins as we have taken j+1 coins from the current pile.
# 7. Return res.
# 8. Return the result of the recursive call solve(0,k).