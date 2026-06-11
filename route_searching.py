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


def build_mst():
    visited_cities = {0}
    mst_edges = []

    while len(visited_cities) < NUM_OF_CITIES:
        min_edge_cost = float("inf")
        best_edge = None

        for current_city in visited_cities:
            for next_city in range(NUM_OF_CITIES):
                if next_city not in visited_cities and distances[current_city][next_city] < min_edge_cost:
                        min_edge_cost = distances[current_city][next_city]
                        best_edge = (current_city, next_city) 

        if best_edge:
            city_a, city_b = best_edge
            visited_cities.add(city_b)
            mst_edges.append((city_a, city_b))
        else:
            return None
    return mst_edges

def walk_mst(mst_edges, start_city):
    tree = {}
    for i in range(NUM_OF_CITIES):
        tree[i] = []
    for city_a, city_b in mst_edges:
        tree[city_a].append(city_b)
        tree[city_b].append(city_a)

    tsp_path = []
    visited = set()
    stack = [start_city]

    while stack:
        current_city = stack.pop()
        
        if current_city not in visited:
            visited.add(current_city)
            tsp_path.append(current_city)
        
            for neighbor in tree[current_city]:
                if neighbor not in visited:
                    stack.append(neighbor)
                    
    return tsp_path

def mst():
    mst_edges = build_mst()
    if mst_edges is None:
        print("No valid MST found.")
        return
    
    tsp_path = walk_mst(mst_edges, 0)
    total_cost = 0.0

    for i in range(len(tsp_path) - 1):
        one_step_cost = distances[tsp_path[i]][tsp_path[i + 1]]
        if one_step_cost == float("inf"):
            print("No valid path between cities.")
            return
        total_cost += one_step_cost

    last_city = tsp_path[-1]
    if distances[last_city][0] != float("inf"):
        total_cost += distances[last_city][0]
        tsp_path.append(0)
    else:
        print("No valid return path to the starting city.")
        return 
    print("==== MST  Result ===")
    print(f"Best path: {tsp_path}")
    print(f"Total cost: {total_cost}")
    print("=====================")

def greedySearch(start_city):
    current_city = start_city
    visited = {start_city}
    tsp_path = [start_city]
    total_cost = 0.0

    while len(visited) < NUM_OF_CITIES:
        best_next_city = None
        min_cost = float("inf")

        for next_city in range(NUM_OF_CITIES):
            if next_city not in visited and distances[current_city][next_city] < min_cost:
                min_cost = distances[current_city][next_city]
                best_next_city = next_city

        if best_next_city is None:
            print("No valid path found.")
            return
        
        visited.add(best_next_city)
        tsp_path.append(best_next_city)
        total_cost += min_cost
        current_city = best_next_city

    return_cost = distances[current_city][start_city]
    if return_cost == float("inf"):
        print("No valid return path to the starting city.")
        return
    total_cost += return_cost
    tsp_path.append(start_city)

    print("==== Greedy Search Result ====")
    print(f"Best path: {tsp_path}")
    print(f"Total cost: {total_cost}")
    print("=============================")


def bidirectionalSearch(start_city, target_city):
    if start_city == target_city:
        print("Start and target cities are the same.")
        return
    
    queue_start = deque([start_city])
    queue_end = deque([target_city])

    visited_start = {start_city: [start_city]}
    visited_end = {target_city: [target_city]}

    while queue_start and queue_end:
        current_start = queue_start.popleft()
        for next_city in range(NUM_OF_CITIES):
            if distances[current_start][next_city] != float("inf") and next_city not in visited_start:
                visited_start[next_city] = visited_start[current_start] + [next_city]
                queue_start.append(next_city)
                if next_city in visited_end:
                    return visited_start[next_city] + visited_end[next_city][::-1][1:]

        current_end = queue_end.popleft()
        for next_city in range(NUM_OF_CITIES):
            if distances[current_end][next_city] != float("inf") and next_city not in visited_end:
                visited_end[next_city] = visited_end[current_end] + [next_city]
                queue_end.append(next_city)
                if next_city in visited_start:
                    return visited_start[next_city] + visited_end[next_city][::-1][1:]
    return None

def bidirectionalSearchWithCost(start_city, target_city):
    path = bidirectionalSearch(start_city, target_city)
    if path is None:
        print("No valid path found.")
        return
    total_cost = 0.0
    for i in range(len(path) - 1):
        step_cost = distances[path[i]][path[i + 1]]
        if step_cost == float("inf"):
            print("No valid path between cities.")
            return
        total_cost += step_cost

    print("====== Bidirectional Search Result =====")
    print(f"Best path: {path}")
    print(f"Total cost: {total_cost}")
    print("=====================================")

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
    print(" ")

    start_time_mst = time.time()
    mst()
    end_time_mst = time.time()

    start_time_greedy = time.time()
    greedySearch(0)
    end_time_greedy = time.time()

    print(f"MST Execution Time: {end_time_mst - start_time_mst} seconds")
    print(f"Greedy Search Execution Time: {end_time_greedy - start_time_greedy} seconds")  
    print(" ")

    start_time_bdir = time.time()
    bidirectionalSearchWithCost(0, NUM_OF_CITIES - 1)
    end_time_bdir = time.time()
    print(f"Bidirectional Search Execution Time: {end_time_bdir - start_time_bdir} seconds")
if __name__ == "__main__":
    main()