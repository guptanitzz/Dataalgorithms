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
import operator
from pythonds.basic.stack import Stack

OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}
LEFT_Bracket = '('
RIGHT_Bracket = ')'

class TreeNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insertleft(self, child):
        if self.left is None:
            self.left = TreeNode(child)
        else:
            t = TreeNode(child)
            t.left = self.left
            self.left = t

    def insertright(self, child):
        if self.right is None:
            self.right = TreeNode(child)
        else:
            t=TreeNode(child)
            t.right = self.right
            self.right = t

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

def parsetree(expression):
    inittr = TreeNode(None)
    # print(tr)
    pStack = Stack()
    pStack.push(inittr)
    tr = inittr

    for val in expression.split():
        print(val)
        if val == LEFT_Bracket:
            tr.insertleft('')
            pStack.push(tr)
            tr = tr.getleft()
        elif val in OPERATORS:
            tr.setvalue(val)
            tr.insertright('')
            pStack.push(tr)
            tr = tr.getright()
        elif val == RIGHT_Bracket:
            tr = pStack.pop()
        else:
            tr.setvalue(int(val))
            parent = pStack.pop()
            tr = parent
        # print(preorder(tr))
        # print(pStack)
    return inittr

def evaluate(parseTree):

    leftC = parseTree.getleft()
    rightC = parseTree.getright()

    if leftC and rightC:
        fn = OPERATORS[parseTree.getvalue()]
        return fn(evaluate(leftC),evaluate(rightC))
    else:
        return parseTree.getvalue()



if __name__ == '__main__':
    root = TreeNode('a')
    print(root.value)
    print(root.right)

    root.insertleft('b')
    root.insertleft('c')
    print(root.left.left.value)

    root.insertright('d')
    root.insertright('e')
    print(root.right.right.value)

    print('Inorder  Traversal:')
    print(inorder(root))
    print('\nPreorder Traversal:')
    print(preorder(root))
    print('\nPostorder Traversal:')
    print(postorder(root))

    pt = parsetree("( ( 10 + 5 ) * 3 ) ")
    print(postorder(pt))  # defined and explained in the next section
    print(evaluate(pt))
