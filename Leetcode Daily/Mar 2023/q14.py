class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def solve(node):
            if not node:
                return []

            arr = []
            left = solve(node.left)
            right = solve(node.right)

            if len(left) != 0:
                for i in left:
                    arr.append(str(node.val)+i)
            if len(right) != 0:
                for i in right:
                    arr.append(str(node.val)+i)
            if len(left)== 0 and len(right) == 0:
                arr.append(str(node.val))

            return arr

        x = solve(root)
        y = []
        for i in x:
            y.append(int(i))
        sm = sum(y)
        return sm