# longest bitonic subsequence

def longestBitonicSubsequence(arr, n):
    dp1 = [1 for _ in range(n)]
    for ind in range(1, n):
        for prev_ind in range(ind):
            if arr[ind] > arr[prev_ind]:
                dp1[ind] = max(dp1[ind], 1 + dp1[prev_ind])

    dp2 = [1 for _ in range(n)]
    for ind in range(n-2, -1, -1):
        for prev_ind in range(ind+1, n):
            if arr[ind] > arr[prev_ind]:
                dp2[ind] = max(dp2[ind], 1 + dp2[prev_ind])

    mx = 1
    for i in range(n):
        mx = max(mx, dp1[i] + dp2[i] - 1)

    return mx

arr = [1, 11, 2, 10, 4, 5, 2, 1]
n = len(arr)
print(longestBitonicSubsequence(arr, n))
