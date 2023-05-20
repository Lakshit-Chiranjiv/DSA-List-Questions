class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)

        for i, eq in enumerate(equations):
            a,b = eq
            adj[a].append([b, values[i]])
            adj[b].append([a, 1/values[i]])

        def bfs(src, target):
            if src not in adj or target not in adj:
                return -1

            q = deque()
            visit = set()
            q.append([src, 1])
            visit.add(src)

            while q:
                node, wt = q.popleft()
                if node == target:
                    return wt
                for nei, weight in adj[node]:
                    if nei not in visit:
                        q.append([nei, wt * weight])
                        visit.add(nei)
            return -1

        return [bfs(q[0], q[1]) for q in queries]

# intuition:
# 1. Graph nodes can act as variables and edges can act as values. Like a -> b with edge weight 2 means a/b = 2.
# 2. We can use a graph to represent the equations and values.
# 3. Simply apply bfs on the adjacency list to find the answer else return -1.

# solution:
# 1. Create an adjacency list which is default dicting to a list.
# 2. For each equation, add the edge to the adjacency list and the inverse edge. Inverse edge is the edge with the inverse value.(a/b = 2, b/a = 1/2)
# 3. Define a bfs function that takes in the source and target.
# 4. If the source or target is not in the adjacency list, then return -1. This is because we can't find the answer.
# 5. Create a queue and a visited set. Add the source to the queue and the visited set.
# 6. While the queue is not empty, pop the node and weight from the queue.
# 7. If the node is the target, then return the weight.
# 8. For each neighbor of the node, if the neighbor is not in the visited set, then add the neighbor and the weight * the weight of the edge to the queue and the visited set. This is because we want to multiply the weight of the edge to the weight of the node. (a/b = 2, b/c = 3, a/c = 6)
# 9. After the function, iterate through each query and call the bfs function on the query and append the result to the answer list.
# 10. Return the answer list.

# Time Complexity: O(n * (V + E)) where n is the number of queries, V is the number of vertices, and E is the number of edges. We visit each node once and each edge once in the worst case for each query.

# Space Complexity: O(V + E) where V is the number of vertices and E is the number of edges. We use a default dict of length V and the call stack can go as deep as V. We also use a queue of length V and a visited set of length V.