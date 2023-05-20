class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [0] * n
        def dfs(graph, colors, node, color):
            if colors[node] != 0:
                return colors[node] == color

            colors[node] = color

            for neighbor in graph[node]:
                if not dfs(graph, colors, neighbor, -color):
                    return False

            return True

        for i in range(n):
            if colors[i] == 0:
                if not dfs(graph, colors, i, 1):
                    return False

        return True

# intuition:
# 1. A graph is bipartite if and only if it is 2-colorable.
# 2. We try to color each node with a color, if we can't, then it is not bipartite.
# 3. We use dfs to color each node.

# solution:
# 1. Create a list of colors of length n, where n is the number of nodes initialized to 0.
# 2. Define a dfs function that takes in the graph, colors, node, and color.
# 3. If the color of the node is not 0, then return whether the color of the node is the same as the color passed in.
# 4. Set the color of the node to the color passed in.
# 5. For each neighbor of the node, if the dfs function returns false, then return false.
# 6. Else, return true.
# 7. After the function, iterate through each node in the graph and if the color of the node is 0, then call the dfs function on the node and if it returns false, then return false.
# 8. Else, return true.

# Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges. We visit each node once and each edge once in the worst case.

# Space Complexity: O(V) where V is the number of vertices. We use a list of colors of length V and the call stack can go as deep as V.