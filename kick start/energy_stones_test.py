# 2019.8.19
# Kick Start 2019 - Round B
# Practice Mode
# TIME LIMIT EXCEEDED

import unittest
from random import randint
from energy_stones import *

class KickStartTest(unittest.TestCase):
    def test_maximum_energy(self):
        # Seconds to eat, Initial Energy, Energy loss per sec
        problem_1 = [[20, 10, 1],
                     [5, 30, 5],
                     [100, 30, 1],
                     [5, 80, 60]]
        problem_2 = [[10, 4, 1000],
                     [10, 3, 1000],
                     [10, 8, 1000]]
        problem_3 = [[12, 300, 50],
                     [5, 200, 0]]
        self.assertEqual(max_energy(problem_1), 105)
        self.assertEqual(max_energy(problem_2), 8)
        self.assertEqual(max_energy(problem_3), 500)

    def test_time_limit(self):
        for i in range(100):
            n_stones = 500
            sec_lim = 100
            energy_lim = 100000
            energy_los = 100000

            stones = []
            for i in range(n_stones):
                stones.append([randint(1, sec_lim),
                               randint(0, energy_lim),
                               randint(0, energy_los)])
            max_energy(stones)


if __name__ == '__main__':
    unittest.main()
