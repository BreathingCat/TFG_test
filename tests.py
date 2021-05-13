import unittest
import functions

class TestBatter(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(3, functions.sum_test(1, 2))

    def test_sum2(self):
        self.assertEqual(3, functions.sum_test(1, 2))


if __name__ == '__main__':
    unittest.main()
