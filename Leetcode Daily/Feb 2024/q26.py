# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def solve(p,q):
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False
            return solve(p.left, q.left) and solve(p.right, q.right)
        return solve(p,q)

# 100. Same Tree
# Time complexity: O(N)
# Space complexity: O(N)
    
# Recursively check if the nodes are the same. If they are, return True. If not, return False. Base cases are if both nodes are None, return True. If one of the nodes is None, return False. If the values of the nodes are not the same, return False. Otherwise, recursively check the left and right nodes.