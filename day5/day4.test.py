import unittest
from day4 import part_1

class TestDay(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(
            part_1("    [D]\n[N] [C]\n[Z] [M] [P]\n 1   2   3\n\nmove 1 from 2 to 1\nmove 3 from 1 to 3\nmove 2 from 2 to 1\nmove 1 from 1 to 2"),
            "CMZ"
        )

if __name__ == '__main__':
    unittest.main()
