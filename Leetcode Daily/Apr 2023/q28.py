class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def dfs(i, strs, vis):
            vis[i] = True
            for j in range(len(strs)):
                if vis[j]: continue
                if is_similar(strs[i], strs[j]):
                    dfs(j, strs, vis)

        def is_similar(a,b):
            count = 0
            for i in range(len(a)):
                if a[i] != b[i]: count += 1
            return count == 2 or count == 0
        groups = 0
        n = len(strs)
        vis = [False] * n
        for i in range(n):
            if vis[i]: continue
            groups += 1
            dfs(i, strs, vis)
        return groups
    
# intuition:
# 1. We can think of it like a graph problem where each string is a node and there is an edge between two nodes if they are similar.
# 2. So, we just need to find the number of connected components in the graph.
# 3. There can be a DFS function which will mark all the nodes connected to a node as visited and while calling this we can increase the count of connected components which will be the answer.

# solution:
# 1. Define a dfs function which takes the index of the current node, the list of strings and the visited array as parameters.
# 2. It marks the current node as visited and then iterates over all the nodes and if the node is not visited and is similar to the current node, then we call the dfs function on that node.
# 3. Next, we define a function which checks if two strings are similar or not. It iterates over the strings and if the characters at the same index are not equal, then it increases the count. If the count is 2 or 0, then the strings are similar and we return True else we return False.
# 4. Next, we define a variable groups which will store the number of connected components and initialize it to 0.
# 5. Also define a variable n which will store the length of the list of strings.
# 6. Create a visited array of size n and initialize all the values to False.
# 7. Iterate over all the nodes and if the node is not visited, then we increase the count of connected components and call the dfs function on that node.
# 8. Finally, we return the value of groups.



