class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []

        ans = []
        q = [root]
        ltr = 1

        while q:
            lvl_sz = len(q)
            lvl = []

            for i in range(lvl_sz):
                node = q.pop(0)

                if ltr == 1:
                    lvl.append(node.val)
                else:
                    lvl = [node.val] + lvl

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            ans.append(lvl)
            if ltr == 1:
                ltr = 0
            else:
                ltr = 1

        return ans