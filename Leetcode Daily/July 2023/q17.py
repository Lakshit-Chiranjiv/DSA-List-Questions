# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1 = []
        s2 = []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        s1 = map(lambda x : str(x), s1)
        s1 = int(''.join(s1))
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        s2 = map(lambda x : str(x), s2)
        s2 = int(''.join(s2))
        s = str(s1+s2)
        s = list(s)
        s = list(map(lambda x : int(x), s))
        t = ListNode(s[0])
        x = t
        for i in s[1:]:
            x.next = ListNode(i)
            x = x.next
        return t