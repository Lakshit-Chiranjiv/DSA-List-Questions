class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        def dfs(al, visited, from_node):
            change = 0
            visited[from_node] = True
            for to_node in al[from_node]:
                if not visited[abs(to_node)]:
                    change += dfs(al, visited, abs(to_node)) + (1 if to_node > 0 else 0)
            return change

        al = [[] for _ in range(n)]
        for c in connections:
            al[c[0]].append(c[1])
            al[c[1]].append(-c[0])

        print(al)
        visited = [False] * n
        return dfs(al, visited, 0)
    
# intution:
# 1. We need to find the minimum number of edges that need to be reversed to make the graph connected.
# 2. We can use DFS to traverse each path till the leaf node.
# 3. We can use a visited array to keep track of the visited nodes.
# 4. Startin with node 0, traverse each path till the leaf node and count the number of edges that need to be reversed.
# 5. We can use an adjacency list to store the edges and directions of the edges.
# 6. We can use a negative value to represent the reversed edge and a positive value to represent the original edge.
# 7. Whenever we get a negative value which has not been visited, we can increment the count by 1.

# solution:
# 1. Initialize an adjacency list to store the edges and directions of the edges.
# 2. Iterate through the edges and add the edges and directions to the adjacency list and the reversed edges and directions to the adjacency list.
# 3. Initialize a visited array to keep track of the visited nodes and set all the elements to False.
# 4. Define a dfs function to traverse each path till the leaf node.
# 5. In dfs function, initialize a change variable to keep track of the number of edges that need to be reversed.
# 6. Set the visited value of the current node to True.
# 7. Iterate through all the adjacent nodes of the current node.
# 8. If the adjacent node is not visited, then we can call the dfs function on the adjacent node and add the number of edges that need to be reversed to the change variable.
# 9. If the adjacent node is a negative value, then we can increment the change variable by 1.
# 10. In the end of dfs function return the change variable.
# 11. Finally, we can return the number of edges that need to be reversed by calling the dfs function on node 0.


