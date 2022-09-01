import unittest


class MyTestCase(unittest.TestCase):
    def test_add(self):
        result = 100+5
        self.assertEqual(result, 15)  # add assertion here


if __name__ == '__main__':
    unittest.main()
