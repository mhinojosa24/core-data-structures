from hashtable import HashTable

class Set(object):

    def __init__(self, elements=None):
        self.set = HashTable()
        self.size = 0

    def contains(self, element):
        """ return a boolean indicating whether element is in this set """
        pass

    def add(self, element):
        """ add element to this set, if not present already """
        pass

    def remove(self, element):
        """ remove element from this set, if present, or else raise KeyError """
        pass

    def union(self, other_set):
        """ return a new set that is the union of this set and other_set """
        pass

    def intersection(self, other_set):
        """ return a new set that is the intersection of this set and other_set """
        pass

    def difference(self, other_set):
        """ return a new set that is the difference of this set and other_set """
        pass

    def is_subset(self, other_set):
        """ return a boolean indicating whether other_set is a subset of this set """
        pass

    def test_set(self):
        set = Set()


if __name__ == '__main__':
    test_set()
