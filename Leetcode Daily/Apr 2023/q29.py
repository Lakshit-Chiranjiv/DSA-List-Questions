
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            if self.rank[px] < self.rank[py]:
                self.parent[px] = py
            elif self.rank[px] > self.rank[py]:
                self.parent[py] = px
            else:
                self.parent[py] = px
                self.rank[px] += 1
    
    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def distanceLimitedPathsExist(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[bool]:
        edges = sorted(edges, key=lambda x: x[2])
        ans = [False] * len(queries)
        uf = UnionFind(n)
        i = 0
        sorted_queries = sorted(enumerate(queries), key=lambda x: x[1][2])
        for q_idx, (u, v, limit) in sorted_queries:
            while i < len(edges) and edges[i][2] < limit:
                uf.union(edges[i][0], edges[i][1])
                i += 1
            ans[q_idx] = uf.connected(u, v)
        return ans

# solution:
# 1. First, we sort the queries based on the limit in ascending order.
# 2. Next, we sort the edges based on the weight in ascending order.
# 3. Traverse the queries and for each query, we traverse the edges and union the nodes if the weight of the edge is less than the limit of the query.
# 4. Finally, we check if the nodes are connected or not and store the result in the answer array.
# 5. Return the answer array.