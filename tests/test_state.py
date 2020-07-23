import unittest
import gobbletGobblers.state


class TestState(unittest.TestCase):
    def test_encode(self):
        state = gobbletGobblers.state.State()
        val = 10
        expect = "hoge"
        actual = state.encode()
        self.assertEqual(expect, actual)


if __name__ == '__main__':
    unittest.main()
