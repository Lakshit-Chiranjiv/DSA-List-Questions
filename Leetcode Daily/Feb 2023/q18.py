class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None
        if root.left == None and root.right == None:
            return root

        self.invertTree(root.left)
        self.invertTree(root.right)

        temp = root.left
        root.left = root.right
        root.right = temp


        return root