# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return head
        p = []
        tmp = head
        while tmp:
            p.append(tmp.val)
            tmp = tmp.next

        q = []
        r = []
        for i in p:
            if i >= x:
                r.append(i)
            else:
                q.append(i)
        t = q+r
        ans = ListNode(t[0])
        tmp = ans
        for i in t[1:]:
            z = ListNode(i)
            tmp.next = z
            tmp = tmp.next
        return ans