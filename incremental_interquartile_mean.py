#!/usr/bin/python3
import math
from bisect import insort


class InterquartileMeanCalculator:
    def __init__(self):
        self._data = []

    @property
    def data(self) -> list:
        return self._data

    def add_to_data(self, number: str) -> None:
        insort(self.data, int(number))

    def interquartile_mean(self) -> float:
        if len(self.data) >= 4:
            quarter_data_length = len(self.data) / 4.0
            interquartile_range = self.data[
                int(math.ceil(quarter_data_length)) - 1:
                int(math.floor((3 * quarter_data_length))) + 1
            ]
            factor = quarter_data_length - (len(interquartile_range) / 2.0 - 1)
            sum_interquartile_range = sum(interquartile_range[1:-1]) + (
                (interquartile_range[0] + interquartile_range[-1])
                * factor
            )
            mean = sum_interquartile_range / (2 * quarter_data_length)
            return mean


if __name__ == '__main__':
    calculator = InterquartileMeanCalculator()
    file = open('data.txt', 'r')
    for line in file:
        calculator.add_to_data(line)
        if len(calculator.data) > 3:
            print("%d: %.2f" % (
                len(calculator.data),
                calculator.interquartile_mean()
            ))
