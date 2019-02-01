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


class Stack:
    """
    # Stacks are dynamic data structures that follow the Last In First Out (LIFO) principle.
    The last item to be inserted into a stack is the first one to be deleted from it.

    Application
    balanced parentheses problem.

    You have a bracket sequence made up of opening '(' and closing ')' parentheses.
    You must check if this bracket sequence is balanced.
    A bracket sequence is considered balanced if for every prefix of the sequence,
    the number of opening brackets is greater than or equal to the number of closing brackets,
    and the total number of opening brackets is equal to the number of closing brackets.

    You can check this using stack.
    You can maintain a stack where you store a parenthesis.
    Whenever, you come across an opening parenthesis,  it in the stack.
    However, whenever you come across a closing parenthesis,  a parenthesis from the stack.

    Stacks are fundamentally important, as they can be used to reverse the order of items.

    every web browser has a Back button.
    As you navigate from web page to web page, those pages are placed on a stack
    (actually it is the URLs that are going on the stack).
    The current page that you are viewing is on the top and the first page you looked at is at the base.
    If you click on the Back button, you begin to move in reverse order through the pages.

    Time Complexities:
    Push: O(1)
    Pop: O(1)
    Peek: O(1)
    isEmpty: O(1)
    Size: O(1)

    Stack implementation using List. Assuming start of the list is base
    """

    def __init__(self):
        self.items = []

    # print values in Stack
    def __str__(self):
        return ' '.join(str(x) for x in self.items)

    # push value
    def push(self, val):
        self.items.append(val)

    # pop value
    def pop(self):
        if len(self.items) <= 0:
            print('SEmpty stack')
            return
        else:
            return self.items.pop()

    # check if empty
    def isempty(self):
        return self.items == []

    def peek(self):
        if len(self.items) <= 0:
            print('SEmpty stack')
            return
        else:
            return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


# parantheis checker

def balancedparanthesis(paraString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(paraString) and balanced:
        symbol = paraString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isempty():
                balanced = False
            else:
                s.pop()

        index = index + 1

    if balanced and s.isempty():
        return True
    else:
        return False


if __name__ == '__main__':
    # Check stack class
    st = Stack()
    print(st.isempty())
    st.push(1)
    st.push(2)
    st.push(4)
    st.push(-1)
    print(st)
    st.pop()
    print(st)
    print(st.peek())
    print(st.isempty())

    print(balancedparanthesis('((()))'))
    print(balancedparanthesis('(()'))
