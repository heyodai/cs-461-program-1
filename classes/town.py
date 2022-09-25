# import math
# import numpy as np

class Town:
    def __init__(self, name, lat, lon):
        """Initialize a town with a name, latitude, and longitude."""
        self.name = name
        self.latitude = lat
        self.longitude = lon

    # def distance(self, other):
    #     """Calculate the distance between this town and another town."""
    #     p1 = np.array([self.latitude, self.longitude])
    #     p2 = np.array([other.latitude, other.longitude])
    #     return np.linalg.norm(p1 - p2)

        # # Convert degrees to radians
        # lat1 = math.radians(float(self.latitude))
        # lon1 = math.radians(float(self.longitude))
        # lat2 = math.radians(float(other.latitude))
        # lon2 = math.radians(float(other.longitude))
        # # Haversine formula
        # dlon = lon2 - lon1
        # dlat = lat2 - lat1
        # a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
        # c = 2 * math.asin(math.sqrt(a))
        # # Radius of earth in kilometers is 6371
        # km = 6371 * c
        # return km