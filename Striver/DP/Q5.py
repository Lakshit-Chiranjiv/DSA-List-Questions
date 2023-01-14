# Maximum Sum of Non-Adjacent Elements | House Robber problem

# recursive solution
def maxSum(arr, n):
    if n == 0:
        return arr[0]
    if n < 0:
        return 0
    pick = arr[n] + maxSum(arr, n-2)
    not_pick = maxSum(arr, n-1)
    return max(pick, not_pick)

# memoization
def maxSumMemo(arr, n, dp):
    if n == 0:
        return arr[0]
    if n < 0:
        return 0
    if dp[n] != -1:
        return dp[n]
    pick = arr[n] + maxSumMemo(arr, n-2, dp)
    not_pick = maxSumMemo(arr, n-1, dp)
    dp[n] = max(pick, not_pick)
    return dp[n]

# tabulation
def maxSumTab(arr, n):
    dp = [0 for i in range(n+1)]
    dp[0] = arr[0]
    for i in range(1, n+1):
        pick = arr[i] + dp[i-2]
        not_pick = dp[i-1]
        dp[i] = max(pick, not_pick)
    return dp[n]

# space optimization
def maxSumSpaceOpt(arr, n):
    a = arr[0]
    b = 0
    for i in range(1, n+1):
        pick = arr[i]
        if i > 1:
            pick += a
        not_pick = b
        c = max(pick, not_pick)
        a = b
        b = c
    return b

arr = [5, 5, 10, 100, 10, 5]
n = len(arr)-1
print(maxSum(arr, n))
print(maxSumSpaceOpt(arr, n))