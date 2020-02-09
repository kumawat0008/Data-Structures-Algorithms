class Node:

    def __init__(self, data):

        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):

        self.head = None

    def push(self,data):

        node = Node(data)
        node.next = self.head
        self.head  = node

    def middleElem(self):

        slow = fast = self.head

        while((fast is not None) and (fast.next is not None)):

            fast = fast.next.next
            slow = slow.next

        return slow.data

if __name__ == '__main__':

    ll = LinkedList()
    ll.push(1)
    ll.push(2)
    ll.push(3)
    ll.push(4)
    ll.push(15)
    print(ll.middleElem())
