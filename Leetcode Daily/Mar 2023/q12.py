class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        mp = {}
        for i in lists:
            temp = i
            while temp:
                if mp.get(temp.val,-1) == -1:
                    mp[temp.val] = 1
                else:
                    mp[temp.val] += 1
                temp = temp.next
        
        mps = OrderedDict(sorted(mp.items()))
        head = ListNode(0)
        temp = head
        for i in mps:
            z = mps[i]
            while z > 0:
                x = ListNode(i)
                temp.next = x
                temp = temp.next
                z -= 1
        
        temp.next = None

        return head.next