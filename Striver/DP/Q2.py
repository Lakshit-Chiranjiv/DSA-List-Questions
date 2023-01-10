# climbing stair problem

# recursive solution - Time: O(n^2) Space: O(n)
def climbStairs(n):
    if n == 0 or n == 1:
        return 1
    return climbStairs(n-1) + climbStairs(n-2)

# memoization - Time: O(n) Space: O(n)
def climbStairs(n,dp):
    if n == 0 or n == 1:
        return 1
    if dp[n] != 0:
        return dp[n]
    dp[n] = climbStairs(n-1,dp) + climbStairs(n-2,dp)
    return dp[n]

# tabulation - Time: O(n) Space: O(n)
def climbStairs(n):
    dp = [0]*(n+1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

# space optimazation - Time: O(n) Space: O(1)
def climbStairs(n):
    a = 1
    b = 1
    for i in range(2,n+1):
        c = a + b
        a = b
        b = c
    return b

n = 3
print(climbStairs(n))
