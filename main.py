from town import populate
town_list = populate()

# get town names from user
while True:
    start = input("Start: ")
    goal = input("Goal: ")
    if (start not in town_list or goal not in town_list):
        print("Invalid town name!")
        continue
    if (start == goal):
        print("Start and goal must be different!")
        continue
    break

# find the shortest path
path = []
current_town = town_list[start]

# while (current_town.name != goal):
while True:
    # identify the frontier town closest to the goal
    frontier = town_list[current_town.name].neighbors
    closest = {
        "name": None,
        "distance": float("inf")
    }
    for town in frontier:
        distance = town_list[town].distance(town_list[goal])
        if (distance < closest["distance"]):
            closest["name"] = town
            closest["distance"] = distance

    # add it to the path
    path.append(closest["name"])
    current_town = town_list[closest["name"]]

    # if it's the goal, stop
    if (current_town.name == goal):
        print("Path found!")
        break

    # if it's a dead end, backtrack
    # otherwise, keep searching

    print("Not found yet!")
    break