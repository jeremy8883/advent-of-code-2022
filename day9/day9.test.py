import unittest
from day9 import part_1, part_2

class TestDay(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(
            part_1("R 4\nU 4\nL 3\nD 1\nR 4\nD 1\nL 5\nR 2"),
            13
        )

    def test_part_2(self):
        self.assertEqual(
            part_2("R 4\nU 4\nL 3\nD 1\nR 4\nD 1\nL 5\nR 2"),
            1
        )
        self.assertEqual(
            part_2("R 5\nU 8\nL 8\nD 3\nR 17\nD 10\nL 25\nU 20"),
            36
        )

if __name__ == '__main__':
    unittest.main()
