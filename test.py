"""
Testcases for Raytracer in Python
Author: Anirudh Rowjee
"""
import unittest
import math
from vector import Vector
from ppmutils import ImageWriter


class VectorTest(unittest.TestCase):
    """
    Test class for Vector Object
    """

    def setUp(self):
        """
        setup - create all static data necessary
        """
        # test vector co-ordinate values
        self.test_vector = (1, 2, 3)
        self.test_vector_alternate = (4, 5, 6)

    def test_creation(self):
        """
        Create a vector
        """
        x, y, z = self.test_vector
        new_vector = Vector(x, y, z)

        self.assertEqual(new_vector.x, x)
        self.assertEqual(new_vector.y, y)
        self.assertEqual(new_vector.z, z)

    def test_null_value_rejection(self):
        """
        test if Vector rejects a set of Null values
        """
        x, y, z = self.test_vector
        y = None

        with self.assertRaises(TypeError):
            new_vector = Vector(x, y, z)

    def test_magnitude(self):
        """
        test correctness of magnitude reporting
        """
        x, y, z = self.test_vector
        new_vector = Vector(x, y, z)
        magnitude = math.sqrt((x ** 2) + (y ** 2) + (z ** 2))

        self.assertEqual(magnitude, new_vector.magnitude)

    def test_direction(self):
        """
        test direction of vector
        """
        x, y, z = self.test_vector
        new_vector = Vector(x, y, z)
        direction = list(map(lambda x: x / new_vector.magnitude, (x, y, z)))

        self.assertEqual(direction, new_vector.direction)

    def test_dot_product(self):
        """
        test functioning of dot product of two vectors
        """
        vector1 = Vector(*self.test_vector)
        vector2 = Vector(*self.test_vector_alternate)

        dot_product = sum(
            x * y for x, y in zip(self.test_vector, self.test_vector_alternate)
        )

        self.assertEqual(dot_product, vector1.dot(vector2))
        self.assertEqual(dot_product, vector2.dot(vector1))

    def test_addition(self):
        """
        test addition of two vectors
        """
        vector1 = Vector(*self.test_vector)
        vector2 = Vector(*self.test_vector_alternate)

        sum1 = vector1 + vector2
        sum2 = vector2 + vector1

        # final sum vector, by adding the values before inserting them
        result_vector = Vector(
            *(x + y for x, y in zip(self.test_vector, self.test_vector_alternate))
        )

        self.assertTrue(sum1 == result_vector)
        self.assertTrue(sum2 == result_vector)

    def test_subtraction(self):
        vector1 = Vector(*self.test_vector)
        vector2 = Vector(*self.test_vector_alternate)

        left_sub_vector_true = vector1 - vector2
        right_sub_vector_true = vector2 - vector1

        left_sub_vector_expected = Vector(
            *(x - y for x, y in zip(self.test_vector, self.test_vector_alternate))
        )
        right_sub_vector_expected = Vector(
            *(x - y for x, y in zip(self.test_vector_alternate, self.test_vector))
        )

        self.assertTrue(left_sub_vector_true == left_sub_vector_expected)
        self.assertTrue(right_sub_vector_true == right_sub_vector_expected)

    def test_multiplication(self):
        vector = Vector(*self.test_vector)
        new_vector_1 = vector * 3.0
        new_vector_2 = vector * 3

        new_vector_1_expected = Vector(*list(map(lambda x: x * 3.0, self.test_vector)))
        new_vector_2_expected = Vector(*list(map(lambda x: x * 3, self.test_vector)))

        self.assertTrue(new_vector_1 == new_vector_1_expected)
        self.assertTrue(new_vector_2 == new_vector_2_expected)

        new_vector_1 = 3.0 * vector
        new_vector_2 = 3 * vector

        self.assertTrue(new_vector_1 == new_vector_1_expected)
        self.assertTrue(new_vector_2 == new_vector_2_expected)

    def test_multiplication_error(self):
        vector = Vector(*self.test_vector)
        with self.assertRaises(TypeError):
            vector * []

    def test_division(self):
        vector = Vector(*self.test_vector)
        new_vector_1 = vector / 3.0
        new_vector_2 = vector / 3

        new_vector_1_expected = Vector(*list(map(lambda x: x / 3.0, self.test_vector)))
        new_vector_2_expected = Vector(*list(map(lambda x: x / 3, self.test_vector)))

        self.assertTrue(new_vector_1 == new_vector_1_expected)
        self.assertTrue(new_vector_2 == new_vector_2_expected)

    def test_division_error(self):
        vector = Vector(*self.test_vector)
        with self.assertRaises(TypeError):
            vector / []


class PPMUtilsTest(unittest.TestCase):
    """
    Test Class for PPM Utils object
    """

    def setUp(self):
        """
        Setup method for testcases for ImageWriter
        """
        pass

    def test_initialization(self):
        """
        check to see if the class initializes
        """
        img_writer = ImageWriter(10, 10, 255)
        self.assertEqual(img_writer.height, 10)
        self.assertEqual(img_writer.width, 10)
        self.assertEqual(img_writer.limit, 255)

    def test_file_header_generation(self):
        """
        check to see if file header is generated properly for a given PPM file
        spec
        """
        height = 10
        width = 15
        limit = 255
        img_writer = ImageWriter(height, width, limit)
        self.assertEqual(img_writer.header, f"P3 {width} {height}\n{limit}\n")

    def test_vector_normalization(self):
        """
        check to see if vectors with component magnitudes ranging from 0 to 1
        are normalized to values within the limit into a tuple of the values
        i.e.
        * vectors with (0.1, 0.2, 0.3) with limit 10 should have normalized
        representations as (1, 2, 3)
        * vectors with (11, 5, 9) with limit 10 should have normalized
        representations as (10, 5, 9) (hard ceiling at limit)
        """
        writer = ImageWriter(3, 3, 100)

        test_vector_1 = Vector(0.1, 0.2, 0.3)
        test_vector_2 = Vector(1, 0.5, 0.57)
        test_vector_3 = Vector(10, 20, 30)

        self.assertEqual(writer.normalize(test_vector_1), (10, 20, 30))
        self.assertEqual(writer.normalize(test_vector_2), (100, 50, 57))
        self.assertEqual(writer.normalize(test_vector_1), (100, 100, 100))

    def test_normalized_tuple_formatting(self):
        """
        Test the formatting of the tuple into the space-padded format it'll be
        written to the PPM file in
        i.e "1, 10, 100" becomes "  1  10 100" (max three characters for each
        component, with one character space between each of them)

        """
        self.assertEqual(1, 1)

    def test_vector_grid_formatting(self):
        """
        test the formatting of the MxN grid of vector tuples (each formatted
        tuple separated by three spaces or a tab
        """
        self.assertEqual(1, 1)

    def test_image_writing(self):
        """
        test writing the formatted vector grid to the file, along with the
        header.
        """
        self.assertEqual(1, 1)


if __name__ == "__main__":
    unittest.main()
