class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        if head.next == None:
            return None

        if head.next.next == None:
            head.next = None
            return head

        slow = slow.next
        fast = fast.next.next
        prev = head
        while fast and fast.next:
            prev = prev.next
            slow = slow.next
            fast = fast.next.next

        prev.next = slow.next
        slow.next = None
        return head