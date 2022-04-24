class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        new_head = ListNode(0)
        carry = 0
        p = l1
        q = l2
        curr = new_head
        while p is not None or q is not None:
            x = p.val if p is not None else 0
            y = q.val if q is not None else 0
            sum = x + y + carry
            carry = sum // 10
            curr.next = ListNode(sum % 10)
            curr = curr.next
            p = p.next if p is not None else None
            q = q.next if q is not None else None

        if carry:
            curr.next = carry
        return new_head.next