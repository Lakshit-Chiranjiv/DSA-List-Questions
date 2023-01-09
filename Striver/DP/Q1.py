# nth fibonacci number

# recursion - Time: O(2^n) Space: O(n)
def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n-1) + fib(n-2)

# memoization - Time: O(n) Space: O(n)
def fib(n,dp):
    if n == 0 or n == 1:
        return n
    if dp[n] != -1:
        return dp[n]
    dp[n] = fib(n-1,dp) + fib(n-2,dp)
    return dp[n]

# tabulation - Time: O(n) Space: O(n)
def fib(n):
    dp = [0,1]
    for i in range(2,n+1):
        dp.append(dp[i-1] + dp[i-2])
    return dp[n]

# space optimization - Time: O(n) Space: O(1)
def fib(n):
    a = 0
    b = 1
    for i in range(2,n+1):
        c = a + b
        a = b
        b = c
    return b


n = int(input())
dp = [-1]*(n+1)
print(fib(n,dp))

