import sys
import tsp
import drawing
import tspstep as step

print('running on {}'.format(sys.platform))
# import numpy as np
#
# incomes = np.random.normal(27000, 15000, 10000)
# print(len(incomes))
# #incomes = np.append(incomes, [10000000000])
# print (np.mean(incomes))
# print (np.median(incomes))
# print(len(incomes))
# from scipy import stats
# import matplotlib.pyplot as plt
# plt.hist(incomes, 50)
# plt.show()

t = tsp.TSP(15, True)

# drawing.draw(t)

t0 = t.getPoints

t1 = step.createnew(t, 3)

drawing.draw(t1)

print(t.getPoints == t1.getPoints)
print(t0==t1)

# t = tsp.TSP(0)
# print(t.getPoints)
# print('point 1 [1] {} 1 [2] {} '.format(t.getPoints[1][1], t.getPoints[1][2]))
# print(t.distance(t.getPoints[0], t.getPoints[1]))
# print('total length (3) {}'.format(t.getPathLength))
# t = tsp.TSP(500, True)
# print('total length (500) {}'.format(t.getPathLength))


