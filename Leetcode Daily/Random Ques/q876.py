def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    x = head
    y = head
    if x.next == None:
        return head
    
    if x.next.next == None:
        return head.next
    
    while y.next != None or y.next.next != None:
        x = x.next
        y = y.next.next        
        if y.next == None:
            return x
        if y.next.next == None:
            return x.next
    if y.next == None:
        return x
    else:
        return x.next