#!/usr/bin/python3
import math
import operator
from functools import reduce
from typing import Iterable


def interquartile_mean(values: Iterable) -> None:
    """
    A function to calculate the Interquartile Means and output to
    standard out.
    :param values: An iterable of items to cast to integers
    :rtype: None
    :return: None
    """
    data = []
    for value in values:
        data.append(int(value))
        if len(data) >= 4:
            q = len(data) / 4.0
            data.sort()
            ys = data[int(math.ceil(q)) - 1:int(math.floor((3 * q))) + 1]
            factor = q - (len(ys) / 2.0 - 1)

            mean = (reduce(operator.add, ys[1:-1], 0)
                    + (ys[0] + ys[-1]) * factor) / (2 * q)
            print("%d: %.2f" % (len(data), mean))


if __name__ == '__main__':
    file = open('data.txt', 'r')
    interquartile_mean(file)
