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

    def test_union(self):
        s = Set(['k', 'G', 'T'])
        o_s = Set(['K', 'T', 'R'])
        n_s = s.union(o_s)

        self.assertCountEqual(n_s.hash_set.keys(), ['k', 'K', 'G', 'T', 'R'])
        assert n_s.hash_set.size == 5

        s_2 = Set(['m', 'M', 'l', 'Y', 'O'])
        o_s_2 = Set(['P', 'M', 'l', 'Y'])
        n_s_2 = s_2.union(o_s_2)

        self.assertCountEqual(n_s_2.hash_set.keys(), ['m', 'M', 'l', 'Y', 'O', 'P'])
        assert n_s_2.hash_set.size == 6

        s_3 = Set([5, 4, 5, 6, 0])
        o_s_3 = Set([6, 7, 7, 4])
        n_s_3 = s_3.union(o_s_3)

        self.assertCountEqual(n_s_3.hash_set.keys(), [5, 4, 6, 0, 7])
        assert n_s_3.hash_set.size == 5

    def test_intersection(self):
        s = Set(['T', 'Y', 'I', 'P'])
        o_s = Set(['P', 'I', 'T'])
        n_s = s.intersection(o_s)

        self.assertCountEqual(n_s.hash_set.keys(), ['T', 'I', 'P'])
        assert n_s.hash_set.size == 3

        s_2 = Set([2, 0, 0, 8])
        o_s_2 = Set([2, 8, 0])
        n_s_2 = s_2.intersection(o_s_2)

        self.assertCountEqual(n_s_2.hash_set.keys(), [2, 0, 8])
        assert n_s_2.hash_set.size == 3

    def test_difference(self):
        s = Set(['T', 'Y', 'O', 'P'])
        o_s = Set(['T', 'R', 'V', 'O'])
        n_s = s.difference(o_s)

        self.assertCountEqual(n_s.hash_set.keys(), ['R', 'V'])
        assert n_s.hash_set.size == 2

        s_2 = Set([1, 3, 5, 6])
        o_s_2 = Set([1, 6, 2, 4, 5])
        n_s_2 = s_2.difference(o_s_2)

        self.assertCountEqual(n_s_2.hash_set.keys(), [2, 4])
        assert n_s_2.hash_set.size == 2

    def is_subset(self):
        s = Set(['A', 'B', 'C', 'D'])
        o_s = Set(['A', 'C', 'D'])
        n_s = s.is_subset(o_s)

        self.assertCountEqual(n_s.hash_set.keys(), [])

if __name__ == '__main__':
    unittest.main()
