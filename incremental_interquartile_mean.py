#!/usr/bin/python3
import math
from typing import Iterable
from bisect import insort


def interquartile_mean(iterable: Iterable) -> None:
    """
    A function to calculate the Interquartile Mean and print to
    standard out.
    :param iterable: An iterable of items to cast to integers
    :rtype: None
    :return: None
    """
    data = []
    for number in iterable:
        insort(data, int(number))
        if len(data) >= 4:
            quarter_data_length = len(data) / 4.0
            interquartile_range = data[
                int(math.ceil(quarter_data_length)) - 1:
                int(math.floor((3 * quarter_data_length))) + 1
            ]
            factor = quarter_data_length - (len(interquartile_range) / 2.0 - 1)
            sum_interquartile_range = sum(interquartile_range[1:-1]) + (
                (interquartile_range[0] + interquartile_range[-1])
                * factor
            )
            mean = sum_interquartile_range / (2 * quarter_data_length)
            print("%d: %.2f" % (len(data), mean))


if __name__ == '__main__':
    file = open('data.txt', 'r')
    interquartile_mean(file)
