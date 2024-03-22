# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        x = []
        tmp = head
        while tmp:
            x.append(tmp.val)
            tmp = tmp.next
        
        return x == x[::-1]