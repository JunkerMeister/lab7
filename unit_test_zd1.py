import unittest
from zd_1 import count_ways_to_climb

class TestCountWaysToClimb(unittest.TestCase):
    def test_count_ways_to_climb(self):
        self.assertEqual(count_ways_to_climb(5), 8)
        self.assertEqual(count_ways_to_climb(10), 89)


if __name__ == '__main__':
    unittest.main()
