class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = { i : [] for i in range(n)}

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                dist = abs(y2-y1) + abs(x2-x1)
                adj[i].append([dist,j])
                adj[j].append([dist,i])

        ans = 0
        visit = set()
        mh = [[0,0]]
        while len(visit) < n:
            cost, i = heapq.heappop(mh)
            if i in visit:
                continue
            ans += cost
            visit.add(i)
            for neiCost, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(mh, [neiCost, nei])
        return ans