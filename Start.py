import sys
import tsp
import drawing
import tspstep as step
import sa
import tspstep as steps


print('running on {}'.format(sys.platform))

t = tsp.TSP(8, True)
steps.createnew(t)
d = t.clone

drawing.draw(d, 1, False)

SA = sa.SimulatedAnnealing(t, 50, 1500, 50, 50)

SA.runAlgorithm()

drawing.draw(SA.globalBest, 2, True)

