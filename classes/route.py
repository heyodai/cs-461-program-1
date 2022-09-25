import numpy as np

class Route:
    def __init__(self, start, end):
        """Initialize a route with a start and end town."""
        self.start = start
        self.end = end
        # self.distance = start.distance(end)
        # self.start.add_adjacent(self.end)
        # self.end.add_adjacent(self.start)

    def distance(self, other):
        """Calculate the distance between this town and another town."""
        p1 = np.array([self.latitude, self.longitude])
        p2 = np.array([other.latitude, other.longitude])
        return np.linalg.norm(p1 - p2)

    # def __str__(self):
    #     return f"{self.start.name} to {self.end.name} = {self.distance}"
