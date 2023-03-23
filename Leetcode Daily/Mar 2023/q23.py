class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n-1:
            return -1

        graph = [set() for i in range(n)]

        for i,j in connections:
            graph[i].add(j)
            graph[j].add(i)

        visited = [0] * n

        def dfs(node):
            if visited[node]:
                return 0

            visited[node] = 1
            for neighbor in graph[node]:
                dfs(neighbor)
            return 1

        return sum(dfs(node) for node in range(n)) - 1
    
#intuition:
# 1. We need to find the number of connected components in the graph.
# 2. We can use DFS to find the number of connected components.
# 3. A graph can be represented as an adjacency list.
# 4. We can use a visited array to keep track of the visited nodes.
# 5. We can start with node 0 and call the dfs function.
# 6. We can iterate through all the adjacent nodes of the current node.
# 7. If the adjacent node is not visited, then we can call the dfs function on the adjacent node.
# 8. We can return 1 if the current node is not visited.
# 9. Finally, we can return the number of connected components in the graph.
# 10. We can also use BFS to find the number of connected components.

#solution:
# 1. If the number of edges is less than n-1, then we can return -1 as we need at least n-1 edges to connect n nodes.
# 2. Initialize a graph to store the edges and weights of the graph.
# 3. Iterate through the edges and add the edges and weights to the graph.
# 4. Initialize a visited array to keep track of the visited nodes and set all the elements to 0.
# 5. Define a dfs function to find the number of connected components.
# 6. If the current node is visited, then we can return 0.
# 7. Set the current node to visited.
# 8. Iterate through all the adjacent nodes of the current node.
# 9. If the adjacent node is not visited, then we can call the dfs function on the adjacent node.
# 10. Return 1 if the current node is not visited.
# 11. Finally, we can return the number of connected components in the graph - 1 as we need to connect n nodes.



