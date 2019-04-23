from sets import Set
import unittest


class TestSets(unittest.TestCase):

    def test_init(self):
        set = Set()
        assert set.hash_set.size == 0

    def test_size(self):
        set = Set()
        assert set.hash_set.size == 0
        set.add('I')
        assert set.hash_set.size == 1
        set.add('H')
        assert set.hash_set.size == 2
        set.add('F')
        set.add('T')
        assert set.hash_set.size == 4
        set.add('Y')
        assert set.hash_set.size == 5

    def test_contains(self):
        set = Set()
        set.add('G')
        set.add('T')
        set.add('R')
        set.add('F')
        assert set.contains('F') is True
        assert set.contains('R') is True
        assert set.contains('D') is False
        assert set.contains('G') is True
        assert set.contains('I') is False
        assert set.contains('E') is False
        set.add('I')
        assert set.contains('I') is True

    def test_add_and_remove(self):
        set = Set()
        set.add('I')
        assert set.hash_set.size == 1
        assert set.contains('T') is False
        assert set.contains('A') is False
        assert set.contains('I') is True
        set.add('T')
        set.add('F')
        assert set.hash_set.size == 3
        assert set.contains('F') is True
        set.add('T')
        set.add('F')
        assert set.hash_set.size == 3
        assert set.contains('F') is True
        set.add('K')
        assert set.hash_set.size == 4
        set.add('K')
        set.add('K')
        set.add('T')
        set.add('T')
        assert set.contains('K') is True
        assert set.contains('A') is False
        assert set.contains('T') is True
        assert set.hash_set.size == 4
        set.remove('T')
        set.remove('K')
        assert set.hash_set.size == 2
        set.add('A')
        set.add('A')
        assert set.hash_set.size == 3
        set.remove('A')
        assert set.hash_set.size == 2
        assert set.contains('A') is False
        with self.assertRaises(KeyError):
            set.remove('A')  # Key does not exist

        def union(self):
            set = Set()



if __name__ == '__main__':
    unittest.main()
