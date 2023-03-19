class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        temp = head
        while temp:
            lst.append(temp.val)
            temp = temp.next

        n = len(lst)
        if n == 1:
            return head
        mx = lst[n-1]
        mark = [1]*n
        i = n-2
        while i >= 0:
            if lst[i] < mx:
                mark[i] = 0
            else:
                mx = lst[i]
            i -= 1

        temp = head
        prev = None
        st = None
        for i in range(n):
            if mark[i] == 1:
                if st:
                    prev.next = temp
                    prev = temp
                else:
                    st = temp
                    prev = temp
            temp = temp.next

        prev.next = None
        return st


