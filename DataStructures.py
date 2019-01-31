# Arrays
# Graph
# Heap
# Linkedlist
# Queue
# Sorting
# Stack
# Trees

class Array:
    """
    # Data Structure used to store homogeneous elements . Size has to be defined before hand
    Time complexity:

    Search: O(n)
    Insert: O(n)
    Delete: O(n)
    Indexing: O(1)
    YOu can import array library in python to get the similar functions
    """

    def __init__(self, arr_size, arr_type):

        self.Array_size = len(list(map(arr_type, range(arr_size))))
        # initialize array with zeroes
        self.Array_Items = [arr_type(0)] * arr_size

    # print array
    def __str__(self):
        return ' '.join([str(i) for i in self.Array_Items])

    # return length of array
    def __len__(self):
        return len(self.Array_Items)

    # Enable indexing
    def __setitem__(self, index, value):
        self.Array_Items[index] = value

    def __getitem__(self, index):
        return self.Array_Items[index]

    # Search key in array, if exists return it's index
    def search(self, key):
        for i in range(self.Array_size):
            if self.Array_Items[i] == key:
                return i
        return -1

    # insert key to the given position
    def insert(self, key, position):
        if self.Array_size > position:
            for i in range(self.Array_size - 2, position - 1, -1):
                self.Array_Items[i + 1] = self.Array_Items[i]
            self.Array_Items[position] = key
        else:
            print('Array size is:', self.Array_size)

    # delete the key from given position
    def delete(self, key, position):
        if self.Array_size > position:
            for i in range(position, self.Array_size - 1):
                self.Array_Items[i] = self.Array_Items[i + 1]
        else:
            print('Array size is:', self.Array_size)


if __name__ == '__main__':
    # Check array class
    a = Array(10, int)
    print(a)
    a.insert(8, 1)
    print(a)
    a.insert(7, 1)
    print(a)
    print(a.search(7))
    print(len(a))
    print(a[2])
    a[5] = 9
    print(a)
