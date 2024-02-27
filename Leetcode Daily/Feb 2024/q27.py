# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]

        def heightCalc(root):
            if not root:
                return -1
            left = heightCalc(root.left)
            right = heightCalc(root.right)
            res[0] = max(res[0], 2+left+right)

            return 1 + max(left, right)
        heightCalc(root)
        return res[0]

# 543. Diameter of Binary Tree
# Time Complexity: O(n)
# Space Complexity: O(n) for the recursive stack
    
# The idea is to calculate the height of the left and right subtree and then calculate the diameter of the tree. The diameter of the tree is the maximum of the sum of the heights of the left and right subtree + 2. We keep track of the maximum diameter in the res array. We return the maximum diameter at the end.