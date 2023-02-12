# rod cutting problem

# recursive solution
def rodCutting(price, idx, N):
    if idx == 0:
        return N * price[0]
    
    notTake = rodCutting(price, idx - 1, N)
    take = float('-inf')
    rodLength = idx + 1
    if rodLength <= N:
        take = price[idx] + rodCutting(price, idx, N - rodLength)

    return max(notTake, take)

# memoization
def rodCuttingMem(price, idx, N, dp):
    if idx == 0:
        return N * price[0]
    
    if dp[idx][N] != -1:
        return dp[idx][N]
    
    notTake = rodCuttingMem(price, idx - 1, N, dp)
    take = float('-inf')
    rodLength = idx + 1
    if rodLength <= N:
        take = price[idx] + rodCuttingMem(price, idx, N - rodLength, dp)

    dp[idx][N] = max(notTake, take)
    return dp[idx][N]

# tabulation
def rodCuttingTab(price, N):
    dp = [[0] * (N + 1) for _ in range(len(price))]
    for i in range(0,N+1):
        dp[0][i] = i * price[0]
    
    for i in range(1, len(price)):
        for j in range(0, N+1):
            notTake = dp[i-1][j]
            take = float('-inf')
            rodLength = i + 1
            if rodLength <= j:
                take = price[i] + dp[i][j - rodLength]
            dp[i][j] = max(notTake, take)
    
    return dp[len(price) - 1][N]

# space optimization
def rodCuttingTabOpt(price, N):
    dp = [0] * (N + 1)
    for i in range(0,N+1):
        dp[i] = i * price[0]
    
    for i in range(1, len(price)):
        for j in range(N, 0, -1):
            notTake = dp[j]
            take = float('-inf')
            rodLength = i + 1
            if rodLength <= j:
                take = price[i] + dp[j - rodLength]
            dp[j] = max(notTake, take)
    
    return dp[N]

prices = [1, 5, 8, 9, 10, 17, 17, 20]
N = 8
dp = [[-1] * (N + 1) for _ in range(len(prices))]
print(rodCutting(prices, len(prices) - 1, N))
print(rodCuttingMem(prices, len(prices) - 1, N, dp))
print(rodCuttingTab(prices, N))
print(rodCuttingTabOpt(prices, N))
