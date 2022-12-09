import unittest
from point import is_point_nearby, new_point


class TestIsPointNearby(unittest.TestCase):

    def test_is_point_nearby(self):
        arr = [
            [1, 2],
            [3, 4],
            [5, 6],
        ]
        self.assertEqual(
            is_point_nearby(new_point(5, 10), new_point(5, 10)),
            True
        )
        self.assertEqual(
            is_point_nearby(new_point(5, 10), new_point(5, 11)),
            True
        )
        self.assertEqual(
            is_point_nearby(new_point(5, 10), new_point(5, 9)),
            True
        )
        self.assertEqual(
            is_point_nearby(new_point(5, 10), new_point(6, 10)),
            True
        )
        self.assertEqual(
            is_point_nearby(new_point(5, 10), new_point(4, 10)),
            True
        )
        self.assertEqual(
            is_point_nearby(new_point(5, 10), new_point(4, 12)),
            False
        )

if __name__ == '__main__':
    unittest.main()
