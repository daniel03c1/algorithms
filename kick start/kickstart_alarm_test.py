# 2019.4.22
# Kick Start 2019 - Round C
# Practice Mode

import unittest
import numpy as np
from random import randint
from kickstart_alarm import *

class KickStartTest(unittest.TestCase):
    def test_generate(self):
        # N, K, x1, y1, C, D, E1, E2, F
        config = [2, 3, 1, 2, 1, 2, 1, 1, 9]
        arr = generate(*config)
        self.assertTrue(np.all([3, 2] == arr))

    def test_total_power(self):
        config = [2, 3, 1, 2, 1, 2, 1, 1, 9]
        arr = generate(*config)
        power = total_power(arr, *config[:2])
        self.assertEqual(power, 52)

        config = [10, 10, 10001, 10002, 10003, 10004, 10005, 10006, 89273]
        arr = generate(*config)
        power = total_power(arr, *config[:2])
        self.assertEqual(power, 739786670)

    def test_sum_of_powers(self):
        self.assertEqual(sum_of_powers(2, 3), 14)

    def test_brute_and_total(self):
        for i in range(20):
            config = [randint(1,10), randint(1, 20)]   # N, K
            config.extend([randint(1, 100) for _ in range(7)])
            arr = generate(*config)
            total = total_power(arr, *config[:2])
            brute_force = brute(arr, *config[:2])
            self.assertEqual(total, brute_force, (arr, config))


if __name__ == '__main__':
    unittest.main()
