import random
from collections import deque
import time

NUM_OF_CITIES = 10
map_of_cities = []
distances = [[float("inf") for i in range(NUM_OF_CITIES)] for j in range(NUM_OF_CITIES)]
class City:
    def __init__(self, city_id, x, y):
        self.id = city_id
        self.x = x
        self.y = y

def defineCities():
    for i in range(NUM_OF_CITIES):
        x = random.randint(-100, 100)
        y = random.randint(-100, 100)
        new_city = City(i, x, y)
        map_of_cities.append(new_city)

def buildRoutes():
    for i in range(NUM_OF_CITIES):
        for j in range(i + 1, NUM_OF_CITIES):
            decision = random.randint(0, 100)
            if decision > 80:
                continue 
            distance = ((map_of_cities[i].x - map_of_cities[j].x) ** 2 + (map_of_cities[i].y - map_of_cities[j].y) ** 2) ** 0.5
            distances[i][j] = distance
            distances[j][i] = distance
        
    for i in range(NUM_OF_CITIES):
        distances[i][i] = 0


def bfs(start_city):
    queue = deque()
    
    initial_state = (start_city, [start_city], 0.0)
    queue.append(initial_state)

    best_path = []
    min_cost = float("inf")

    while queue:
        current_city, path, cost = queue.popleft()

        if len(path) == NUM_OF_CITIES:
            return_cost = distances[current_city][start_city]
            if return_cost != float("inf"):
                cost += return_cost
                if cost < min_cost:
                    min_cost = cost
                    best_path = path + [start_city]
            continue
        for next_city in range(NUM_OF_CITIES):
            if next_city not in path and distances[current_city][next_city] != float("inf"):
                new_cost = cost + distances[current_city][next_city]
                new_path = path + [next_city]
                queue.append((next_city, new_path, new_cost))

    print("=== BFS Search Result ===")
    if min_cost == float("inf"):
        print("No valid path found.")
    else:
        print(f"Best path: {best_path}")
        print(f"Minimum cost: {min_cost}")
    print("=========================")
    print(" ")

def dfs(start_city):
    stack = []

    initial_state = (start_city, [start_city], 0.0)
    stack.append(initial_state)

    best_path = []
    min_cost = float("inf")

    while stack:
        current_city, path, cost = stack.pop()

        if len(path) == NUM_OF_CITIES:
            return_cost = distances[current_city][start_city]
            if return_cost != float("inf"):
                cost += return_cost
                if cost < min_cost:
                    min_cost = cost
                    best_path = path + [start_city]
            continue
    
        for next_city in range(NUM_OF_CITIES):
            if next_city not in path and distances[current_city][next_city] != float("inf"):
                new_cost = cost + distances[current_city][next_city]
                new_path = path + [next_city]
                stack.append((next_city, new_path, new_cost))

    print("=== DFS Search Result ===")
    if min_cost == float("inf"):
        print("No valid path found.")
    else:
        print(f"Best path: {best_path}")
        print(f"Minimum cost: {min_cost}")
    print("=========================")
    print(" ")


def mst():
    visited_cities = {0}


def main():
    defineCities()
    buildRoutes()
    print("=== Map of Cities ===")
    for i, city in enumerate(map_of_cities):
        print(f"City {city.id}: ({city.x}, {city.y})")
   
    start_time_bfs = time.time()
    bfs(0)
    end_time_bfs = time.time()
    start_time_dfs = time.time()
    dfs(0)
    end_time_dfs = time.time()

    print(f"BFS Execution Time: {end_time_bfs - start_time_bfs} seconds")
    print(f"DFS Execution Time: {end_time_dfs - start_time_dfs} seconds")




if __name__ == "__main__":
    main()