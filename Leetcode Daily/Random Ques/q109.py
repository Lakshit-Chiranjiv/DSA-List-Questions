class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def constructBST(arr,start,end):
            if start > end:
                return None
            mid = (start+end)//2
            node = TreeNode(arr[mid])
            node.left = constructBST(arr,start,mid-1)
            node.right = constructBST(arr,mid+1,end)
            return node

        arr = []
        while head:
            arr.append(head.val)
            head = head.next

        return constructBST(arr,0,len(arr)-1)