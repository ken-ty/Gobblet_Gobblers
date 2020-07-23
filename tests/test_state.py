from unittest import TestCase
from gobbletGobblers.state import State


class TestState(TestCase):
    def test_encode(self):
        val = 10
        expect = "10"
        actual = State.encode(val)
        self.assertEqual(expect, actual)
