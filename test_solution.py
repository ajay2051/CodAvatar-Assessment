import unittest
import solution


class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_reverse(self):
        self.assertEqual(solution.reverse(52478), 87425)

        with self.assertRaises(ValueError):
            solution.reverse(-5214)

        with self.assertRaises(ValueError):
            solution.reverse(254.25)

    def test_number_length(self):
        self.assertEqual(solution.number_length(12547896), 8)

    def test_mul(self):
        self.assertEqual(solution.mul(45387), 7)


if __name__ == "__main__":
    unittest.main()
