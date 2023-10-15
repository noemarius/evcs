from datetime import datetime


class VirtualClock:
    def __init__(self, start: datetime, end: datetime, resolution: int) -> None:
        if type(start) != datetime or type(end) != datetime:
            raise ValueError('Not a datetime')
        self.start: datetime = start
        self.end: datetime = end
        if type(resolution) != int:
            raise ValueError('Resolution has to be an int')
        if not resolution in [1, 15, 30, 60]:
            raise ValueError(
                'Resolution has to be one of the following: 1,15,30,60')
        self.resolution = resolution

    def gen_timestamps(self):
        pass
