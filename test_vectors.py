
import unittest
import numpy as np

from vectors import (
    add_vectors,
    subtract_vectors,
    multiply_vectors,
    divide_vectors,
    calculate_dot_product,
)


class TestVectorOperations(unittest.TestCase):

    def test_add_vectors(self):
        result = add_vectors(
            np.array([1, 2, 3]),
            np.array([4, 5, 6])
        )
        np.testing.assert_array_equal(result, [5, 7, 9])

    def test_subtract_vectors(self):
        result = subtract_vectors(
            np.array([1, 2, 3]),
            np.array([4, 5, 6])
        )
        np.testing.assert_array_equal(result, [-3, -3, -3])

    def test_multiply_vectors(self):
        result = multiply_vectors(
            np.array([1, 2, 3]),
            np.array([4, 5, 6])
        )
        np.testing.assert_array_equal(result, [4, 10, 18])

    def test_divide_vectors(self):
        result = divide_vectors(
            np.array([1, 2, 3]),
            np.array([4, 5, 6])
        )
        np.testing.assert_allclose(result, [0.25, 0.4, 0.5])

    def test_dot_product(self):
        result = calculate_dot_product(
            np.array([1, 2, 3]),
            np.array([4, 5, 6])
        )
        self.assertEqual(result, 32)

    def test_dot_product_different_lengths(self):
        with self.assertRaises(ValueError):
            calculate_dot_product(
                np.array([1, 2]),
                np.array([3, 4, 5])
            )


if __name__ == "__main__":
    unittest.main()
