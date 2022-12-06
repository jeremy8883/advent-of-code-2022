import unittest
from day6 import part_1, part_2

class TestDay(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(
            part_1("mjqjpqmgbljsphdztnvjfqwrcgsmlb"),
            7
        )
        self.assertEqual(
            part_1("bvwbjplbgvbhsrlpgdmjqwftvncz"),
            5
        )
        self.assertEqual(
            part_1("nppdvjthqldpwncqszvftbrmjlhg"),
            6
        )
        self.assertEqual(
            part_1("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"),
            10
        )
        self.assertEqual(
            part_1("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"),
            11
        )
    def test_part_2(self):
        self.assertEqual(
            part_2("mjqjpqmgbljsphdztnvjfqwrcgsmlb"),
            19
        )
        self.assertEqual(
            part_2("bvwbjplbgvbhsrlpgdmjqwftvncz"),
            23
        )
        self.assertEqual(
            part_2("nppdvjthqldpwncqszvftbrmjlhg"),
            23
        )
        self.assertEqual(
            part_2("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"),
            29
        )
        self.assertEqual(
            part_2("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"),
            26
        )

if __name__ == '__main__':
    unittest.main()
