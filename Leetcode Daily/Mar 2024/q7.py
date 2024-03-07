# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        x = head
        y = head
        if x.next == None:
            return head
        
        if x.next.next == None:
            return head.next
        
        while y.next != None or y.next.next != None:
            x = x.next
            y = y.next.next        
            if y.next == None:
                return x
            if y.next.next == None:
                return x.next
        if y.next == None:
            return x
        else:
            return x.next
        
# 876. Middle of the Linked List
# Time Complexity: O(n)
# Space Complexity: O(1)
        
# We maintain two pointers, x and y. The x pointer moves one step at a time and the y pointer moves two steps at a time. The x pointer will be at the middle of the list when the y pointer reaches the end of the list. If the length of the list is even, the x pointer will be at the first middle node. If the length of the list is odd, the x pointer will be at the second middle node.