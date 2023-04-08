class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        def dfs(node,copy,vis):
            vis[copy.val] = copy

            for n in node.neighbors:
                if vis[n.val] == None:
                    newNode = Node(n.val)
                    copy.neighbors.append(newNode)
                    dfs(n, newNode, vis)
                else:
                    copy.neighbors.append(vis[n.val])

        if not node:
            return None
        
        copy = Node(node.val)
        vis = [None]*101
        dfs(node,copy,vis)

        return copy
        
# intuition:
# 1. We use a dfs to traverse the graph and create a copy of it.
# 2. Use a visited array to keep track of the nodes that have been visited.
# 3. If the node has not been visited, then we create a new node and add it to the neighbors of the current node.
# 4. We then call dfs on the new node and the original node.
# 5. If the node has been visited, then we add the visited node to the neighbors of the current node.

# solution:
# 1. If the node is None, then we return None.
# 2. We create a copy of the node and a visited array of size 101.
# 3. We call dfs on the original node and the copy of the node.
# 4. In dfs, we mark the copy of the node as visited.
# 5. For each neighbor of the original node, if the neighbor has not been visited, then we create a new node and add it to the neighbors of the copy of the node.
# 6. We then call dfs on the new node and the original node.
# 7. If the neighbor has been visited, then we add the visited node to the neighbors of the copy of the node.
# 8. Return the copy of the node at the end.


# time complexity: O(n) where n is the number of nodes in the graph. We visit each node once.
# space complexity: O(n) where n is the number of nodes in the graph. We use a visited array of size n and a recursive stack of size n.