def maxDistance(self, grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    l = [(i, j) for i in range(rows) for j in range(cols) if grid[i][j] == 1]
    if not l: return -1
    
    w = [(i, j) for i in range(rows) for j in range(cols) if grid[i][j] == 0]
    if not w: return -1
    
    q = collections.deque(l)
    dist = 0
    while q:
        dist += 1
        for _ in range(len(q)):
            x, y = q.popleft()
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                    grid[nx][ny] = dist
                    q.append((nx, ny))
    return dist-1