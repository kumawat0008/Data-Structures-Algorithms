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

    def find_middle_node(self, node):
        slow = fast = node
        if node is not None:
            while fast.next is not None and fast.next.next is not None:
                print('+++',slow.data,fast.data)
                slow = slow.next
                fast = fast.next.next

        return slow

    def recursive_merge(self,h1,h2):
        if h1 is None:
            return h2
        if h2 is None:
            return h1
        if h1.data<=h2.data:
            result = h1
            result.next = self.recursive_merge(h1.next, h2)
        else:
            result = h2
            result.next = self.recursive_merge(h1,h2.next)

        return result

    def merge_sort(self, node):
        if node is None or node.next is None:
            return node
        middle_node = self.find_middle_node(node)
        # return middle_node
        next_of_middle = middle_node.next
        middle_node.next = None
        left = self.merge_sort(node)
        right = self.merge_sort(next_of_middle)

        return self.recursive_merge(left,right)
         

 

if __name__ == '__main__':

    ll = LinkedList()
    ll.push(8)
    ll.push(5)
    ll.push(3)
    ll.push(6)
    ll.push(9)
    ll.push(7)
    ll.push(11)
    ll.push(12)
    ll.push(10)
    sorted_list =ll.merge_sort(ll.head)
    print(sorted_list.data)
    while sorted_list is not None:
        print('++++++++++',sorted_list.data)
        sorted_list = sorted_list.next

    
