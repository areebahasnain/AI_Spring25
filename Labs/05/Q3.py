import random
import math

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def total_distance(route):
    return sum(distance(route[i], route[i + 1]) for i in range(len(route) - 1))


def create_population(size, locations):
    return [random.sample(locations, len(locations)) for _ in range(size)]


def crossover(parent1, parent2):
    cut = random.randint(1, len(parent1) - 1)
    child = parent1[:cut] + [gene for gene in parent2 if gene not in parent1[:cut]]
    return child


def mutate(route, mutation_rate=0.1):
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(route)), 2)
        route[i], route[j] = route[j], route[i]
    return route


def genetic_algorithm(locations, population_size=100, generations=500, mutation_rate=0.1):
    population = create_population(population_size, locations)

    for _ in range(generations):
        population = sorted(population, key=total_distance)
        new_population = population[:10]  # Keep the best individuals

        while len(new_population) < population_size:
            parents = random.sample(population[:50], 2)
            child = crossover(parents[0], parents[1])
            child = mutate(child, mutation_rate)
            new_population.append(child)

        population = new_population

    best_route = min(population, key=total_distance)
    return best_route, total_distance(best_route)


locations = [(random.randint(0, 100), random.randint(0, 100)) for _ in range(10)]
optimized_route, min_distance = genetic_algorithm(locations)
print("Optimized Route:", optimized_route)
print("Total Distance:", min_distance)
