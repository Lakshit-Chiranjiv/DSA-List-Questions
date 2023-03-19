class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def f(node):
            if not node:
                return
            f(node.left)
            f(node.right)
            ans.append(node.val)

        f(root)
        return ans