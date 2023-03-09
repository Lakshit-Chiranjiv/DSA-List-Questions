class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None
        
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return fast
    


# solution 
# 1. initialize the slow pointer and the fast pointer to the head of the linked list.
# 2. run a while loop, if the fast pointer and the fast pointer.next is not None, we can move the slow pointer one step, and the fast pointer two steps.
# 3. if the slow pointer and the fast pointer meet, we can break the loop. This means we detected the cycle.
# 4. if the fast pointer and the fast pointer.next is None, we can return None as there is no cycle.
# 5. after we detect the cycle, we can initialize the slow pointer to the head of the linked list.
# 6. run a while loop, if the slow pointer and the fast pointer are not equal, we can move the slow pointer one step, and the fast pointer one step as well.
# 7. when the slow pointer and the fast pointer are equal, we can return the slow pointer as the start of the cycle.

# complexity
# time complexity: O(n) as we only need to run one loop for increasing the slow pointer and the fast pointer.
# space complexity: O(1) as we only need to use two pointers.