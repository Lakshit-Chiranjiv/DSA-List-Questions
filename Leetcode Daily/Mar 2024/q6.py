# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False

# 141. Linked List Cycle
# Time Complexity: O(n)
# Space Complexity: O(1)

# We maintain two pointers, fast and slow. The fast pointer moves two steps at a time and the slow pointer moves one step at a time. If there is a cycle, the fast pointer will eventually meet the slow pointer. If there is no cycle, the fast pointer will reach the end of the list.