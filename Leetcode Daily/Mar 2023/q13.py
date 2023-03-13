class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def Mirror(a,b):
            if not a and not b: return True
            if not a or not b: return False

            if a.val == b.val and Mirror(a.left,b.right) and Mirror(a.right,b.left): return True

        return Mirror(root.left,root.right)