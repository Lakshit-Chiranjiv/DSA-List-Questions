class Solution:
    def shortestPathLength(self, graph):
        n = len(graph)
        ans = 0
        goal = (1 << n) - 1
        q = deque()  # (u, state)
        seen = [[False for _ in range(1 << n)] for _ in range(n)]

        for i in range(n):
            q.append((i, 1 << i))

        while q:
            for _ in range(len(q)):
                u, state = q.popleft()
                if state == goal:
                    return ans
                if seen[u][state]:
                    continue
                seen[u][state] = True
                for v in graph[u]:
                    q.append((v, state | (1 << v)))
            ans += 1

        return -1