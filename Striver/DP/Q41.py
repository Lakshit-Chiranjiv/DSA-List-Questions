# longest increasing subsequence length

# recursive solution
def lis(arr, n, idx, prev_idx):
    if idx == n:
        return 0
    
    lis_len = lis(arr, n, idx+1, prev_idx)+0

    if prev_idx == -1 or arr[idx] > arr[prev_idx]:
        lis_len = max(lis_len, lis(arr, n, idx+1, idx)+1)

    return lis_len

# memoization solution
def lismem(arr, n, idx, prev_idx, dp):
    if idx == n:
        return 0
    
    if dp[idx][prev_idx+1] != -1:
        return dp[idx][prev_idx+1]
    
    lis_len = lismem(arr, n, idx+1, prev_idx, dp)+0

    if prev_idx == -1 or arr[idx] > arr[prev_idx]:
        lis_len = max(lis_len, lismem(arr, n, idx+1, idx, dp)+1)

    dp[idx][prev_idx+1] = lis_len
    return lis_len

arr = [10, 22, 9, 33, 21, 50, 41, 60]
n = len(arr)
dp = [[-1 for _ in range(n+1)] for _ in range(n)]
print(lis(arr, n, 0, -1))
print(lismem(arr, n, 0, -1, dp))
