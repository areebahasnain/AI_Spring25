import random
import math

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def total_distance(route):
    return sum(distance(route[i], route[i + 1]) for i in range(len(route) - 1))


def hill_climb(locations, max_iterations=1000):
    current_route = locations[:]
    random.shuffle(current_route)
    current_distance = total_distance(current_route)

    for _ in range(max_iterations):
        new_route = current_route[:]
        i, j = random.sample(range(len(locations)), 2)
        new_route[i], new_route[j] = new_route[j], new_route[i]  # Swap two locations
        new_distance = total_distance(new_route)

        if new_distance < current_distance:
            current_route, current_distance = new_route, new_distance

    return current_route, current_distance


locations = [(0, 0), (2, 3), (5, 4), (1, 1), (6, 2)]
optimized_route, min_distance = hill_climb(locations)
print("Optimized Route:", optimized_route)
print("Total Distance:", min_distance)
