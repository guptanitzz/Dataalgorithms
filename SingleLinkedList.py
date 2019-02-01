# Arrays
# Graph
# Heap
# Linkedlist
# Queue
# Sorting
# Stack
# Trees
class Node:

    # Each node object has its value and points to the next node in the linked list
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    # to get the value from list
    def getvalue(self):
        return self.val

    # to set the value in list
    def setvalue(self, val):
        self.val = val

    # to get the pointer from list
    def getpointer(self):
        return self.next

    # to set the pointer in list
    def setpointer(self, next):
        self.next = next


class LinkedList:
    """
    # D Linked list is a linear collection of data elements, whose order is not given by their physical placement in memory.
    Instead, each element points to the next.
    It is a data structure consisting of a collection of nodes which together represent a sequence.
    In its most basic form, each node contains: data, and a reference (in other words, a link) to the next node in the sequence.
    This structure allows for efficient insertion or removal of elements from any position in the sequence during iteration

    Time Complexity:
    Insertion: O(1)
    Insertion at beginning (or front): O(1)
    Insertion in between: O(1)
    Insertion at End: O(n)
    Deletion: O(1)
    Indexing: O(n)
    Searching: O(n)
    """

    def __init__(self):
        self.head = None

    # print values in linked list
    def printlinkedlist(self):
        tmp = self.head
        # print("chk tmp",tmp.val)
        while (tmp):
            print(tmp.val, end=" ")
            tmp = tmp.next

    # insert node at beginning

    def insertatstart(self, val):
        newnode = Node(val)
        newnode.next = self.head
        self.head = newnode

    # inserting the node after the given node in list
    def insertbetween(self, previousnode, data):
        if previousnode.next is None:
            print('Previous node should not be last node')
        else:
            newNode = Node(data)
            newNode.next = previousnode.next
            previousnode.next = newNode

    # inserting at the end of linked list
    def insertatend(self, data):
        newNode = Node(data)
        temp = self.head
        while temp.next != None:  # get last node
            temp = temp.next
        temp.next = newNode

    # deleting an item based on data(or key)
    def deletebyval(self, val):
        temp = self.head
        # if data/key is found in head node itself
        if temp.next is not None:
            if temp.val == val:
                self.head = temp.next
                temp = None
                return
            else:
                #  else search all the nodes
                while temp.next != None:
                    if temp.val == val:
                        break
                    prev = temp  # save current node as previous so that we can go on to next node
                    temp = temp.next

                # node not found
                if temp == None:
                    return

                prev.next = temp.next
                return

    # Given a reference to the head of a list
    # and a position, delete the node at a given position
    def deletebyposition(self, position):

        # If linked list is empty
        if self.head == None:
            return

        # Store head node
        temp = self.head

        # If head needs to be removed
        if position == 0:
            self.head = temp.next
            temp = None
            return

        # Find previous node of the node to be deleted
        for i in range(position - 1):
            temp = temp.next
            if temp is None:
                break

        # If position is more than number of nodes
        if temp is None:
            return
        if temp.next is None:
            return

        # Node temp.next is the node to be deleted
        # store pointer to the next of node to be deleted
        next = temp.next.next

        # Unlink the node from linked list
        temp.next = None

        temp.next = next

    # iterative search
    def search(self, node, val):
        # print('node',node)
        # print('val',val)
        if node == None:
            return False
        if node.val == val:
            return True
        return self.search(node.getpointer(), val)

    def isempty(self):
        return self.head is None


if __name__ == '__main__':
    # Check array class
    List = LinkedList()
    # List.printlinkedlist()
    print("chk1")
    List.head = Node(2)  # create the head node
    List.printlinkedlist()
    print("chk2")
    node2 = Node(2)
    List.head.setpointer(node2)  # head node's next --> node2
    node3 = Node(3)
    node2.setpointer(node3)  # node2's next --> node3
    List.insertatstart(4)  # node4's next --> head-node --> node2 --> node3
    List.insertbetween(node2, 5)  # node2's next --> node5
    List.insertatend(6)
    List.printlinkedlist()
    print()
    List.deletebyval(3)
    List.printlinkedlist()
    print()
    print(List.search(List.head, 1))
