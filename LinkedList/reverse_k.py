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

    def print_list(self,temp):
        while temp is not None:
            print(temp.data,end=" ")
            temp = temp.next
        print("\n")

    def reverse(self,node, count,k):

        if node.next is None or count == k:
            head = node
            next_node = node.next
            node.next = None
            return next_node,head

        next_node,head = self.reverse(node.next,count+1,k)
        node.next.next = node
        node.next = None
        return next_node,head
    
    def reverse_k(self,node,k):
        if node is None:
            return node
        end = node
        next_node,head = self.reverse(node,1,k)
        
        if next_node is not None:
            end.next = self.reverse_k(next_node,k)
        return head


        


        

if __name__ == '__main__':

    ll = LinkedList()
    ll.push(8)
    ll.push(7)
    ll.push(6)
    ll.push(5)
    ll.push(4)
    ll.push(3)
    ll.push(2)
    ll.push(1)
    print('+++++before')
    ll.print_list(temp=ll.head)
    ll.head = ll.reverse_k(ll.head,5)
    temp = ll.head
    print('+++++after')
    ll.print_list(temp)
    
