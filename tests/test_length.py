from unittest import TestCase
from tests.functions.length_functions import(
    feet_to_meters,
    meters_to_feet,
    miles_to_kilos,
    kilos_to_miles
)


class LengthTests(TestCase):

    # Test that 1ft = 0.3m
    def test_feet_to_meters(self):

        self.assertEqual(feet_to_meters(1), 0.3)

    # Test that 1 m = 3.28 ft.
    def test_meters_to_feet(self):

        self.assertEqual(meters_to_feet(1), 3.28)

    # Test that 1 mi = 1.61 km (rounded)
    def test_miles_to_kilos(self):

        self.assertEqual(miles_to_kilos(1), 1.61)

    # Test that 1 km = 0.62 mi
    def test_kilos_to_miles(self):

        self.assertEqual(kilos_to_miles(1), 0.62)    