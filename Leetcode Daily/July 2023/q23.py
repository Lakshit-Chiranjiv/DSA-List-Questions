# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        dp = {}
        def solve(n):
            if n == 0:
                return []
            if n == 1:
                return [TreeNode()]
            if n in dp:
                return dp[n]
            ans = []
            for l in range(n):
                r = n - 1 - l
                lt = solve(l)
                rt = solve(r)
                for t1 in lt:
                    for t2 in rt:
                        ans.append(TreeNode(0,t1,t2))
            dp[n] = ans
            return ans
        return solve(n)