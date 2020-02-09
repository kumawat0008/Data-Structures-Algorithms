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

    def is_palindrome(self,left,right,flag):

        if right is None:
            return

        print('+++++++going',left[0].data,right.data)

        self.is_palindrome(left,right.next,flag)

        print('++++++++hey',left[0].data, right.data)

        if left[0].data != right.data:
            print('+++++++inside')
            flag[0] = 0
        left[0] = left[0].next


        

if __name__ == '__main__':

    ll = LinkedList()
    ll.push(1)
    ll.push(2)
    ll.push(3)
    ll.push(4)
    ll.push(3)
    ll.push(2)
    ll.push(1)
    flag = [1]
    left = [ll.head]
    ll.is_palindrome(left,ll.head,flag)
    print('+++++++',flag[0])
