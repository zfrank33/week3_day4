import unittest
import hmwk_move as hm
class TestZeroMove(unittest.TestCase):

    def test_zero_move_1(self):
        self.assertEqual(hm.zeros_move( [0, 1, 0, 3, 12]), [1, 3, 12, 0, 0], "Should be [1, 3, 12, 0, 0]")
    def test_zero_move_2(self):
        self.assertEqual(hm.zeros_move( [1, 7, 0, 0, 8, 0, 10, 12, 0, 4,0]),[1, 7, 8, 10, 12, 4, 0, 0, 0, 0], "Should be [1, 7, 8, 10, 12, 4, 0, 0, 0, 0]")
    # def test_sum_tuple(self):
    #     self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

if __name__ == '__main__':
    unittest.main()
