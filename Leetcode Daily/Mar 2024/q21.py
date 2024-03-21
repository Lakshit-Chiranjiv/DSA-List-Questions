# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        curr = head.next if head else None
        nxt = curr.next if curr else None
        if head:
            if not head.next:
                return head
            head.next = None
        else:
            return head
        while nxt:
            curr.next = prev
            prev = curr
            curr = nxt
            nxt = nxt.next
        curr.next = prev
        return curr
    
# 206. Reverse Linked List
# Time Complexity: O(n)
# Space Complexity: O(1)
    
# We maintain three pointers, prev, curr and nxt. Handled 2 edge cases, where head is None and head.next is None then we simply return the head. Then we iterate the linked list until the next pointer is None that means, we will stop when the current pointer is the last node. And simultaneously we reverse the pointers. At the end of the iteration, we need to reverse the next pointer of the last node to the previous node as the last node will be the new head. We then return the new head.