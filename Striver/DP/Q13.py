# Cherry Pickup | 3D DP
# Alice & Bob are playing a game. They are given a grid of size n x m. Each cell of the grid has a value. Alice and Bob take turns in a way, that in each turn, a player picks two cells and removes them from the grid. The score of each player is the sum of the values of the cells they picked. The player with the maximum score wins. If both players play optimally, what is the maximum possible score that Alice can achieve?
# alice starts from (0, 0) and bob starts from (0, m - 1)
# they can only down, left down, right down
# they can move to the same cell in the next row
# their target is to maximize the sum of the values of the cells they picked
# if they land on the same cell, they will only pick it once

import random


# recursive solution 
def cherryPickup(grid,i,j1,j2):
    if j1 < 0 or j1 >= len(grid[0]) or j2 < 0 or j2 >= len(grid[0]):
        return -float('inf')
    if i == len(grid):
        if j1 == j2:
            return grid[i-1][j1]
        else:
            return grid[i-1][j1] + grid[i-1][j2]
    ans = 0
    for x in range(-1,2):
        for y in range(-1,2):
            if j1 == j2:
                ans = max(ans, cherryPickup(grid,i+1,j1+x,j2+y)+grid[i][j1])
            else:
                ans = max(ans, cherryPickup(grid,i+1,j1+x,j2+y)+grid[i][j1]+grid[i][j2])
    return ans

# memoization solution
def cherryPickupMem(grid,i,j1,j2,dp):
    if j1 < 0 or j1 >= len(grid[0]) or j2 < 0 or j2 >= len(grid[0]):
        return -float('inf')
    if i == len(grid):
        if j1 == j2:
            return grid[i-1][j1]
        else:
            return grid[i-1][j1] + grid[i-1][j2]
    if dp[i][j1][j2] != -1:
        return dp[i][j1][j2]
    ans = 0
    for x in range(-1,2):
        for y in range(-1,2):
            if j1 == j2:
                ans = max(ans, cherryPickupMem(grid,i+1,j1+x,j2+y,dp)+grid[i][j1])
            else:
                ans = max(ans, cherryPickupMem(grid,i+1,j1+x,j2+y,dp)+grid[i][j1]+grid[i][j2])
    dp[i][j1][j2] = ans
    return ans 

# tabulation solution
def cherryPickupTab(grid):
    n = len(grid)
    m = len(grid[0])
    dp = [[[-float('inf') for _ in range(m)] for _ in range(m)] for _ in range(n)]
    for j1 in range(m):
        for j2 in range(m):
            dp[n-1][j1][j2] = grid[n-1][j1] + grid[n-1][j2]
    for i in range(n-2,-1,-1):
        for j1 in range(m):
            for j2 in range(m):
                for x in range(-1,2):
                    for y in range(-1,2):
                        val = 0
                        if j1 == j2:
                            val = grid[i][j1]
                        else:
                            val = grid[i][j1] + grid[i][j2]
                        
                        if j1+x >= 0 and j1+x < m and j2+y >= 0 and j2+y < m:
                            dp[i][j1][j2] = max(dp[i][j1][j2], dp[i+1][j1+x][j2+y]+val)
                        else:
                            dp[i][j1][j2] = max(dp[i][j1][j2], -float('inf'))
        
    
    return dp[0][0][m-1]       

# space optimization
def cherryPickupSpOpt(grid):
    n = len(grid)
    m = len(grid[0])
    dp = [[-float('inf') for _ in range(m)] for _ in range(m)]
    curr = [[-float('inf') for _ in range(m)] for _ in range(m)]
    for j1 in range(m):
        for j2 in range(m):
            dp[j1][j2] = grid[n-1][j1] + grid[n-1][j2]
    for i in range(n-2,-1,-1):
        for j1 in range(m):
            for j2 in range(m):
                for x in range(-1,2):
                    for y in range(-1,2):
                        val = 0
                        if j1 == j2:
                            val = grid[i][j1]
                        else:
                            val = grid[i][j1] + grid[i][j2]
                        
                        if j1+x >= 0 and j1+x < m and j2+y >= 0 and j2+y < m:
                            curr[j1][j2] = max(dp[j1][j2], dp[j1+x][j2+y]+val)
                        else:
                            curr[j1][j2] = max(dp[j1][j2], -float('inf'))
        dp = curr
    return dp[0][m-1]   

n = 4
m = 5
# fill grid with random single digit values
grid = [[random.randint(0,9) for _ in range(m)] for _ in range(n)]

print(cherryPickup(grid,0,0,m-1))
dp = [[[-1 for _ in range(m)] for _ in range(m)] for _ in range(n)]
print(cherryPickupMem(grid,0,0,m-1,dp))
print(cherryPickupTab(grid))
print(cherryPickupSpOpt(grid))