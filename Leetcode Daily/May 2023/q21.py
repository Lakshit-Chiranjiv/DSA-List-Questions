class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dirc = [[0,1],[1,0],[0,-1],[-1,0]]

        def invalid(r,c):
            return r < 0 or c < 0 or r >= n or c >= n

        visit = set()
        def dfs(r,c):
            if invalid(r,c) or not grid[r][c] or (r,c) in visit:
                return
            visit.add((r,c))
            for dr,dc in dirc:
                dfs(r+dr, c+dc)
            
        def bfs():
            res = 0
            q = deque(visit)
            while q:
                for i in range(len(q)):
                    r,c = q.popleft()
                    for dr, dc in dirc:
                        curr, curc = r+dr, c+dc
                        if invalid(curr,curc) or (curr,curc) in visit:
                            continue
                        if grid[curr][curc]:
                            return res
                        q.append([curr,curc])
                        visit.add((curr,curc))
                res += 1
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    dfs(i,j)
                    return bfs()

# intuition:
# 1. It is given that there will be only 2 islands.
# 2. So, if we find the first island, we can use bfs to go layer by layer and find the shortest distance to the second island.
# 3. We can use dfs to find the first island and then use bfs to find the shortest distance to the second island.

# solution:
# 1. Take the length of the grid and define the directions list.
# 2. Define a function invalid that takes in a row and column and returns if the row or column is out of bounds of the grid.
# 3. Define a visit set.
# 4. Define a dfs function that takes in a row and column as parameters.
# 5. If the row or column is invalid or the value at the row and column is 0 or the row and column is in the visit set, then return.
# 6. Else, add the row and column to the visit set and iterate through each direction in the directions list. Call the dfs function on the row + the row of the direction and the column + the column of the direction.
# 7. Then, define a bfs function.
# 8. Define a res variable and a queue that is initialized to the visit set.
# 9. While the queue is not empty, iterate through each element in the queue.
# 10. Pop the row and column from the queue and iterate through each direction in the directions list.
# 11. Define a curr and curc variable that is the row + the row of the direction and the column + the column of the direction.
# 12. If the curr or curc is invalid or the curr and curc is in the visit set, then continue.
# 13. If the value at the curr and curc is 1, then return the res variable.
# 14. Else, append the curr and curc to the queue and add the curr and curc to the visit set.
# 15. Increment the res variable by 1.
# 16. After the bfs function, iterate through each row and column in the grid and if the value at the row and column is 1, then call the dfs function on the row and column. This will find the first island. Then, return the bfs function. This will find the shortest distance to the second island.

# Time Complexity: O(n^2) where n is the length of the grid.

# Space Complexity: O(n^2) where n is the length of the grid.