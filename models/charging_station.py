
from datetime import datetime
from typing import List
from models.virtual_clock import VirtualClock
from abc import ABC


class ClockParameters(ABC):
    start: datetime
    end: datetime
    resolution: int


class ChargingStationSpecifications(ABC):
    peak_power: float
    number_of_connectors: int


class Telemetry(ABC):
    timestamp: datetime
    value: float


class Geometry(ABC):
    type: str
    coordinates: List[float]


class Feature(ABC):
    type: str
    properties: ChargingStationSpecifications


class GeoJSON(ABC):
    type: str
    features: List[Feature]


class ChargingStation:
    def __init__(self, geojson: GeoJSON, profile: object, clock_parameters: ClockParameters):
        self.geojson: GeoJSON = geojson
        self.profile: object = self._add_profile(profile)
        self.clock: VirtualClock = self._add_clock(clock_parameters)
        self.telemetry: List[Telemetry] = []

    def _add_clock(self, parameters: ClockParameters):
        return VirtualClock(parameters.start, parameters.end, parameters.resolution)

    def _add_profile(self, path):
        # from profile obj get the day's values
        # based on those either we  use them as is
        # or do we generate a variation (delta +/- some amount?)
        pass

    def gen_telemetry(self):
        # for each clock next()
        # read the profile values which match the timestamps

        pass
