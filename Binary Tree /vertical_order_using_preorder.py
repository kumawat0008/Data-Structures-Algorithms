class Node(object):

    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key


class BinaryTree(object):

    def __init__(self):
        self.root = None

    def vertical_order(self, root, hd, m):

        if root is None:
            return
        try:
            m[hd].append(root.key)
        except:
            m[hd] = [root.key]
        self.vertical_order(root.left, hd-1, m)
        self.vertical_order(root.right, hd+1, m)


if __name__ == '__main__':
    bt = BinaryTree()
    bt.root = Node(1)
    bt.root.left = Node(2)
    bt.root.right = Node(3)
    bt.root.left.left = Node(4)
    bt.root.left.right = Node(5)

    m = dict()

    bt.vertical_order(bt.root, 0, m)

    print(sorted(m))
    for i in sorted(m):
        print(m[i])
