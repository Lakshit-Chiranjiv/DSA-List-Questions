# Partition Array for Maximum Sum

# recursive solution
def maxSumRec(i,arr,k):
    if i>=len(arr):
        return 0
    
    maxSum = float('-inf')
    length = 0
    maxVal = float('-inf')

    for j in range(i,min(i+k,len(arr))):
        maxVal = max(maxVal,arr[j])
        length += 1
        maxSum = max(maxSum,maxVal*length + maxSumRec(j+1,arr,k))

    return maxSum

# memoization solution
def maxSumMemo(i,arr,k,dp):
    if i>=len(arr):
        return 0
    
    if dp[i]!=-1:
        return dp[i]

    maxSum = float('-inf')
    length = 0
    maxVal = float('-inf')

    for j in range(i,min(i+k,len(arr))):
        maxVal = max(maxVal,arr[j])
        length += 1
        maxSum = max(maxSum,maxVal*length + maxSumMemo(j+1,arr,k,dp))

    dp[i] = maxSum
    return maxSum


# tabulation solution
def maxSumTab(arr,k):
    n = len(arr)
    dp = [0 for i in range(n+1)]

    for i in range(n-1,-1,-1):
        maxSum = float('-inf')
        length = 0
        maxVal = float('-inf')

        for j in range(i,min(i+k,n)):
            maxVal = max(maxVal,arr[j])
            length += 1
            maxSum = max(maxSum,maxVal*length + dp[j+1])

        dp[i] = maxSum

    return dp[0]

arr = [1,15,7,9,2,5,10]
k = 3
print(maxSumRec(0,arr,k))
dp = [-1 for i in range(len(arr))]
print(maxSumMemo(0,arr,k,dp))
print(maxSumTab(arr,k))
