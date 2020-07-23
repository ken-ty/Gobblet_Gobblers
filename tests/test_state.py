import unittest


class TestState(unittest.TestCase):
    def test_encode(self):
        val = 10
        expect = "10"
        actual = State.encode(val)
        self.assertEqual(expect, actual)


if __name__ == '__main__':
    unittest.main()
