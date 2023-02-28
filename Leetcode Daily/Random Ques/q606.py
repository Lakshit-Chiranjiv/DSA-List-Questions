class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        ans = [str(root.val)]
        def preOrder(node):
            if not node:
                return
            ans.append("(")
            ans.append(str(node.val))
            if node.left == None and node.right != None:
                ans.append("()")
            preOrder(node.left)
            preOrder(node.right)
            ans.append(")")

        if root.left == None and root.right != None:
            ans.append("()")
        preOrder(root.left)
        preOrder(root.right)
        return ''.join(ans)