class Solution:
    def markParents(self,root, parentsMap, target):
        q = []
        q.append(root)
        while len(q) > 0:
            curr = q.pop(0)
            if curr.left:
                parentsMap[curr.left] = curr
                q.append(curr.left)
            if curr.right:
                parentsMap[curr.right] = curr
                q.append(curr.right)
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parentsMap = {}
        self.markParents(root, parentsMap, target)
        q = []
        q.append(target)
        visited = set()
        visited.add(target)
        level = 0
        while len(q) > 0:
            if level == k:
                break
            size = len(q)
            for i in range(size):
                curr = q.pop(0)
                if curr.left and curr.left not in visited:
                    q.append(curr.left)
                    visited.add(curr.left)
                if curr.right and curr.right not in visited:
                    q.append(curr.right)
                    visited.add(curr.right)
                if parentsMap.get(curr,-1) != -1 and parentsMap[curr] not in visited:
                    q.append(parentsMap[curr])
                    visited.add(parentsMap[curr])
            level += 1
        ans = []
        for i in q:
            ans.append(i.val)
        return ans
