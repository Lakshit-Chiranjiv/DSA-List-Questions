class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = []
        q.append(root)

        nullEncountered = False

        while q:
            node = q.pop(0)
            if not node:
                nullEncountered = True
            else:
                if nullEncountered: return False
                q.append(node.left)
                q.append(node.right)
        return True