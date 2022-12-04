import unittest
from day4 import part_1, part_2

class TestDay(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(
            part_1("2-4,6-8\n2-3,4-5\n5-7,7-9\n2-8,3-7\n6-6,4-6\n2-6,4-8"),
            2
        )
    def test_part_2(self):
        self.assertEqual(
            part_2("2-4,6-8\n2-3,4-5\n5-7,7-9\n2-8,3-7\n6-6,4-6\n2-6,4-8"),
            4
        )

if __name__ == '__main__':
    unittest.main()
