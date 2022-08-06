#!/usr/bin/python
import math
import random

f = open("data.txt","w")
for i in range(100000):
    v = math.sin(i * math.pi/80000) * 300 + random.randint(0, 40) + 280
    v = max(v, 0)
    v = int(min(v, 600))
    f.write("{}\n".format(v))
