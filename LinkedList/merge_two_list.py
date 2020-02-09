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

    def merge(self,h1,h2):

        if h1 is None:
            return h2
        elif h2 is None:
            return h1

        ref = Node(-1)

        if h1.data <= h2.data:
            ref = h1
            ref.next = self.merge(h1.next, h2)
        else:
            ref = h2
            ref.next = self.merge(h1, h2.next)

        return ref

        


        

if __name__ == '__main__':

    ll_1 = LinkedList()
    ll_2 = LinkedList()
    ll_1.push(11)
    ll_1.push(8)
    ll_1.push(6)
    ll_1.push(4)
    ll_1.push(2)

    ll_2.push(10)
    ll_2.push(7)
    ll_2.push(5)
    ll_2.push(4)
    ll_2.push(3)
    
    merge_obj = LinkedList()
    obj = merge_obj.merge(ll_1.head,ll_2.head)
    while obj is not None:
        print('+++++++',obj.data)
        obj = obj.next
