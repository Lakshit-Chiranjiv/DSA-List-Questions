# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head.next:
            return
        tmp = head
        x = []
        while tmp:
            x.append(tmp.val)
            tmp = tmp.next
        y = x[:len(x)//2]
        z = x[len(x)//2:]
        i, j = 0, len(z)-1
        tmp = head
        c = 1
        while tmp:
            if c % 2 != 0 and i < len(y):
                tmp.val = y[i]
                i += 1
            else:
                tmp.val = z[j]
                j -= 1
            tmp = tmp.next
            c += 1
# 143. Reorder List
# Time Complexity: O(n)
# Space Complexity: O(n)
            
# We create a list x to store the values of the linked list. We then split the list into two halves, y and z. We then iterate through the linked list and alternate between the values of y and z and simultaneously update the linked list values.