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
    # populate frontier list
    frontier = town_list[current_town.name].neighbors
    print(frontier)
    break
    # add it to the path
    # if it's the goal, stop
    # if it's a dead end, backtrack
    # otherwise, keep searching