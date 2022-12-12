import unittest
from day12 import part_1, part_2

test_input = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""

class TestDay(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(
            part_1(test_input),
            31
        )

    def test_part_2(self):
        self.assertEqual(
            part_2(test_input),
            29
        )

if __name__ == '__main__':
    unittest.main()
