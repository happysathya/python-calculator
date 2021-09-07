from unittest import TestCase

from Calculator import Calculator


class TestCalculator(TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        result = self.calculator.add(10, 20)
        expected = 30
        self.assertEqual(expected, result)

