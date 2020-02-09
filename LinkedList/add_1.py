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

    def add_1(self,node):

        if node is None:
            return 1

        carry = self.add_1(node.next)
        sum = node.data+carry
        node.data = sum%10
        return int(sum/10)

 

if __name__ == '__main__':

    ll = LinkedList()
    ll.push(9)
    ll.push(9)
    ll.push(9)
    ll.push(1)

    carry = ll.add_1(ll.head)
    if carry:
        new_node = Node(carry)
        new_node.next = ll.head
        ll.head = new_node

    temp = ll.head

    while temp is not None:
        print('+++++',temp.data)
        temp = temp.next
