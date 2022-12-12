import unittest
from day12 import part_1, part_2

class TestDay(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(
            part_1("""Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""),
            31
        )

    def test_part_2(self):
        self.assertEqual(
            part_2("TODO"),
            "TODO"
         )

if __name__ == '__main__':
    unittest.main()
