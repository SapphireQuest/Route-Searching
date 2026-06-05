import random

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

def main():
    defineCities()
    buildRoutes()
    print(distances)

if __name__ == "__main__":
    main()