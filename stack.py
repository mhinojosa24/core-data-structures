from linkedlist import LinkedList


class LinkedStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        return self.list.is_empty()

    def length(self):
        """Return the number of items in this stack."""
        # time complexity: O(n) n for items in a list
        return self.list.length()

    def push(self, item):
        """Insert the given item on the top of this stack."""
        # time complexity: O(1) constant to add an item to list
        self.list.prepend(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        # time complexity: O(1) checks if there is a item in list

        if self.list.is_empty() == False: # constant time to call is_empty method
            return self.list.head.data
        return None

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty."""
        # Running time: O(1) constant to delete item from the beginning of the list

        if self.list.is_empty() == True: # constant time to call is_empty method
            raise ValueError('List is empty')
        else:
            value = self.list.head.data
            self.list.delete(self.list.head.data) # constant to call delete method and delete item from list
            return value

# Implement ArrayStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class ArrayStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        # time complexity: O(n) n for items in list

        return len(self.list) == 0

    def length(self):
        """Return the number of items in this stack."""
        # time complexity: O(n) n for items in list

        return len(self.list)

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(???) – Why? [TODO]"""
        # time complexity: O(1) constant to add itme at the end of list

        self.list.append(item)


    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        if len(self.list) != 0:
            return self.list[-1]
        return None

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(???) – Why? [TODO]"""
        if len(self.list) > 0:
            value = self.list[-1]
            del self.list[-1]
        else:
            raise ValueError('Oops the list is empty')
        return value

# Implement LinkedStack and ArrayStack above, then change the assignment below
# to use each of your Stack implementations to verify they each pass all tests
Stack = LinkedStack
# Stack = ArrayStack
