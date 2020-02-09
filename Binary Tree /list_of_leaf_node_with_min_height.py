class Node(object):

    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key


class BinaryTree(object):

    def __init__(self):
        self.root = None

    def get_list(self, root, level, min_level, nodes_at_min_level):
        if root is None:
            return
        if root.left is None and root.right is None:
            if level < min_level[0]:
                nodes_at_min_level.clear()
                nodes_at_min_level.append(root)
                min_level[0] = level
            elif level == min_level[0]:
                nodes_at_min_level.append(root)

        self.get_list(root.left, level+1, min_level, nodes_at_min_level)
        self.get_list(root.right, level+1, min_level, nodes_at_min_level)


if __name__ == '__main__':
    bt = BinaryTree()
    bt.root = Node(1)
    bt.root.left = Node(2)
    bt.root.right = Node(3)
    bt.root.left.left = Node(4)
    bt.root.left.right = Node(5)
    bt.root.right.left = Node(6)
    bt.root.right.right = Node(7)
    bt.root.left.left.left = Node(8)
    bt.root.left.left.right = Node(9)

    min_level = [1000000]
    nodes_at_min_level = []
    bt.get_list(bt.root, 1, min_level, nodes_at_min_level)
    for root in nodes_at_min_level:
        print(root.key)
