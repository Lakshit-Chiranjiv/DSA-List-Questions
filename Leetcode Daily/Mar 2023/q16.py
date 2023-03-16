class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None

        rootVal = postorder.pop()
        root = TreeNode(rootVal)

        inOrder_idx = inorder.index(rootVal)

        root.right = self.buildTree(inorder[inOrder_idx+1:],postorder)
        root.left = self.buildTree(inorder[:inOrder_idx],postorder)

        return root