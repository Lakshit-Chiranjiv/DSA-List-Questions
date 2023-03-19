class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        if head.next == None:
            return head
        if head.next.next == None:
            x = head
            y = head.next
            y.next = x
            x.next = None
            return y

        x = head
        y = head.next
        z = head
        st = y
        f = 0

        while y:
            x.next = y.next
            y.next = x
            if f:
                z.next = y
            z = x
            x = x.next
            if x:
                y = x.next
            else:
                y = None
            
            f = 1

        return st