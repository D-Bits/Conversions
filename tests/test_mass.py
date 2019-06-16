from unittest import TestCase
from tests.functions.mass_functions import pounds_to_kilograms, kilograms_to_pounds


class MassTests(TestCase):

    # Ensure that 1 lbs = 0.45 kgs
    def test_pounds_to_kilos(self):

        self.assertEqual(pounds_to_kilograms(1), 0.45)

    # Ensure that 1 kg equals 2.2 lbs
    def test_kilos_to_pounds(self):

        self.assertEqual(kilograms_to_pounds(1), 2.2)