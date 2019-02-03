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

class BinaryHeap:
    """
    While building heap , heap structure property need to be maintain ( minHeap or maxHeap)
     1. It is a complete binary tree
    2. All nodes in the tree follow the property that they are greater than their children i.e.
    the largest element is at the root and both its children and smaller than the root and so on.
    Such a heap is called a max-heap. If instead all nodes are smaller than their children, it is called a min-heap

    buildheap : O(n); you can build the heap in O(n) is to remember that the
    logn factor is derived from the height of the tree.
    For most of the work in buildHeap, the tree is shorter than logn.

    Heap sort (nlogn)
    """

    def __init__(self):
        self.heap = [0]
        self.size = 0

    def insert(self, value):
        self.heap.append(value)
        self.size += 1
        self.heapifyup(self.size)

    def heapifyup(self, i):
        """

        This function ensure the heap structure property.
        as for every i child, parent is at i//2 . So we will check all child with parent
        and if child is less than parent than will switch value using tmp.

        :param i: size of heap
        :return: None
        """
        while i //2 >0:
            if self.heap[i] < self.heap[i //2]:
                tmp = self.heap[i // 2]
                self.heap[i // 2] = self.heap[i]
                self.heap[i] = tmp
            i = i //2

    def heapifydown(self, i):
        while (i * 2) <= self.size:
            minchild = self.minchild(i)
            if self.heap[i] > self.heap[minchild]:
                tmp = self.heap[i]
                self.heap[i] = self.heap[minchild]
                self.heap[minchild] = tmp
            i = minchild

    def minchild(self, i):

        if i * 2 + 1 > self.size:
            return i*2
        else:
            if self.heap[i*2] < self.heap[i*2+1]:
                return i*2
            else:
                return i*2 +1


    def delmin(self):
        # save root value in return variable
        ret = self.heap[1]
        # replace root value with last value of heap
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        # remove last element of heap
        self.heap.pop()
        self.heapifyup(self.size)
        return ret

    def buildheap(self, vallist):
        i = len(vallist) //2
        self.size = len(vallist)
        self.heap = [0] + vallist
        while (i>0) :
            self.heapifydown(i)
            i -= 1


if __name__ == '__main__':
    bh = BinaryHeap()
    bh.buildheap([9, 5, 6, 2, 3, 1, 4])
    print(bh.heap)
    print('Deleted:', bh.delmin())
    print('Deleted:', bh.delmin())
    print('Deleted:', bh.delmin())
    bh.insert(3)
    print('Deleted:', bh.delmin())