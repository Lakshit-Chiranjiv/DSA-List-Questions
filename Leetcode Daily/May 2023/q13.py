class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 10**9+7
        @cache
        def solve(i):
            if i > high:
                return 0
            res = ((1 if i >= low else 0) + (solve(i+zero)%mod) + (solve(i+one)%mod))%mod

            return (res)%mod

        return solve(0)
    
# intuition:
# 1. We don't need to form the string, we just need to keep track of the length of the string.
# 2. We just need to check if the length of the string is between low and high.
# 3. There are two cases for each index, either we take zero zeros or we take one ones.
# 4. DP is a suitable choice for this problem as we can store the results of the subproblems and hence we don't need to repeat the calculations.
# 5. Finally we return the sum of the results of all the subproblems with modulo 10^9+7.

# solution:
# 1. Take the modulo 10^9+7 in a variable mod.
# 2. Define a function solve(i) which returns the number of good strings that can be formed if we start from index i.
# 3. If i > high then return 0.
# 4. Take a variable res to store the result. Add 1 if i >= low else add 0. Then add solve(i+zero)%mod and solve(i+one)%mod.
# 5. Return res%mod.

# Time Complexity: O(n) where n is the length of the string. We are using memoization to store the results of the subproblems and hence we are not repeating the calculations. We only visit each index once.

# Space Complexity: O(n) where n is the length of the string. We are using memoization to store the results of the subproblems.