# target sum by assigning + or - to each element of array
# count number of ways to assign + or - to each element of array such that sum of array is equal to target

# this problem can be broken down into partition array into two subsets such that difference of sum of both subsets is equal to a specific difference
# + elements can be considered as one subset and - elements can be considered as another subset
# now we have to find number of ways to partition array into two subsets such that difference of sum of both subsets is equal to target


# recursive solution
def countWaysToSumTarget(arr, target, n):
    if target == 0:
        return 1

    if n == 0:
        if arr[n] == target:
            return 1
        else:
            return 0

    notPick = countWaysToSumTarget(arr, target, n-1)
    pick = 0
    if arr[n] <= target:
        pick = countWaysToSumTarget(arr, target-arr[n], n-1)

    return notPick + pick

def countPartition(arr, diff, n):
    totalSum = 0
    for i in range(n):
        totalSum += arr[i]

    target = (totalSum - diff) // 2
    return countWaysToSumTarget(arr, target, n)

# memoization
def countWaysToSumTargetMemo(arr, target, n, dp):
    if target == 0:
        return 1

    if n == 0:
        if arr[n] == target:
            return 1
        else:
            return 0

    if dp[n][target] != -1:
        return dp[n][target]

    notPick = countWaysToSumTargetMemo(arr, target, n-1, dp)
    pick = 0
    if arr[n] <= target:
        pick = countWaysToSumTargetMemo(arr, target-arr[n], n-1, dp)

    dp[n][target] = notPick + pick
    return dp[n][target]

def countPartitionMemo(arr, diff, n):
    totalSum = 0
    for i in range(n):
        totalSum += arr[i]

    target = (totalSum - diff) // 2
    dp = [[-1 for i in range(target+1)] for j in range(n)]
    return countWaysToSumTargetMemo(arr, target, n, dp)

# tabulation
def countWaysToSumTargetTab(arr, target, n):
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
    return countWaysToSumTargetTab(arr, target, n)

# space optimization
def countWaysToSumTargetTabOpt(arr, target, n):
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
    return countWaysToSumTargetTabOpt(arr, target, n)