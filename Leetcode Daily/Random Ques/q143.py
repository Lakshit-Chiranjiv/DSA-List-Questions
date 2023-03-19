class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        arr = []
        temp = head
        while temp:
            arr.append(temp)
            temp = temp.next

        s = 1
        e = len(arr)-1
        f = False
        n = len(arr)
        ans = head
        temp = ans
        for i in range(1,n):
            if not f:
                temp.next = arr[e]
                e -= 1
            else:
                temp.next = arr[s]
                s += 1
            f = not f
            temp = temp.next
        temp.next = None
        return ans