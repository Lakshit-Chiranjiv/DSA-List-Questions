class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        all_nodes = set(range(n))
        destination_nodes = set(destination for _, destination in edges)
        source_nodes = all_nodes - destination_nodes
        
        return list(source_nodes)
    
# intution:
# 1. Find all nodes and all destination nodes.
# 2. Find all source nodes by subtracting destination nodes from all nodes.
# 3. Return source nodes.

# solution:
# 1. Create a set of all nodes by using range(n).
# 2. Create a set of all destination nodes by using list comprehension.
# 3. Create a set of all source nodes by subtracting destination nodes from all nodes using set difference.
# 4. Return source nodes by converting set to list.

# Time complexity: O(n) where n is the number of nodes in the graph as we are iterating over all nodes once.

# Space complexity: O(n) where n is the number of nodes in the graph as we are storing all nodes in a set.