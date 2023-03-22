class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(dict)

        for u,v,w in roads:
            graph[u][v] = graph[v][u] = w

        mn = float('inf')
        visited = set()
        q = [1]

        while q:
            node = q.pop(0)

            for adj,wt in graph[node].items():
                if adj not in visited:
                    q.append(adj)
                    visited.add(adj)
                mn = min(mn,wt)
        
        return mn
    

#intuition:
# 1. We simply need to find the minimum weight edge in the graph which can connect from node 1 to any other node which in turn can connect to Nth node. 
# 2. We can use BFS to find the minimum weight edge.
# 3. We can use a queue to store the nodes to be visited and a set to store the visited nodes.
# 4. We can start with node 1 and add it to the queue and visited set.
# 5. We can pop the first element from the queue and iterate through all the adjacent nodes of the popped node.
# 6. If the adjacent node is not visited, then we can add it to the queue and visited set.
# 7. We can also find the minimum weight edge by comparing the weight of the current edge with the minimum weight edge found so far.
# 8. Finally, we can return the minimum weight edge.
# 9. DFS can also be used to find the minimum weight edge.

#solution:
# 1. Initialize a graph to store the edges and weights of the graph.
# 2. Iterate through the edges and add the edges and weights to the graph.
# 3. Initialize a variable mn to infinity and a set visited to store the visited nodes.
# 4. Initialize a queue q to store the nodes to be vissited.
# 5. Add node 1 to the queue.
# 6. While the queue is not empty, we can pop the first element from the queue and iterate through all the adjacent nodes of the popped node.
# 7. If the adjacent node is not visited, then we can add it to the queue and visited set.
# 8. We can also find the minimum weight edge by comparing the weight of the current edge with the minimum weight edge found so far.
# 9. Finally, we can return the minimum weight edge.