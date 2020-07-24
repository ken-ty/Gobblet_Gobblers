# coding=utf-8
import unittest
import gobbletGobblers.state
import gobbletGobblers.bitExpression as be
import numpy as np


class TestState(unittest.TestCase):
    def test___init__(self):
        patterns = [
            ((None, None), (be.EMPTY, be.EMPTY)),  # 空の初期化
            ((be.C3S, None), (be.C3S, be.EMPTY)),  # blackのみ引数を指定
            ((None, be.A1L), (be.EMPTY, be.A1L)),  # white飲み引数を指定
            ((be.A1L, be.A1M), (be.A1L, be.A1M)),  # 単一のコマがある盤面
            ((be.A2M | be.B3S, be.A1M), (be.A2M | be.B3S, be.A1M)),  # 複数のコマがある盤面
            ((np.uint32(0xFFFFFFFF), np.uint32(0xFFFFFFFF)), (np.uint32(0xFFFFFFFF), np.uint32(0xFFFFFFFF))),  #
            # uint32の限界
        ]
        for input_param, expect_param in patterns:
            black, white = input_param
            state = gobbletGobblers.state.State(black, white)
            expect = expect_param  # expect_param == expect_black, expect_white
            actual = state.black, state.white
            self.assertEqual(expect, actual)

    def test_encode(self):
        patterns = [
            (be.EMPTY, be.EMPTY),

        ]
        for input_param, expect_param in patterns:
            expect = expect_param
            actual = gobbletGobblers.state.encode(input_param)
            self.assertEqual(expect, actual)


if __name__ == '__main__':
    unittest.main()
