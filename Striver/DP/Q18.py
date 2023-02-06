# count partition with given difference

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

def countPartition(arr, diff, n):
    totalSum = 0
    for i in range(n):
        totalSum += arr[i]

    target = (totalSum - diff) // 2
    return countSubsetSum(arr, target, n)

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

def countPartitionMemo(arr, diff, n):
    totalSum = 0
    for i in range(n):
        totalSum += arr[i]

    target = (totalSum - diff) // 2
    dp = [[-1 for i in range(target+1)] for j in range(n)]
    return countSubsetSumMemo(arr, target, n, dp)

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

def countPartitionTab(arr, diff, n):
    totalSum = 0
    for i in range(n):
        totalSum += arr[i]

    target = (totalSum - diff) // 2
    return countSubsetSumTab(arr, target, n)

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

def countPartitionTabOpt(arr, diff, n):
    totalSum = 0
    for i in range(n):
        totalSum += arr[i]

    target = (totalSum - diff) // 2
    return countSubsetSumTabOpt(arr, target, n)


arr = [1, 1, 2, 3]
diff = 1
n = len(arr)
print(countPartition(arr, diff, n))
print(countPartitionMemo(arr, diff, n))
print(countPartitionTab(arr, diff, n))
print(countPartitionTabOpt(arr, diff, n))
