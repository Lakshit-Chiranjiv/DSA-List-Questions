class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        l = 1 + self.maxDepth(root.left)
        r = 1 + self.maxDepth(root.right)

        return max(l,r)