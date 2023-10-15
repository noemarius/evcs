import unittest
from models.charging_station import ChargingStation


class TestChargingStation(unittest.TestCase):
    def test_add_clock(self):
        cs = ChargingStation()
        self.assertEqual(cs._add_clock())
