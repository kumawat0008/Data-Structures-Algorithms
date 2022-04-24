# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        first = head
        count = 0
        second = head
        while count != n:
            second = second.next
            count+=1
        if second is None:
            return head.next
        while second.next is not None:
            second = second.next
            first = first.next
        temp = first.next
        first.next = first.next.next
        del(temp)
        return head