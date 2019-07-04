from hashtable import HashTable

class Set(object):

    def __init__(self, elements=None):
        self.hashset = HashTable()
        self.size = 0

        if elements is not None:
            for element in elements:
                self.add(element)

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}'.format(item) for item in self.hashset.keys()]
        return '[' + ', '.join(items) + ']'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'Set({!r})'.format(self.hashset.keys())

    def contains(self, element):
        """ return a boolean indicating whether element is in this set """
         # time complexity: O(1)
        return self.hashset.contains(element)

    def add(self, element):
        """ add element to this set, if not present already """
        # O(1) for best case and O(n) worst case if the item is not found

        if self.hashset.contains(element) is False:
            self.size += 1
            self.hashset.set(element, None)

    def remove(self, element):
        """ remove element from this set, if present, or else raise KeyError """
        # O(1) constant time to find item and delete
        self.size -= 1
        self.hashset.delete(element)

    def union(self, other_set):
        """ return a new set that is the union of this set and other_set """
        # O(n * m) where n is amount of items in set one and m is the amount of set two
        new_set = Set()

        for element in self.hashset.keys():
            new_set.add(element)

        for element in other_set.hashset.keys():
            new_set.add(element)

        return new_set

    def intersection(self, other_set):
        """ return a new set that is the intersection of this set and other_set """
        # O(n) where n is the amount of items in set
        new_set = Set()

        for element in other_set.hashset.keys():
            if self.hashset.contains(element) is True:
                new_set.add(element)
        return new_set

    def difference(self, other_set):
        """ return a new set that is the difference of this set and other_set """
        new_set = Set()

        for element in other_set.hashset.keys():
            if self.contains(element) is False:
                new_set.add(element)
        return new_set

    def is_subset(self, other_set):
        """ return a boolean indicating whether other_set is a subset of this set """

        for element in other_set.hashset.keys():
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
    s.add('E')
    s.add('Y')
    s.add('Y')
    print('set: {}'.format(s))
    s.remove('Y')
    print('set: {}'.format(s))
    set = Set(['k', 'G', 'T'])
    other_set = Set(['K', 'T', 'R'])
    new_set = set.union(other_set)
    print('size: {}'.format(new_set.size))

    s_1 = Set(['A', 'B', 'C', 'D', 'E'])
    o_s = Set(['B', 'T', 'H', 'J', 'P', 'O'])
    print('intersection: {}'.format(s_1.intersection(o_s)))
    sss = Set(['k', 'G', 'T'])
    o_ss = Set(['K', 'T', 'R'])
    print(sss.union(o_ss))

if __name__ == '__main__':
    test_set()
