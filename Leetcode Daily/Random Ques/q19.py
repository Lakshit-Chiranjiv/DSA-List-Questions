def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    x = head
    y = head
    c = 1
    while x != None:
        x = x.next
        c += 1
    c -= 1
    if c == 1:
        return None

    if n == c:
        return head.next

    nf = c - n + 1
    c = 1
    x = head

    x = x.next
    while c != nf-1:
        y = y.next
        x = x.next
        c += 1

    y.next = x.next
    x.next = None

    return head