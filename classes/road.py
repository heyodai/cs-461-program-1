import numpy as np

class Road:
    def __init__(self, start, end):
        """Initialize a road with a start and end town."""
        self.start = start
        self.end = end

    def distance(self, other):
        """Calculate the distance between this town and another town."""
        p1 = np.array([self.latitude, self.longitude])
        p2 = np.array([other.latitude, other.longitude])
        return np.linalg.norm(p1 - p2)
