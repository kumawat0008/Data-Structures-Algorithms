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

    def reverse(self,node):

        if node.next is None:
            self.head = node
            node.next = None
            return

        self.reverse(node.next)
        node.next.next = node
        node.next = None

        


        

if __name__ == '__main__':

    ll = LinkedList()
    ll.push(1)
    ll.push(2)
    ll.push(3)
    ll.push(4)
    ll.push(5)
    ll.push(6)
    ll.push(7)
    ll.push(8)
    print(ll.head.data)
    ll.reverse(ll.head)
    print(ll.head.data)
