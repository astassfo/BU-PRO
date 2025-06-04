import ROOT
import numpy as np
import matplotlib.pyplot as plt

points = {}
for i in range(40):
    rng1 = np.random.default_rng()
    x = rng1.random()
    rng2 = np.random.default_rng()
    y = rng2.random()
    points[x] = y

c1 = 0
c2 = 0
for key in points.keys():
    for value in points.values():
        if key**2 + value**2 <= 1:
            plt.scatter(key, value)
            c1 += 1
        else:
            c2 += 1
area = c1/(c1 + c2)
print(area)
plt.show()
