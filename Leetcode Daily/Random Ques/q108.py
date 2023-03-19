class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def constructBST(arr,start,end):
            if start > end:
                return None
            mid = (start+end)//2
            node = TreeNode(arr[mid])
            node.left = constructBST(arr,start,mid-1)
            node.right = constructBST(arr,mid+1,end)
            return node
        return constructBST(nums,0,len(nums)-1)