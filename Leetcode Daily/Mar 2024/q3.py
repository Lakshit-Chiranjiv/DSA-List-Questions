# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        x = head
        y = head
        c = 1
        while x != None:
            x = x.next
            c += 1
        c -= 1
        if c == 1:
            return None

        if n == c:
            return head.next

        nf = c - n + 1
        c = 1
        x = head

        x = x.next
        while c != nf-1:
            y = y.next
            x = x.next
            c += 1

        y.next = x.next
        x.next = None

        return head

# 19. Remove Nth Node From End of List
# Time Complexity: O(n)
# Space Complexity: O(1)
    
# We can solve this problem using two pointers. We can use two pointers x and y and move x to the end of the list and y to the node before the node to be deleted. We can then delete the node by changing the next pointer of y to the next pointer of x. We can then return the head of the list. We can also handle the edge cases where the list has only one node or the node to be deleted is the first node.