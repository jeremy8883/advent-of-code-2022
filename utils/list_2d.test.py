import unittest
from list_2d import map_2d_reverse, map_2d


class TestMap2D(unittest.TestCase):

    def test_map_2d(self):
        arr = [
            [1, 2],
            [3, 4],
            [5, 6],
        ]
        self.assertEqual(
            map_2d(lambda item, x, y, _: f"{item}, {x}, {y}", arr),
            [
                ["1, 0, 0", "2, 1, 0"],
                ["3, 0, 1", "4, 1, 1"],
                ["5, 0, 2", "6, 1, 2"],
            ]
        )

class TestMap2DReverse(unittest.TestCase):

    def test_map_2d_reverse(self):
        arr = [
            [1, 2],
            [3, 4],
            [5, 6],
        ]
        self.assertEqual(
            map_2d_reverse(lambda item, x, y, _: f"{item}, {x}, {y}", arr),
            [
                ["1, 0, 0", "2, 1, 0"],
                ["3, 0, 1", "4, 1, 1"],
                ["5, 0, 2", "6, 1, 2"],
            ]
        )
        # Does not mutate the original array
        self.assertEqual(
            arr,
            [
                [1, 2],
                [3, 4],
                [5, 6],
            ]
        )


if __name__ == '__main__':
    unittest.main()
