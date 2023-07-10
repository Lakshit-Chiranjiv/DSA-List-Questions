class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        if not root.left and not root.right:
            return 1
        l = float('inf')
        r = float('inf')
        if root.left:
            l = 1 + self.minDepth(root.left)
        if root.right:
            r = 1 + self.minDepth(root.right)

        return min(l,r)