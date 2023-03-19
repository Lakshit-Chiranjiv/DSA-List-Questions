class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def f(node):
            if not node:
                return
            ans.append(node.val)
            f(node.left)
            f(node.right)

        f(root)
        return ans