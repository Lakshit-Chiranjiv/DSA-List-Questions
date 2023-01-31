# Partition a set into two subsets such that the difference of subset sums is minimum

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

def min_diff(arr):
    total = sum(arr)
    target = total//2
    for i in range(target, -1, -1):
        if subset_sum(arr, i, len(arr)-1):
            return total - 2*i


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

def min_diff_memo(arr):
    total = sum(arr)
    target = total//2
    dp = [[-1 for i in range(target+1)] for j in range(len(arr)+1)]
    for i in range(target, -1, -1):
        if subset_sum_memo(arr, i, len(arr)-1, dp):
            return total - 2*i

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

def min_diff_tab(arr):
    total = sum(arr)
    target = total//2
    for i in range(target, -1, -1):
        if subset_sum_tab(arr, i, len(arr)-1):
            return total - 2*i

# space optimization
def min_diff_tab_opt(arr):
    total = sum(arr)
    target = total//2
    dp = [False for i in range(target+1)]
    dp[0] = True
    dp[arr[0]] = True
    for i in range(1, len(arr)):
        for j in range(target, -1, -1):
            if j >= arr[i]:
                dp[j] = dp[j] or dp[j-arr[i]]
    for i in range(target, -1, -1):
        if dp[i]:
            return total - 2*i

arr = [1, 6, 11, 5]
print(min_diff(arr))
print(min_diff_memo(arr))
print(min_diff_tab(arr))
print(min_diff_tab_opt(arr))
