# burst balloons

# recursive solution
def maxCoins(i,j,nums):
    if i > j: return 0
    mx = float('-inf')

    for k in range(i,j+1):
        cost = nums[i-1]*nums[k]*nums[j+1] + maxCoins(i,k-1,nums) + maxCoins(k+1,j,nums)
        mx = max(mx,cost)

    return mx

# memoization solution
def maxCoinsMemo(i,j,nums,memo):
    if i > j: return 0
    if memo[i][j] != -1: return memo[i][j]
    mx = float('-inf')

    for k in range(i,j+1):
        cost = nums[i-1]*nums[k]*nums[j+1] + maxCoinsMemo(i,k-1,nums,memo) + maxCoinsMemo(k+1,j,nums,memo)
        mx = max(mx,cost)

    memo[i][j] = mx
    return mx

# tabulation solution
def maxCoinsTab(nums):
    n = len(nums)
    dp = [[0]*(n+2) for _ in range(n+2)]
    nums = [1] + nums + [1]

    for i in range(n, 0, -1):
        for j in range(1, n+1):
            if i > j: continue

            for k in range(i, j+1):
                dp[i][j] = max(dp[i][j], nums[i-1]*nums[k]*nums[j+1] + dp[i][k-1] + dp[k+1][j])
    
    return dp[1][n]


nums = [3,1,5,8]
n = len(nums)
memo = [[-1]*(n+2) for _ in range(n+2)]
newNums = [1] + nums + [1]
print(maxCoins(1,n,newNums))
print(maxCoinsMemo(1,n,newNums,memo))
print(maxCoinsTab(nums))