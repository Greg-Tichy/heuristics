# Simulated Annealing implementation
import tspstep as steps
from numpy import exp
from random import random
class SimulatedAnnealing:
    """
    The ideea.
    Lat's first look at a simple hill climbing. At any given point, we look at the surrounding and choose to step to
    the point delivering better result. Say, the salesman paths is shorter. What is surrounding? In this case (permutations
    of the list of the cities) we can measure it as number of differences between two permutations. For example
    [0, 1, 2] differs from [0, 2, 1] on two places, e.g. 1 swap. Well, then we say distance between two sequences is
    number of differences divided by 2, which equals number of swaps. One swap is the step. Thus surrounding is the
    collection of points in distance of N steps.
    Here we can notice, that the climber hat not a chance to achieve a better point when is already on a local optimum. All
    possible steps deliver worse result, algorithm stops.
    To fix it moves worsening the acutal height must be allowed.
    """
    def __init__(self, tsp, Tmin, Tmax, Iterations, Rounds):
        self.tsp, self.Tmin, self.Tmax, self.Iterations, self.Rounds = tsp, Tmin, Tmax, Iterations, Rounds
    def currentTemperature(self, iteration):
        return self.Tmax * (self.Tmin / self.Tmax) ** (iteration / self.Iterations)
    def probabilityToAccept(self, current, previous, temp):
        return exp((-(previous - current))/temp)

    def innerLoop(self, tsp, rounds, temp):
        while rounds:
            oldPathLength = tsp.PathLength
            savedState = tsp.clone
            steps.createnew(tsp)
            newPathLength = tsp.PathLength
            accept = oldPathLength > newPathLength # better result?
            if not accept:
                if self.probabilityToAccept(newPathLength, oldPathLength, temp) > random():
                    accept = True

            if accept:
                currentResult = newPathLength
                if currentResult < self.globalBestResult:
                    self.globalBestResult = currentResult
                    self.globalBest = tsp.clone
                    savedState = tsp.clone
            else:
                tsp = savedState.clone
            rounds -= 1

    def runAlgorithm(self):
        self.globalBestResult = self.tsp.PathLength # init global values
        self.globalBest = self.tsp.clone
        currentTemp = self.currentTemperature(0)
        iteration = 0
        while currentTemp > self.Tmin:
            self.innerLoop(self.tsp, self.Rounds, currentTemp)
            iteration += 1
            currentTemp = self.currentTemperature(iteration)
            print("currentTemp=%d Max=%d Min=%d" % (currentTemp, self.Tmax, self.Tmin))
        print("finished")







