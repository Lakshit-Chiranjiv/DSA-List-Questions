# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fr = ListNode(0, head)
        st = fr
        
        while st:
            ps = 0
            ed = st.next

            while ed:
                ps += ed.val
                if ps == 0:
                    st.next = ed.next
                ed = ed.next
            st = st.next
        return fr.next

# 1171. Remove Zero Sum Consecutive Nodes from Linked List
# Time Complexity: O(n^2)
# Space Complexity: O(1)
    
# We create a dummy node and set it's next to the head of the linked list. We then iterate through the linked list and for each node, we iterate through the linked list again and calculate the sum of the nodes from the current node to the end of the linked list. If the sum is 0, we remove the nodes from the current node to the end of the linked list. We then move to the next node and repeat the process. We then return the next of the dummy node.
