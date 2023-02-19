class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []

        ans = []
        q = [root]

        while q:
            lvl_sz = len(q)
            lvl = []

            for i in range(lvl_sz):
                node = q.pop(0)

                lvl.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            ans.append(lvl)

        return ans