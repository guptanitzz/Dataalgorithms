# Arrays
# , array is a static data structure (residing in Data or Stack section)
## while linked list is a dynamic data structure (residing in Heap section).
# Linkedlist
# Stack
# Queue

# Graph
# Heap
# Trees
# Sorting
# Searching



class Queue:
    """
    A queue is an ordered collection of items where the addition of new items happens at one end,
    called the “rear,” and the removal of existing items occurs at the other end,
     commonly called the “front.” (FIFO)
    Example of queue are. waiting in a line for a movie, waiting in the check-out line at a grocery store

    Applications :
    When a resource is shared among multiple consumers likeCPU scheduling, Disk Scheduling.
    When data is transferred asynchronously between two processes like IO Buffers, pipes, file IO, etc.
    Keyboard: As we type, sometimes keystrokes get ahead of the characters that appear on the screen.
    This is due to the computer doing other work at that moment. The keystrokes are being placed in a queue-like buffer
    so that they can eventually be displayed on the screen in the proper order.


    Time Complexities:
    enqueue(): O(1)
    dequeue(): O(1)
    isEmpty(): O(1)
    getSize(): O(1)

    """

    def __init__(self):
        self.items = []

    # print values in Stack
    def __str__(self):
        return ' '.join(str(x) for x in self.items)

    # push value
    def enqueue(self, val):
        self.items.insert(0, val)

    # pop value
    def dequeue(self):
        if self.isempty():
            print('Empty Queue')
            return
        else:
            return self.items.pop()

    # check if empty
    def isempty(self):
        return self.items == []

    def size(self):
        return len(self.items)


class Deque:
    """
    (Double ended queue): Supports insert and delete at both the ends (front as well as rear) of the queue.
    Likewise, existing items can be removed from either end. In a sense, this hybrid linear structure
    provides all the capabilities of stacks and queues in a single data structure

    Time Complexities:
    enqueue(): O(1)
    dequeue(): O(1)
    isEmpty(): O(1)
    getSize(): O(1)

    """

    def __init__(self):
        self.items = []

    # print values in Stack
    def __str__(self):
        return ' '.join(str(x) for x in self.items)

    def addrear(self, val):
        self.items.insert(0, val)

    def addfront(self, val):
        self.items.append(val)

    def removefront(self):
        if self.isempty():
            return
        else:
            return self.items.pop()

    def removerear(self):
        if self.isempty():
            return
        else:
            return self.items.pop(0)

    # check if empty
    def isempty(self):
        return self.items == []

    def size(self):
        return len(self.items)


class Node:
    def __init__(self, val, priority):
        self.val = val
        self.priority = priority

class PriorityQueue:
    """
    Priority Queue is an extension of the queue with following properties.
    1) An element with high priority is dequeued before an element with low priority.
    2) If two elements have the same priority, they are served according to their order in the queue.

    Applications :
    1) CPU Scheduling
    2) Graph algorithms like Dijkstra’s shortest path algorithm, Prim’s Minimum Spanning Tree, etc
    3) All queue applications where priority is involved.

    Time Complexities:
     delete : O(n)

    """

    def __init__(self):
        self.items = []

    # print values in queue
    def show(self):
        for x in self.items:
            print(str(x.val) + " - " + str(x.priority))

    def insert(self, val):
        # if queue is empty
        if self.size() == 0:
            # add the new node
            self.items.append(val)
        else:
            # traverse the queue to find the right place for new node
            for x in range(0, self.size()):
                # if the priority of new node is greater
                if val.priority >= self.items[x].priority:
                    # if we have traversed the complete queue
                    if x == (self.size() - 1):
                        # add new node at the end
                        self.items.insert(x + 1, val)
                    else:
                        continue
                else:
                    self.items.insert(x, val)
                    return True

    def delete(self):
        # remove the first node from the queue
        return self.items.pop(0)

    # check if empty
    def isempty(self):
        return self.items == []

    def size(self):
        return len(self.items)


class CircularQueue:
    """
    A queue in which last position is connected back to front

    Time Complexities:

    Application:
    Computer Architecture (Scheduler)
    Disk drivers
    Video buffering
    Printer job scheduling


    """

    def __init__(self):
        self.items = []
        self.head = 0
        self.tail = 0

    # print values in Stack
    def __str__(self):
        return ' '.join(str(x) for x in self.items)

    # Adding elements to the queue
    def enqueue(self, val):
        self.items.append(val)
        self.tail = self.tail + 1
        return True

    # Removing elements from the queue
    def dequeue(self):
        if self.isempty():
            return ("Queue Empty!")

        data = self.items[self.head]
        self.head = self.head -1
        return data

    # Calculating the size of the queue
    def size(self):
        if self.tail >= self.head:
            return self.tail - self.head
        else:
            return

    # check if empty
    def isempty(self):
        return self.items == []


# Palindrome checker using Deque
def checkpalindrome(word):

    equalflag = True
    dq = Deque()

    for w in word:
        dq.addrear(w)

    while dq.size()>1 and equalflag:
        front = dq.removefront()
        rear = dq.removerear()
        if front != rear:
            equalflag=False

    return  equalflag


if __name__ == '__main__':
    # Check queues class

    #Queue
    st = Queue()
    print(st.isempty())

    st.enqueue(1)
    st.enqueue(2)
    st.enqueue(4)
    st.enqueue(-1)
    print(st.size())

    print(st)
    st.dequeue()
    print(st)
    print(st.isempty())

    # Dequeue
    dq = Deque()
    print(dq.isempty())
    dq.addrear('hello')
    dq.addrear('buffalo')
    dq.addfront('cat')
    dq.addrear('mat')
    print(dq.size())
    print(dq.isempty())
    dq.addrear('zz')
    print(dq)
    print(dq.removerear())
    print(dq.removefront())

    # check palindrom function

    print(checkpalindrome("weather"))
    print(checkpalindrome("madam"))


    ## Priority Queue
    print("Priority queue")
    pq = PriorityQueue()
    node1 = Node("C", 3)
    node2 = Node("B", 2)
    node3 = Node("A", 1)
    node4 = Node("Z", 26)
    node5 = Node("Y", 25)
    node6 = Node("L", 12)
    pq.insert(node1)
    pq.insert(node2)
    pq.insert(node3)
    pq.insert(node4)
    pq.insert(node5)
    pq.insert(node6)
    pq.show()
    pq.delete()
    pq.show()

    #Circular queue
    print("Circular queue")
    q = CircularQueue()
    print(q.enqueue(1))
    print(q.enqueue(2))
    print(q.enqueue(3))
    print(q.enqueue(4))
    print(q.enqueue(5))
    print(q.enqueue(6))
    print(q.enqueue(7))
    print(q.enqueue(8))
    print(q.enqueue(9))
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())