class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        adj = defaultdict(list)

        for src,dst in edges:
            adj[src].append(dst)

        def dfs(node):
            if node in path:
                return float('inf')
            if node in visit:
                return 0

            visit.add(node)
            path.add(node)

            colorIdx = ord(colors[node]) - 97
            colormap[node][colorIdx] = 1

            for nei in adj[node]:
                if dfs(nei) == float('inf'): return float('inf')

                for col in range(26):
                    colormap[node][col] = max(colormap[node][col], (1 if col==colorIdx else 0)+colormap[nei][col])

            path.remove(node)
            return max(colormap[node])
            
        
        n = len(colors)
        ans = 0

        visit = set()
        path = set()

        colormap = [[0]*26 for i in range(n)]

        for i in range(n):
            ans = max(ans,dfs(i))

        return -1 if ans==float('inf') else ans
    
# intution:
# 1. For each node, we need to find the max number of nodes that can be reached from it and have the same color as the node.
# 2. DFS is a good choice for this problem. We can use a colormap to store the max number of nodes that can be reached from a node and have the same color as the node.
# 3. We can use a path set to detect if there is a cycle in the graph and a visit set to detect if a node has been visited.
# 4. Using the adj list, we can traverse the graph and update the colormap for each node using the colormap of its neighbors.

# solution:
# 1. Create an adj list. Iterate through the edges and add the edges to the adj list.
# 2. Create a dfs function that takes a node as input. If the node is in the path set, return infinity. If the node is in the visit set, return 0.
# 3. Add the node to the visit set and the path set.
# 4. Get the color index of the node. Update the colormap of the node at the color index to 1.
# 5. Iterate through the neighbors of the node. If the dfs function returns infinity, return infinity.
# 6. Iterate through the colormap of the neighbor. Update the colormap of the node at the color index to the max of the current value and the value of the neighbor at the color index plus 1 if the color index is the same as the color index of the node and 0 otherwise.
# 7. Remove the node from the path set.
# 8. Return the max of the colormap of the node.
# 9. Create a visit set and a path set.
# 10. Create a colormap of size n*26 and initialize it to 0.
# 11. Iterate through the nodes. Update the ans to the max of the ans and the dfs function of the node.
# 12. Return -1 if the ans is infinity and the ans otherwise.