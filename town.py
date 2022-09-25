import numpy as np

class Town:
    def __init__(self, name, lat, lon):
        """Initialize a town with a name, latitude, longitude, and neighbors."""
        self.name = name
        self.latitude = lat
        self.longitude = lon
        self.neighbors = set() #{}

    def distance(self, other):
        """Calculate the distance between this town and another town."""
        p1 = np.array([self.latitude, self.longitude])
        p2 = np.array([other.latitude, other.longitude])
        return np.linalg.norm(p1 - p2)

def populate():
    town_list = {}

    # read in town names and coordinates
    coord_file = open("./data/coordinates.txt", "r")
    for line in coord_file.readlines():
        town = Town(*line.split())
        town_list[town.name] = town

    # read in town adjacencies
    adj_file = open("./data/adjacencies.txt", "r")
    for line in adj_file.readlines():
        line = line.split()
        start = line[0]
        neighbor_list = []

        for town in line:
            if (start == town or (town not in town_list)):
                continue
            neighbor_list.append(town)

            # add this town to the neighbor's list
            for neighbor in neighbor_list:
                if (neighbor not in town_list[start].neighbors):
                    town_list[neighbor].neighbors.add(start)

        # town_list[start].neighbors.add(neighbor_list)
        for item in neighbor_list:
            town_list[start].neighbors.add(item)

    return town_list