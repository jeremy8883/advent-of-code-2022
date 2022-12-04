import unittest
from day3 import part_1

class TestDay(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(part_1("vJrwpWtwJgWrhcsFMMfFFhFp"), 16)
        self.assertEqual(part_1("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL"), 38)
        self.assertEqual(part_1("PmmdzqPrVvPwwTWBwg"), 42)
        self.assertEqual(part_1("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn"), 22)
        self.assertEqual(part_1("ttgJtRGJQctTZtZT"), 20)
        self.assertEqual(part_1("CrZsJsPPZsGzwwsLwLmpwMDw"), 19)
        self.assertEqual(
            part_1("vJrwpWtwJgWrhcsFMMfFFhFp\njqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\nPmmdzqPrVvPwwTWBwg\nwMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\nttgJtRGJQctTZtZT\nCrZsJsPPZsGzwwsLwLmpwMDw"),
            157
        )

if __name__ == '__main__':
    unittest.main()
