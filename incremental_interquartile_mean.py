#!/usr/bin/python
import math
import operator

data = []
f = open('data.txt','r')
for l in f:
    data.append(int(l))
    if len(data) >= 4:
      q = len(data) / 4.0
      data.sort()
      ys = data[int(math.ceil(q))-1:int(math.floor((3*q)))+1]
      factor = q - (len(ys)/2.0 - 1)

      mean = (reduce(operator.add, ys[1:-1], 0) + (ys[0] + ys[-1]) * factor) / (2*q)
      print("%d: %.2f" % (len(data), mean))

