class Node(object):

    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key


class BinaryTree(object):

    def __init__(self):
        self.root = None

    def specific_order_PBT(self, root):

        if root is None:
            return
        print(root.key)

        if root.left is not None:
            print(root.left.key)
            print(root.right.key)

        if root.left.left is None:
            return

        q = list()
        q.append(root.left)
        q.append(root.right)

        while(len(q) > 0):
            first = q.pop(0)
            second = q.pop(0)
            print(first.left.key)
            print(second.right.key)
            print(first.right.key)
            print(second.left.key)

            if first.left.left is not None:
                q.append(first.left)
                q.append(second.right)
                q.append(first.right)
                q.append(second.left)


if __name__ == '__main__':
    bt = BinaryTree()
    bt.root = Node(1)
    bt.root.left = Node(2)
    bt.root.right = Node(3)
    bt.root.left.left = Node(4)
    bt.root.left.right = Node(5)
    bt.root.right.left = Node(6)
    bt.root.right.right = Node(7)

    bt.specific_order_PBT(bt.root)
