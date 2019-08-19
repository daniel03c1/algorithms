# 2019.4.20
# Kick Start 2019 - Round A
# Practice Mode

import unittest
from random import randint
import numpy as np
from contention import *

class KickStartTest(unittest.TestCase):
    def test_book(self):
        cases = [([[1, 2], [3, 4], [2, 5]], 1),
                 ([[10, 11], [10, 10], [11, 11]], 0),
                 ([[1, 8], [4, 5], [3, 6], [2, 7]], 2),
                 ([[8, 11], [2, 10], [8, 9], [5, 12]], 2),
                 ([[1, 3], [4, 6], [8, 12], [6, 12]], 2)]

        for case in cases:
            self.assertEqual(book(99, case[0]), case[1], case)

        total = 12
        for i in range(5):
            random_cases = [sorted([randint(0, total), randint(0, total)]) \
                            for i in range(4)]
            print(book(total, random_cases), random_cases)

    def test_sorting(self):
        before = [[1, 3], [1, 4], [3, 4]]
        after = [[1, 3], [3, 4], [1, 4]]
        sort_booking(before)
        self.assertEqual(np.sum(np.abs(np.array(before) - after)),
                         0)        

    def test_merge(self):
        old = [[1, 4]]
        added, old = merge(old, [1, 5])
        self.assertEqual(added, 1)
        added, old = merge(old, [2, 6])
        self.assertEqual(added, 1)

    def test_num_of_seats(self):
        self.assertEqual(num_of_seats([1,1]), 1)
        self.assertEqual(num_of_seats([1,5]), 5)


if __name__ == '__main__':
    unittest.main()
