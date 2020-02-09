class Node(object):

    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key


class BinaryTree(object):

    def __init__(self):
        self.root = None

    def next_right_node(self, root, key, level, value_level):
        if root is None:
            return None

        if root.key == key:
            value_level[0] = level
            return None

        if value_level[0] == level:
            return root

        left = self.next_right_node(root.left, key, level+1, value_level)
        if left:
            return left

        return self.next_right_node(root.right, key, level+1, value_level)


if __name__ == '__main__':
    bt = BinaryTree()
    bt.root = Node(1)
    bt.root.left = Node(2)
    bt.root.right = Node(3)
    bt.root.left.left = Node(4)
    bt.root.left.right = Node(5)

    value_level = [0]
    node = bt.next_right_node(bt.root, 3, 1, value_level)
    if node:
        print(node.key)
    else:
        print(node)
