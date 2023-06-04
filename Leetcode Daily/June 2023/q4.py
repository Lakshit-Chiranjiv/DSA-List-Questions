class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        prov = 0
        vis = [0] * n

        def dfs(node):
            vis[node] = 1
            for nei in range(n):
                if isConnected[node][nei] == 1 and vis[nei] == 0:
                    dfs(nei)
        
        for i in range(n):
            if vis[i] == 0:
                prov += 1
                dfs(i)

        return prov
    
# intution:
# 1. Simply select a node and traverse as far as possible until you reach a node which has no further connections. This becomes one province.
# 2. Keep track of visited nodes so that you don't visit them again.
# 3. Repeat the above steps for all nodes. DFS is the best way to do this.

# solution:
# 1. Create a visited array of size n initialized to 0.
# 2. Initialize a variable prov to 0. This will store the number of provinces.
# 3. Define a function dfs which takes a node as input and performs the following: Mark the node as visited. Traverse all the nodes connected to this node and call dfs on them if they are not visited.
# 4. Iterate over all the nodes using a for loop. If the node is not visited, increment prov by 1 and call dfs on that node.
# 5. Return prov.

# Time Complexity: O(n^2)
# Space Complexity: O(n)