from sets import Sets
import unittest


class TestSets(unittest.TestCase):

    def test_init(self):
        set = Set()
        assert set.size == 0

    def test_size(self):
        set = Set()
        assert set.size == 0
        set.add('I')
        assert set.size == 1
        set.add('H')
        assert set.size == 2
        set.add('F')
        set.add('T')
        assert set.size == 4
        set.add('Y')
        assert set.size == 5

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
        assert set.size == 1
        assert set.contains('T') is False
        assert set.contains('A') is False
        assert set.contains('I') is False
        set.add('T')
        set.add('F')
        assert set.size == 3
        set.add('T')
        set.add('F')
        assert set.size == 3
        assert set.contains('F') is False
        set.add('K')
        assert set.size == 4
        set.add('K')
        set.add('K')
        set.add('T')
        set.add('T')
        assert set.contains('K') is True
        assert set.contains('A') is False
        assert set.contains('T') is True
        assert set.size == 4
        set.remove('T')
        set.remove('K')
        assert set.size == 2
        set.add('A')
        set.add('A')
        assert set.size == 3
        set.remove('A')
        assert set.size == 2
        assert set.contains('A') is False

        def union(self):
            set = Set()


if __name__ == '__main__':
    unittest.main()
