from typing import List
import pandas as pd

import numpy as np
from datetime import datetime, timedelta
# from models.virtual_clock import VirtualClock
# from scipy.interpolate import CubicSpline


# def piecewise_linear_interpolation(data_points, target_timestamp):
#     data_points.sort(key=lambda x: x[0])
#     for i in range(1, len(data_points)):
#         if data_points[i][0] >= target_timestamp:
#             t1, v1 = data_points[i - 1]
#             t2, v2 = data_points[i]
#             break
#     return v1 + (target_timestamp - t1) * (v2 - v1) / (t2 - t1)


# def spline_interpolation(data_points, target_timestamp):
#     t, v = zip(*data_points)
#     spline = CubicSpline(t, v)
#     return spline(target_timestamp)


# def polynomial_interpolation(data_points, target_timestamp):
#     t, v = zip(*data_points)
#     coefficients = np.polyfit(t, v, len(data_points) - 1)
#     return np.polyval(coefficients, target_timestamp)


def linear_interpolation(t1, v1, t2, v2, target_timestamp):
    return v1 + (target_timestamp - t1) * (v2 - v1) / (t2 - t1)


def gen_time_list(resolution: int) -> List:
    if type(resolution) != int:
        raise ValueError('Resolution needs to be an int')
    start = datetime.strptime("00:00", "%H:%M")
    end = datetime.strptime("23:59", "%H:%M")

    time_delta = timedelta(minutes=resolution)
    times = []
    while start < end:
        times.append(start.strftime("%H:%M"))
        start = start + time_delta
    times.append(end.strftime("%H:%M"))
    return times


class Profile:
    def __init__(self, resolution: int, path: str) -> None:
        self.input_profile_data = self._get_data(path)
        self.resolution = resolution
        self.processed_data = self._populate_missing_data_points(resolution)

    def _get_data(self, path):
        with open(path, 'r', encoding='utf-8') as file:
            return pd.read_csv(file)

    def _make_dataframe_with_timestamps(self):
        df = pd.DataFrame(columns=['time', "monday", "tuesday",
                          "wednesday", "thursday", "friday", "saturday", "sunday"])
        times = gen_time_list(self.resolution)
        df['time'] = times
        for k, v in df['time'].items():
            if '30' in v:
                for i in df:
                    if i != 'time':
                        # df[i].iloc[k] = self.input_profile_data[[df[‘Name’]==i]].index.values
                        print(v[:2])
                        print(
                            self.input_profile_data[self.input_profile_data == v[:2]])

        return df

    def _populate_missing_data_points(self, resolution):
        # We consider that the time range value is the value at the half point of the range
        # if 00:00 - 01:00 -> 0 then 00:30 -> 0
        # if 01:00 - 02:00 -> 5 then 00:30 -> 5
        # we linear interpolate each missing values

        pass

    def get_profile_timestamp_value(self, timestamp):
        return self.input_profile_data


def main():
    t = Profile(30, './samples/cs_profile_pop_standard_v2.csv')
    # print(t.data)
    # print(t._make_dataframe_with_timestamps())
    t._make_dataframe_with_timestamps()


if __name__ == '__main__':
    main()
