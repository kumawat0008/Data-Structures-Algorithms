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

    def middleElem(self,node,count,COUNT):

        if node is None:
            COUNT[0] = count
            return -1
        val = self.middleElem(node.next,count+1,COUNT)
        if count == int(COUNT[0]/2):
            return node.data
        else:
            return val



        

if __name__ == '__main__':

    ll = LinkedList()
    ll.push(1)
    ll.push(2)
    ll.push(3)
    ll.push(4)
    ll.push(15)
    COUNT = [-1]
    print(ll.middleElem(ll.head,0,COUNT))
