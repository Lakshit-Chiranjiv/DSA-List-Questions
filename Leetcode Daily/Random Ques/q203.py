class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev = curr = head
        if not head:
            return None

        if head.next == None:
            if head.val == val:
                return None
            else:
                return head

        curr = curr.next

        while curr:
            if curr.val == val:
                prev.next = curr.next
                curr = curr.next
            else:
                prev = prev.next
                curr = curr.next

        if head.val == val:
            return head.next
        return head