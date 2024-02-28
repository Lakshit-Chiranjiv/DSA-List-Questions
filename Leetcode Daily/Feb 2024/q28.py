# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = deque([root])

        while q:
            node = q.popleft()
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)
        return node.val
    
# 513. Find Bottom Left Tree Value
# Time Complexity: O(n)
# Space Complexity: O(n)
    
# We perform a level wise traversal from right to left so that when we reach the last level and last node through our traversal, it will be surely the left most one.