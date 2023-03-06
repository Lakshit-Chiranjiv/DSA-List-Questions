# longest increasing subsequence

# tabulation
def lengthOfLISTab(arr, n):
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for ind in range(n-1, -1, -1):
        for prev_ind in range(ind-1, -2, -1):
            length = 0 + dp[ind+1][prev_ind+1]
            if prev_ind == -1 or arr[ind] > arr[prev_ind]:
                length = max(length, 1 + dp[ind+1][ind+1])
            dp[ind][prev_ind+1] = length
    return dp[0][0]

# space optimization
def lengthOfLISSpOpt(arr, n):
    next = [0] * (n+1)
    curr = [0] * (n+1)
    for ind in range(n-1, -1, -1):
        for prev_ind in range(ind-1, -2, -1):
            length = 0 + next[prev_ind+1]
            if prev_ind == -1 or arr[ind] > arr[prev_ind]:
                length = max(length, 1 + next[ind+1])
            curr[prev_ind+1] = length
        next, curr = curr, next
    return next[0]


# optimized solution
def lengthOfLISOp(arr, n):
    dp = [1 for _ in range(n)]
    mx = 1
    for ind in range(1, n):
        for prev_ind in range(ind):
            if arr[ind] > arr[prev_ind]:
                dp[ind] = max(dp[ind], 1 + dp[prev_ind])
        mx = max(mx, dp[ind])

    return mx

# optimized solution and printing the sequence
def lengthOfLISOptimizedPrint(arr, n):
    dp = [1] * n
    hash = [i for i in range(n)]
    max_len = 1
    last_idx = 0
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                hash[i] = j
        if max_len < dp[i]:
            max_len = dp[i]
            last_idx = i

    lis = [0] * max_len
    idx = max_len - 1
    while last_idx != hash[last_idx]:
        lis[idx] = arr[last_idx]
        idx -= 1
        last_idx = hash[last_idx]
    lis[idx] = arr[last_idx]
    print(lis)
    return max_len


arr = [10, 22, 9, 33, 21, 50, 41, 60]
n = len(arr)
print(lengthOfLISTab(arr, n))
print(lengthOfLISSpOpt(arr, n))
print(lengthOfLISOp(arr, n))
print(lengthOfLISOptimizedPrint(arr, n))