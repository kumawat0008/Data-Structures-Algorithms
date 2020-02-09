class Node(object):

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree(object):

    def __init__(self):
        self.root = None

    def insert(self, root, key):

        if root is None:
            return Node(key)

        if key <= root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        return root

    def inorder(self, root):

        if root is None:
            return

        else:
            self.inorder(root.left)
            print(root.key)
            self.inorder(root.right)

    def min_value(self, root):
        current = root
        while current.left is not None:
            current = current.left

        return current

    def delete(self, root, key):

        if root is None:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)

        elif key > root.key:
            root.right = self.delete(root.right, key)

        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.min_value(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, key)

        return root


if __name__ == '__main__':

    bst = BinarySearchTree()
    bst.root = bst.insert(bst.root, 10)
    bst.root = bst.insert(bst.root, 5)
    bst.root = bst.insert(bst.root, 12)
    bst.root = bst.insert(bst.root, 14)
    bst.root = bst.insert(bst.root, 2)
    bst.root = bst.insert(bst.root, 7)
    bst.root = bst.insert(bst.root, 8)
    bst.inorder(bst.root)
    bst.delete(bst.root, 14)
    bst.inorder(bst.root)
