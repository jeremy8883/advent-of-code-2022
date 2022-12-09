import unittest
from day8 import part_1, part_2, get_scenic_score


class TestDay(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(
            part_1("30373\n25512\n65332\n33549\n35390"),
            21
        )

    def test_get_scenic_score(self):
        trees = [[3,0,3,7,3], [2,5,5,1,2], [6,5,3,3,2], [3,3,5,4,9], [3,5,3,9,0]]
        self.assertEqual(
            get_scenic_score(trees, 2, 0),
            2
        )
        self.assertEqual(
            get_scenic_score(trees, 2, 1),
            4
        )
        self.assertEqual(
            get_scenic_score(trees, 2, 3),
            8
        )

    def test_part_2(self):
        self.assertEqual(
            part_2("30373\n25512\n65332\n33549\n35390"),
            8
        )

if __name__ == '__main__':
    unittest.main()
