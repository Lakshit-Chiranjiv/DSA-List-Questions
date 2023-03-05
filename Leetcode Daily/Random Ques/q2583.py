class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        def getHeight(root):
            if (root.left == None and root.right == None):
                return 0

            left = 0
            if (root.left != None):
                left = getHeight(root.left)

            right = 0
            if (root.right != None):
                right = getHeight(root.right)

            return (max(left, right) + 1)
        
        lvls = getHeight(root) + 1
        if k > lvls:
            return -1
        sums = [0] * lvls
        def levelSum(root,lvl):
            if not root:
                return
            sums[lvl] += root.val
            levelSum(root.left,lvl+1)
            levelSum(root.right,lvl+1)
            
        levelSum(root,0)
        sums.sort()
        return sums[len(sums)-k]