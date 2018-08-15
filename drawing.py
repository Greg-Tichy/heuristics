import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
import tsp

def draw(tsp, figure,  block = False):
    a=[]
    b=[]
    for x in tsp.getPoints:
        a += [x[1]]
        b += [x[2]]
    plt.figure(figure)
    plt.axis([-0.2, 1.2, -0.2, 1.2])
    plt.plot(a, b, 'g^')
    for v in tsp.getPoints:
        plt.text(v[1]+0.01, v[2]+0.01, v[0])
    order = ''
    p = tsp.getPoints
    for i in range(tsp.getCount - 1):
        plt.plot([p[i][1], p[i+1][1]], [p[i][2], p[i+1][2]])
        order += '{}>'.format(p[i][0])
    plt.plot([p[tsp.getCount - 1][1], p[0][1]], [p[tsp.getCount - 1][2], p[0][2]])
    order += p[tsp.getCount - 1][0]
    plt.title('TSP with {} cities ({})'.format(tsp.getCount, 'circular' if tsp.Circular else 'random'))
    plt.xlabel('order {} length = {}'.format(order, tsp.PathLength))
    plt.show(block=block)
