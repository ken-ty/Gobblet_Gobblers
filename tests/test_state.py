import unittest
import gobbletGobblers.state
import gobbletGobblers.bitExpression as be
import numpy as np


class TestState(unittest.TestCase):
    def test___init__(self):
        patterns = [
            ((None, None), (be.EMPTY, be.EMPTY)),
            ((be.C3S, None), (be.C3S, be.EMPTY)),
            ((None, be.A1L), (be.EMPTY, be.A1L)),
            ((be.A1L, be.A1M), (be.A1L, be.A1M)),
            ((be.A2M | be.B3S, be.A1M), (be.A2M | be.B3S, be.A1M)),
            ((np.uint32(0xFFFFFFFF), np.uint32(0xFFFFFFFF)), (np.uint32(0xFFFFFFFF), np.uint32(0xFFFFFFFF))),
        ]
        for input_param, expect_param in patterns:
            black, white = input_param
            state = gobbletGobblers.state.State(black, white)
            expect = expect_param  # expect_param == expect_black, expect_white
            actual = state.black, state.white
            self.assertEqual(expect, actual)


if __name__ == '__main__':
    unittest.main()
