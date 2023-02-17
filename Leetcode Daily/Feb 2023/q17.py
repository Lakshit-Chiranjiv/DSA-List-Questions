class Solution:
    def findMax(self, root):
        if root == None:
            return -1

        l = self.findMax(root.left)
        r = self.findMax(root.right)
        return max(root.val,l,r)

    def traverse(self, root, arr):
        if root == None:
            return

        arr[root.val] = 1
        self.traverse(root.left,arr)
        self.traverse(root.right,arr)


    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        mx = self.findMax(root)

        arr = [0] * (mx+1)
        self.traverse(root,arr)

        prev = -1
        curr = -1
        print(mx)
        print(arr)
        mnd = float('inf')
        for i in range(mx+1):
            curr += 1
            if arr[i] == 1:
                if prev != -1:
                    mnd = min(mnd,curr - prev)
                prev = i

        return mnd