import random
import math
import copy

class TSP:
    def __init__(self, howmany: int, onCircle = False) -> object:
        """
        when all cities are located on a circle, there's an obvious and trivial solution. Therefore it's a good way to
        see how heuristic algorithms find a solution. If at all...
        Layout: we want all of them in a unit square, when layout is circular, the circle has center at (0.5, 0.5) and
        radius 0.5
        Distance is euclidean, see below.
        :type howmany: object
        """
        self.__count = howmany
        # print('OnCircle', onCircle)
        self.__circular = onCircle
        if self.__count > 0:
            self.__points = []
            if onCircle:        # center on (0.5, 0.5) with radius 0.5
                angle = 6.28 / howmany      # tells me math.PI is unknown aargh!!!!
                for x in range(howmany):
                    self.__points.append((str(x), math.sin(x * angle)/2 + 0.5, math.cos(x * angle)/2 + 0.5))
                    # print('angle {} result {}'.format(x * angle, self.__points[len(self.__points)-1]))
            else:               # just a bunch of random point inside of unit square,
               for x in range(self.__count):
                    self.__points.append((str(x), random.random(), random.random()))

    def distance(self, x, y):
        if x == y:
            return 0
        else:
            return math.sqrt((x[1] - y[1]) ** 2 + (x[2] - y[2]) ** 2)
    @property
    def getCount(self):
        return self.__count
    @property
    def getPoints(self):
        if (self.__count > 0):
            return self.__points
    @property
    def PathLength(self):
        if self.__count < 2:
            return 0
        totalLength = 0
        for i in range(self.__count):
            totalLength += self.distance(self.__points[i], self.__points[(i+1) % self.__count])
        return totalLength
    @property
    def Circular(self):
        return self.__circular
    @property
    def clone(self):
        t = TSP(0, self.__circular)
        t.__count = self.__count
        t.__points = copy.deepcopy(self.__points)
        return t

