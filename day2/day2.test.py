import unittest
from day2 import part_1

class TestDay(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1("A Y"), 8)
        self.assertEqual(part_1("B X"), 1)
        self.assertEqual(part_1("C Z"), 6)
        self.assertEqual(part_1("A Y\nB X\nC Z"), 15)
        self.assertEqual(part_1("C Y"), 0 + 2)

if __name__ == '__main__':
    unittest.main()
