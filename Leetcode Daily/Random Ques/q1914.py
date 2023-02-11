def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
    m, n = len(grid), len(grid[0])
    ll = min(m, n) // 2
    
    for l in range(ll):
        v = []
        
        for i in range(l, n - l - 1): # top row
            v.append(grid[l][i])
        
        for i in range(l, m - l - 1): # right
            v.append(grid[i][n - l - 1])
    
        for i in range(n - l - 1, l, -1): # bottom row
            v.append(grid[m - l - 1][i])
        
        for i in range(m - l - 1, l, -1): # left
            v.append(grid[i][l])
        
        # assign it back to the grid from the 'start' position
        start = k % len(v)
        
        for i in range(l, n - l - 1): # top row
            grid[l][i] = v[start % len(v)]
            start += 1

        for i in range(l, m - l - 1): # right
            grid[i][n - l - 1] = v[start % len(v)]
            start += 1

        for i in range(n - l - 1, l, -1): # bottom row
            grid[m - l - 1][i] = v[start % len(v)]
            start += 1

        for i in range(m - l - 1, l, -1): # left
            grid[i][l] = v[start % len(v)]
            start += 1
    
    return grid