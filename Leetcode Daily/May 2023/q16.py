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
    
# intuition:
# 1. Check all the base checks of number of nodes between 0 and 2.
# 2. Then move on taking 3 temporary nodes and keep swapping the links of two nodes in sequence.
# 3. Keep track of the first node of the list and return it at the end.

# solution:
# 1. If head is None or head.next is None, return head.
# 2. If head.next.next is None, swap the two nodes and return the new head.
# 3. Take three temporary nodes x, y and z. x and y are the two nodes to be swapped and z is the node before x.
# 4. Initialize x to head, y to head.next and z to head.
# 5. Initialize st to y. st will be the new head of the list.
# 6. Initialize f to 0. f will be used to check if the first swap has been done or not.
# 7. While y is not None, swap the links of x and y. Then move x, y and z to the next nodes.
# 8. If f is 1, then set the link of z to y. This is done to link the swapped nodes to the previous nodes.
# 9. Set f to 1.
# 10. Return st.

# Time Complexity: O(n) where n is the number of nodes in the list as we are traversing the list only once and swapping the nodes.

# Space Complexity: O(1) as we are not using any extra space.