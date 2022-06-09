# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def findmid(self, head):
        slow = head
        fast = head.next
        while (fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
        return slow
        return slow

    def merge(self, l1, l2):
        l = ListNode(-1)
        temp = l
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        while l1 is not None:
            temp.next = l1
            l1 = l1.next
            temp = temp.next
        while l2 is not None:
            temp.next = l2
            l2 = l2.next
            temp = temp.next
        return l.next

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        mid = self.findmid(head)
        h1 = head
        h2 = mid.next
        mid.next = None
        newh1 = self.sortList(h1)
        newh2 = self.sortList(h2)
        return self.merge(newh1, newh2)

