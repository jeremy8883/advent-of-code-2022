import unittest
from day2 import part_1, part_2

class TestDay(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1("A Y"), 8)
        self.assertEqual(part_1("B X"), 1)
        self.assertEqual(part_1("C Z"), 6)
        self.assertEqual(part_1("A Y\nB X\nC Z"), 15)
        self.assertEqual(part_1("C Y"), 0 + 2)
    def test_part_2(self):
        self.assertEqual(part_2("A Y"), 4)
        self.assertEqual(part_2("B X"), 1)
        self.assertEqual(part_2("C Z"), 7)
        self.assertEqual(part_2("A Y\nB X\nC Z"), 12)

if __name__ == '__main__':
    unittest.main()
