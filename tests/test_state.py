import unittest
import gobbletGobblers.state


class TestState(unittest.TestCase):
    def test___init__(self):
        patterns = [
            ((None, None), (0, 0)),
            ((None, None), (0, 0)),
            ((None, None), (0, 0)),
        ]
        for input_param, expect_param in patterns:
            with self.subTest('hogehoge'):
                black, white = input_param
                state = gobbletGobblers.state.State(black, white)
                expect_black, expect_white = expect_param
                expect = expect_black, expect_white
                actual = state.black, state.white
                self.assertEqual(expect, actual)

    def test___init__2(self):
        state = gobbletGobblers.state.State()
        expect = 0
        actual = state.white
        self.assertEqual(expect, actual)

    def test_encode(self, state=state):
        val = 10
        expect = "hoge"
        actual = state.encode()
        self.assertEqual(expect, actual)

if __name__ == '__main__':
    unittest.main()
