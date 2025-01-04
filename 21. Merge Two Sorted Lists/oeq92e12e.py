while p1 and p2:
    if p1.val < p2.val:
        current.next = p1
        p1 = p1.next
    else:
        current.next = p2
        p2 = p2.next
    current = current.next
