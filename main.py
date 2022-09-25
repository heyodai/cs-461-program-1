from assets import get_towns, get_roads

town_list = get_towns()
road_list = get_roads(town_list)

# get town names from user
while True:
    start = input("Start: ")
    goal = input("Goal: ")
    if (start not in town_list or goal not in town_list):
        print("Invalid town!")
        continue
    break

# find the shortest path
frontier = []
path = []
current_town = start

# while True:
    # populate frontier list
    # frontier = road_list[current_town]
    # add it to the path
    # if it's the goal, stop
    # otherwise, repeat