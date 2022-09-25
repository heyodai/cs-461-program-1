from classes.town import Town
from classes.route import Route

def get_towns():
    coord_file = open("./data/coordinates.txt", "r")
    town_list = {}

    for line in coord_file.readlines():
        town = Town(*line.split())
        town_list[town.name] = town

    return town_list

def get_routes(town_list):
    adj_file = open("./data/adjacencies.txt", "r")
    route_list = []
    for line in adj_file.readlines():
        line = line.split()
        start = line[0]

        for town in line:
            if (start == town or (town not in town_list)):
                continue

            route = Route(town_list[start], town_list[town])
            route_list.append(route)