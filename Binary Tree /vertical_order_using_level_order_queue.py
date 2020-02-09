class Node(object):

    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key


class BinaryTree(object):

    def __init__(self):
        self.root = None

    def vertical_order(self, root, m, hd_node):
        q = []
        q.append(root)
        while len(q) > 0:

            temp = q.pop(0)
            hd = hd_node[temp]
            try:
                m[hd].append(temp.key)
            except:
                m[hd] = [temp.key]
            if temp.left:
                q.append(temp.left)
                hd_node[temp.left] = hd-1
            if temp.right:
                q.append(temp.right)
                hd_node[temp.right] = hd+1


if __name__ == '__main__':
    bt = BinaryTree()
    bt.root = Node(1)
    bt.root.left = Node(2)
    bt.root.right = Node(3)
    bt.root.left.left = Node(4)
    bt.root.left.right = Node(5)

    hd_node = dict()
    m = dict()

    hd_node[bt.root] = 0

    bt.vertical_order(bt.root, m, hd_node)

    print(sorted(m))
    for i in sorted(m):
        print(m[i])
