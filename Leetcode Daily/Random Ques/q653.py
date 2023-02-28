class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        mp = {}
        def traverse(node):
            if not node:
                return

            if mp.get(node.val,0) == 0:
                mp[node.val] = 1
            else:
                mp[node.val] += 1
            traverse(node.left)
            traverse(node.right)

        traverse(root)
        if len(mp) < 2:
            return False
        for i in mp:
            mp[i] -= 1
            if mp.get(k-i,0) > 0:
                return True
            mp[i] += 1

        return False