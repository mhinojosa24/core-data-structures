from linkedlist import LinkedList

class Set(object):

    def __init__(self, elements=None):
        self.list = LinkedList()
        self.size = 0

        if elements is not None:
            for element in elements:
                self.add(element)

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['({!r})'.format(item) for item in self.elements()]
        return '[' + ', '.join(items) + ']'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'Set({!r})'.format(self.list.items())

    def elements(self):
        return self.list.items()

    def contains(self, element):
        """ return a boolean indicating whether element is in this set """
        item = self.list.find(lambda item: item == element)
        if item is not None:
            return True
        else:
            return False

    def add(self, element):
        """ add element to this set, if not present already """
        self.size += 1

        if element not in self.list.items():
            return self.list.append(element)

    def remove(self, element):
        """ remove element from this set, if present, or else raise KeyError """
        self.size -= 1
        self.list.delete(element)

    def union(self, other_set):
        """ return a new set that is the union of this set and other_set """
        new_set = Set()

        for element in self.list.items():
            new_set.add(element)

        for element in self.list.items():
            new_set.add(element)

        return new_set

    def intersection(self, other_set):
        """ return a new set that is the intersection of this set and other_set """
        new_set = Set()

        for element in other_set.list.items():
            if element in self.list:
                new_set.add(element)
        return new_set

    def difference(self, other_set):
        """ return a new set that is the difference of this set and other_set """
        new_set = Set()

        for element in other_set.list.items():
            if element not in self.list.items():
                new_set.add(element)
        return new_set

    def is_subset(self, other_set):
        """ return a boolean indicating whether other_set is a subset of this set """

        for element in other_set.list.items():
            if self.contains(element):
                return True

        return False

    def is_proper_subset(self, other_set):
        """ return a boolean indicating whether other_set is a proper subset of this set """

        if self.is_subset(other_set) == True and other_set.size < self.size:
            return True
        return False

def test_set():
    s = Set()
    s.add('I')
    # print('list => ', s.elements())
    s.add('E')
    s.add('Y')
    print(s.elements())
    print('set: {}'.format(s))
    s.remove('Y')
    print('set: {}'.format(s))
    set = Set(['k', 'G', 'T'])
    other_set = Set(['K', 'T', 'R'])
    new_set = set.union(other_set)
    print('size: {}'.format(new_set.size))

    s_1 = Set(['A', 'B', 'C', 'D', 'E'])
    o_s = Set(['B', 'T', 'H', 'J', 'P', 'O'])
    print('size of set 2: {}'.format(s_1.is_proper_subset(o_s)))

if __name__ == '__main__':
    test_set()
