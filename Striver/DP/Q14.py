# subset sum equal to target

# recursive solution
def subset_sum(arr, target, n):
    if target == 0:
        return True
    if n == 0:
        return arr[0] == target
    not_pick = subset_sum(arr, target, n-1)
    pick = False
    if target >= arr[n]:
        pick = subset_sum(arr, target-arr[n], n-1)
    return pick or not_pick

# memoization
def subset_sum_memo(arr, target, n, dp):
    if target == 0:
        return True
    if n == 0:
        return arr[0] == target
    if dp[n][target] != -1:
        return dp[n][target]
    not_pick = subset_sum_memo(arr, target, n-1, dp)
    pick = False
    if target >= arr[n]:
        pick = subset_sum_memo(arr, target-arr[n], n-1, dp)
    dp[n][target] = pick or not_pick
    return dp[n][target]

# tabulation
def subset_sum_tab(arr, target, n):
    dp = [[False for i in range(target+1)] for j in range(n+1)]
    for i in range(n+1):
        dp[i][0] = True
    dp[0][arr[0]] = True
    for i in range(1, n+1):
        for j in range(1, target+1):
            not_pick = dp[i-1][j]
            pick = False
            if j >= arr[i]:
                pick = dp[i-1][j-arr[i]]
            dp[i][j] = pick or not_pick
    return dp[n][target]

# space optimization
def subset_sum_tab_opt(arr, target, n):
    dp = [False for i in range(target+1)]
    curr = [False for i in range(target+1)]
    dp[0] = True
    curr[0] = True
    dp[arr[0]] = True
    for i in range(1, n+1):
        for j in range(target, arr[i]-1, -1):
            not_pick = dp[j]
            pick = False
            if j >= arr[i]:
                pick = dp[j-arr[i]]
            curr[j] = pick or not_pick
        dp = curr
    return dp[target]

arr = [2, 3, 7, 8, 10]
target = 11
n = len(arr)-1
dp = [[-1 for i in range(target+1)] for j in range(n+1)]
print(subset_sum(arr, target, n))
print(subset_sum_memo(arr, target, n, dp))
print(subset_sum_tab(arr, target, n))
print(subset_sum_tab_opt(arr, target, n))