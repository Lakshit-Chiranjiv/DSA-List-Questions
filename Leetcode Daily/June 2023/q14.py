class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.min_diff = float('inf')
        self.prev_val = None
        
        def inorder_traversal(node):
            if node is None:
                return
            
            inorder_traversal(node.left)
            
            if self.prev_val is not None:
                self.min_diff = min(self.min_diff, abs(node.val - self.prev_val))
                
            self.prev_val = node.val
            
            inorder_traversal(node.right)
        
        inorder_traversal(root)
        return self.min_diff
    
# intuition:
# 1. Basically going over a DFS based inorder traversal of the tree and keeping track of the previous value in the inorder traversal.
# 2. At each node, we will check the difference between the current node value and the previous node value and update the minimum difference accordingly.
# 3. Finally, we will return the minimum difference.

# solution:
# 1. Initialize a variable min_diff to store the minimum difference between any two nodes in the tree. Set it to infinity.
# 2. Initialize a variable prev_val to store the value of the previous node in the inorder traversal. Set it to None.
# 3. Define a function inorder_traversal which takes a node as an argument. This function will perform a DFS based inorder traversal of the tree.
# 4. If the node is None, then return.
# 5. Call inorder_traversal on the left child of the node.
# 6. If prev_val is not None, then update min_diff to be the minimum of min_diff and the absolute difference between the current node value and the previous node value.
# 7. Update prev_val to be the current node value.
# 8. Call inorder_traversal on the right child of the node.
# 9. Call inorder_traversal on the root node.
# 10. Return min_diff.

# Time Complexity: O(n)
# Space Complexity: O(n)