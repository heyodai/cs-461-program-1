from assets import get_towns, get_routes

town_list = get_towns()
route_list = get_routes(town_list)

start = input("Enter your starting town: ")
goal = input("Enter your destination: ")
