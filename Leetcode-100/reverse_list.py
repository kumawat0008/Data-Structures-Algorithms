# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        def reverse_util(head):
            if head.next is None:
                self.final = head
                return

            reverse_util(head.next)
            head.next.next = head
            head.next = None

        if head is None:
            return head

        reverse_util(head)
        return self.final