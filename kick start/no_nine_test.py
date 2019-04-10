# 2019.4.10
# Kick Start 2018 - Round B
# Practice Mode

import unittest
from random import randint
from no_nine import *

class KickStartTest(unittest.TestCase):
    def test_no_nine(self):
        self.assertEqual(no_nine('16', '26'), 9)
        self.assertEqual(no_nine('88', '102'), 4)

    def test_count_legal(self):
        for i in range(10):
            num = 0
            while is_legal(num):
                num = randint(1, 100000)
            
            self.assertEqual(brute_count_legal(num),
                             count_legal(str(num)),
                             "num:{}".format(num)),


if __name__ == '__main__':
    unittest.main()
