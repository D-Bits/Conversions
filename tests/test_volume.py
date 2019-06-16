from unittest import TestCase
from tests.functions.volume_functions import litres_to_gallons, gallons_to_litres


class VolumeTests(TestCase):

    def test_litres_to_gallons(self):

        self.assertEqual(litres_to_gallons(1), 0.26)

    def test_gallons_to_litres(self):

        self.assertEqual(gallons_to_litres(1), 3.79)