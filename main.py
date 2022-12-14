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
latest_dead_end = None

# while (current_town.name != goal):
while True:
    # identify the frontier town closest to the goal
    frontier = town_list[current_town.name].neighbors
    closest = {
        "name": None,
        "distance": float("inf")
    }
    for town in frontier:
        if (town in path or town == latest_dead_end):
            # we've already been here
            continue

        distance = town_list[town].distance(town_list[goal])
        if (distance < closest["distance"]):
            closest["name"] = town
            closest["distance"] = distance

    if (closest["name"] is None):
        # no more frontier towns, time to backtrack
        latest_dead_end = current_town.name
        path.pop()
        current_town = town_list[path[-1]]
        continue
    else:
        # add it to the path
        path.append(closest["name"])
        current_town = town_list[closest["name"]]

    # if it's the goal, stop
    if (current_town.name == goal):
        print("Path found!")
        print(start + " -> " + " -> ".join(path))
        break
