# Simulated Annealing implementation

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
    def __init__(self, Tmin, Tmax, Iterations):
        self.Tmin, self.Tmax, self.Iteratins = Tmin, Tmax, Iterations
    def temperature(self, iteration):
        return self.Tmin * (self.Tmax / self.Tmin) ** (iteration / self.Iteratins)

