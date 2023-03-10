import random


class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        n = 0
        temp = self.head
        while temp:
            n += 1
            temp = temp.next

        self.count = n

    def getRandom(self) -> int:
        x = random.randint(1,self.count)
        if x == 1:
            return self.head.val

        y = 1
        temp = self.head
        while y != x:
            temp = temp.next
            y += 1
        
        return temp.val