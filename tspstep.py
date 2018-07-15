import random
import tsp

def swap(which, tsp):
    tmp = tsp.getPoints[which[0]]
    tsp.getPoints[which[0]] = tsp.getPoints[which[1]]
    tsp.getPoints[which[1]] = tmp

"""
I guess, starting point is the first one, thus no need to include it in permutations.
Error handing? Obviously number of swaps cannot exceed half of the number of cities. Later on, maybe... - DONE
Not so obvious and false as a matter of fact. Shift one position to the right takes N-1 swaps
therefore: no checks, simply return steps number of swaps, swaps like (n, n) are allowed
"""
def generate(tsp, step=1):
    pairs = []
    for i in range(step):
        pairs += [(random.randint(1, tsp.getCount-1), random.randint(1, tsp.getCount-1))]
    return pairs


def createnew(tsp, step=1):
    pairs = generate(tsp, step)
    for p in pairs:
        swap(p, tsp)
    return tsp
