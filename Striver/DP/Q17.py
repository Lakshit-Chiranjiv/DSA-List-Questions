# Count number of subsets which sum to target

# recursive solution
def countSubsetSum(arr, target, n):
    if target == 0:
        return 1

    if n == 0:
        if arr[n] == target:
            return 1
        else:
            return 0

    notPick = countSubsetSum(arr, target, n-1)
    pick = 0
    if arr[n] <= target:
        pick = countSubsetSum(arr, target-arr[n], n-1)

    return notPick + pick

# memoization
def countSubsetSumMemo(arr, target, n, dp):
    if target == 0:
        return 1

    if n == 0:
        if arr[n] == target:
            return 1
        else:
            return 0

    if dp[n][target] != -1:
        return dp[n][target]

    notPick = countSubsetSumMemo(arr, target, n-1, dp)
    pick = 0
    if arr[n] <= target:
        pick = countSubsetSumMemo(arr, target-arr[n], n-1, dp)

    dp[n][target] = notPick + pick
    return dp[n][target]

# tabulation
def countSubsetSumTab(arr, target, n):
    dp = [[0 for i in range(target+1)] for j in range(n)]

    for i in range(n):
        dp[i][0] = 1
    
    if arr[0] <= target:
        dp[0][arr[0]] = 1

    for i in range(1, n):
        for j in range(0, target+1):
            notPick = dp[i-1][j]
            pick = 0
            if arr[i] <= j:
                pick = dp[i-1][j-arr[i]]
            dp[i][j] = notPick + pick

    return dp[n-1][target]

# space optimization
def countSubsetSumTabOpt(arr, target, n):
    dp = [0 for i in range(target+1)]
    curr = [0 for i in range(target+1)]

    dp[0] = 1
    curr[0] = 1

    if arr[0] <= target:
        dp[arr[0]] = 1

    for i in range(1, n):
        for j in range(0, target+1):
            notPick = dp[j]
            pick = 0
            if arr[i] <= j:
                pick = dp[j-arr[i]]
            curr[j] = notPick + pick
        dp = curr

    print(dp)

    return dp[target]

arr = [2, 3, 5, 6, 8, 10]
target = 10
n = len(arr)
dp = [[-1 for i in range(target+1)] for j in range(n)]
print(countSubsetSum(arr, target, n-1))
print(countSubsetSumMemo(arr, target, n-1, dp))
print(countSubsetSumTab(arr, target, n))
print(countSubsetSumTabOpt(arr, target, n))