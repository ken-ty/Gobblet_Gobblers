import unittest
import state


class TestState(unittest.TestCase):
    def test_encode(self):
        val = 10
        expect = "10"
        actual = state.encode(val)
        self.assertEqual(expect, actual)
