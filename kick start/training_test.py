# 2019.4.11
# Kick Start 2019 - Round A
# Practice Mode

import unittest
from training import *

class KickStartTest(unittest.TestCase):
    def test_min_train(self):
        self.assertEqual(min_train([3, 1, 9, 100], 3), 14)
        self.assertEqual(min_train([5, 5, 1, 2, 3, 4], 2), 0)
        self.assertEqual(min_train([7, 7, 1, 7, 7], 5), 6)


if __name__ == '__main__':
    unittest.main()
