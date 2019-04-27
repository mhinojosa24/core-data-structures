from hashtable import HashTable

class Set(object):

    def __init__(self, elements=None):
        self.hash_set = HashTable()

        if elements is not None:
            for element in elements:
                self.add(element)

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.hash_set.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'Set({!r})'.format(self.hash_set.items())

    def contains(self, element):
        """ return a boolean indicating whether element is in this set """
        return self.hash_set.contains(element)

    def add(self, element):
        """ add element to this set, if not present already """
        if self.hash_set.contains(element) is False:
            return self.hash_set.set(element, None)

    def remove(self, element):
        """ remove element from this set, if present, or else raise KeyError """
        self.hash_set.delete(element)

    def union(self, other_set):
        """ return a new set that is the union of this set and other_set """
        new_set = Set()

        for element in self.hash_set.keys():
            new_set.add(element)

        for element in other_set.hash_set.keys():
            new_set.add(element)

        return new_set

    def intersection(self, other_set):
        """ return a new set that is the intersection of this set and other_set """
        new_set = Set()

        for element in other_set.hash_set.keys():
            if element in self.hash_set.keys():
                new_set.add(element)
        return new_set

    def difference(self, other_set):
        """ return a new set that is the difference of this set and other_set """
        new_set = Set()

        for element in other_set.hash_set.keys():
            if element not in self.hash_set.keys():
                new_set.add(element)
        return new_set

    def is_subset(self, other_set):
        """ return a boolean indicating whether other_set is a subset of this set """
        is_subset = False

        



def test_set():
    s = Set()
    s.add('I')
    s.add('E')
    s.add('Y')
    print('set: {}'.format(s))
    s.remove('Y')
    print('set: {}'.format(s))
    set = Set(['k', 'G', 'T'])
    other_set = Set(['K', 'T', 'R'])
    new_set = set.union(other_set)
    print('size: {}'.format(new_set.hash_set.size))


if __name__ == '__main__':
    test_set()
