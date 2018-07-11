from random import shuffle
import tsp

def swap(which, tsp):
    tmp = tsp.getPoints[which[0]]
    tsp.getPoints[which[0]] = tsp.getPoints[which[1]]
    tsp.getPoints[which[1]] = tmp


def generate(tsp, step=1):
    nums = list(range(tsp.getCount))
    shuffle(nums)
    pairs = []
    l = int(len(nums)/2)
    for i in range(step):
        pairs += [(nums[i], nums[i+l])]
    return pairs


def createnew(tsp, step=1):
    pairs = generate(tsp, step)
    for p in pairs:
        swap(p, tsp)
    return tsp
