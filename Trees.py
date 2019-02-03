# Arrays
# , array is a static data structure (residing in Data or Stack section)
## while linked list is a dynamic data structure (residing in Heap section).
# Graph
# Heap
# Linkedlist
# Queue
# Sorting
# Searching
# Stack
# Trees

class TreeNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insertleft(self, child):
        if self.left is None:
            self.left = child
        else:
            child.left = self.left
            self.left = child

    def insertright(self, child):
        if self.right is None:
            self.right = child
        else:
            child.right = self.right
            self.right = child

    def getleft(self):
        return self.left

    def getright(self):
        return self.right

    def setvalue(self, value):
        self.value = value

    def getvalue(self):
        return self.value


# Tree traversals
# Inorder (left, value, right)
# Preorder (value, left, right)
# Postorder (left, right, value)

def inorder(Tree):
    """
    # in this we traverse first to the leftmost node, then print its data and then traverse for rightmost node
    :param Tree:
    :return:
    """
    if Tree:
        inorder(Tree.getleft())
        print(Tree.getvalue(), end=' ')
        inorder(Tree.getright())
    return


def preorder(Tree):
    """
    # in this we first print the root node and then traverse towards leftmost node and then to the rightmost node
    :param Tree:
    :return:
    """
    if Tree:
        print(Tree.getvalue(), end=' ')
        preorder(Tree.getleft())
        preorder(Tree.getright())
    return


def postorder(Tree):
    """
    # in this we first traverse to the leftmost node and then to the rightmost node and then print the data
    :param Tree:
    :return:
    """
    if Tree:
        postorder(Tree.getleft())
        postorder(Tree.getright())
        print(Tree.getvalue(), end=' ')
    return


if __name__ == '__main__':
    root = TreeNode('a')
    print(root.value)
    print(root.right)

    root.insertleft(TreeNode('b'))
    root.insertleft(TreeNode('c'))
    print(root.left.left.value)

    root.insertright(TreeNode('d'))
    root.insertright(TreeNode('e'))
    print(root.right.right.value)

    print('Inorder  Traversal:')
    print(inorder(root))
    print('\nPreorder Traversal:')
    print(preorder(root))
    print('\nPostorder Traversal:')
    print(postorder(root))
