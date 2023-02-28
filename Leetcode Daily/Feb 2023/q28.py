class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        ans = []

        subTreeMap = defaultdict(list)

        def preOrder(node):
            if not node:
                return "NULL"

            s = ','.join([str(node.val), preOrder(node.left), preOrder(node.right)])
            if len(subTreeMap[s]) == 1:
                ans.append(node)

            subTreeMap[s].append(node)
            return s

        preOrder(root)
        return ans