class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        q = [root]
        mxl = 1
        mxsm = float('-inf')
        lvl = 1

        while q:
            lvl_sum = 0
            nxt_lvl = []

            for node in q:
                lvl_sum += node.val
                if node.left:
                    nxt_lvl.append(node.left)
                if node.right:
                    nxt_lvl.append(node.right)
            
            if lvl_sum > mxsm:
                mxsm = lvl_sum
                mxl = lvl
            q = nxt_lvl
            lvl += 1
        return mxl