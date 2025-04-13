import random

# Production Tasks and Times (in hours):
tasks = {
    1: {"time": 5},
    2: {"time": 8},
    3: {"time": 4},
    4: {"time": 7},
    5: {"time": 6},
    6: {"time": 3},
    7: {"time": 9}
}

# Production Facilities and Their Capacities (in hours per day):
facilities = {
    1: {"capacity": 24},
    2: {"capacity": 30},
    3: {"capacity": 28}
}

# Cost Matrix (cost per hour for each task at each facility):
cost_matrix = {
    1: {1: 10, 2: 12, 3: 9},
    2: {1: 15, 2: 14, 3: 16},
    3: {1: 8, 2: 9, 3: 7},
    4: {1: 12, 2: 10, 3: 13},
    5: {1: 14, 2: 13, 3: 12},
    6: {1: 9, 2: 8, 3: 10},
    7: {1: 11, 2: 12, 3: 13}
}

# Genetic Algorithm parameters
POPULATION_SIZE = 6
CROSSOVER_RATE = 0.8
MUTATION_RATE = 0.2
MAX_GENERATIONS = 50


class Individual:
    def __init__(self, chromosome=None):
        # Each chromosome is a list of facility assignments for each task
        # For example [1, 3, 2, 1, 3, 2, 1] means:
        # Task 1 -> Facility 1, Task 2 -> Facility 3, etc.
        if chromosome is None:
            self.chromosome = [random.randint(1, 3) for _ in range(len(tasks))]
        else:
            self.chromosome = chromosome
        self.fitness = self.calculate_fitness()

    def calculate_fitness(self):
        # calculate total cost
        total_cost = 0
        facility_time_used = {1: 0, 2: 0, 3: 0}

        for task_id, facility_id in enumerate(self.chromosome, 1):
            # Add cost for this task-facility assignment
            total_cost += cost_matrix[task_id][facility_id] * tasks[task_id]["time"]

            # track time used at each facility
            facility_time_used[facility_id] += tasks[task_id]["time"]

        # check capacity constraints and penalize if violated
        penalty = 0
        for facility_id, time_used in facility_time_used.items():
            if time_used > facilities[facility_id]["capacity"]:
                # Penalize proportionally to how much the capacity is exceeded
                penalty += (time_used - facilities[facility_id]["capacity"]) * 100

        # lower the cost and penalty, the higher the fitness
        return 1 / (total_cost + penalty + 1)  # adding 1 to avoid division by zero

    def __str__(self):
        return f"Chromosome: {self.chromosome}, Fitness: {self.fitness}"

    def get_solution_details(self):
        total_cost = 0
        facility_time_used = {1: 0, 2: 0, 3: 0}
        task_assignments = {1: [], 2: [], 3: []}

        for task_id, facility_id in enumerate(self.chromosome, 1):
            task_time = tasks[task_id]["time"]
            task_cost = cost_matrix[task_id][facility_id] * task_time

            total_cost += task_cost
            facility_time_used[facility_id] += task_time
            task_assignments[facility_id].append(task_id)

        return {
            "assignments": self.chromosome,
            "task_assignments": task_assignments,
            "facility_time_used": facility_time_used,
            "total_cost": total_cost,
            "feasible": all(facility_time_used[f] <= facilities[f]["capacity"] for f in facilities)
        }


def initialize_population():
    return [Individual() for _ in range(POPULATION_SIZE)]


def roulette_wheel_selection(population):
    total_fitness = sum(individual.fitness for individual in population)

    # generate a random value between 0 and total_fitness
    r = random.uniform(0, total_fitness)

    # find the individual that corresponds to this value
    current_sum = 0
    for individual in population:
        current_sum += individual.fitness
        if current_sum > r:
            return individual

    return population[-1]


def one_point_crossover(parent1, parent2):
    if random.random() > CROSSOVER_RATE:
        return parent1, parent2

    # choose crossover point
    crossover_point = random.randint(1, len(tasks) - 1)

    # create offspring
    child1_chromosome = parent1.chromosome[:crossover_point] + parent2.chromosome[crossover_point:]
    child2_chromosome = parent2.chromosome[:crossover_point] + parent1.chromosome[crossover_point:]

    return Individual(child1_chromosome), Individual(child2_chromosome)


def swap_mutation(individual):
    if random.random() > MUTATION_RATE:
        return individual

    # choose two random positions and swap their values
    pos1, pos2 = random.sample(range(len(tasks)), 2)
    new_chromosome = individual.chromosome.copy()
    new_chromosome[pos1] = individual.chromosome[pos2]
    new_chromosome[pos2] = individual.chromosome[pos1]

    return Individual(new_chromosome)


def genetic_algorithm():
    # Initialize population
    population = initialize_population()

    best_individual = max(population, key=lambda ind: ind.fitness)

    for generation in range(MAX_GENERATIONS):
        new_population = []
        new_population.append(best_individual)

        while len(new_population) < POPULATION_SIZE:
            # Selection
            parent1 = roulette_wheel_selection(population)
            parent2 = roulette_wheel_selection(population)

            # Crossover
            child1, child2 = one_point_crossover(parent1, parent2)

            # Mutation
            child1 = swap_mutation(child1)
            child2 = swap_mutation(child2)

            # Add to new population
            new_population.append(child1)
            if len(new_population) < POPULATION_SIZE:
                new_population.append(child2)

        # update population
        population = new_population

        # update best individual
        current_best = max(population, key=lambda ind: ind.fitness)
        if current_best.fitness > best_individual.fitness:
            best_individual = current_best

        if generation > 20 and len(set(tuple(ind.chromosome) for ind in population)) <= 2:
            print(f"Converged after {generation} generations")
            break

    return best_individual


best_solution = genetic_algorithm()

print("Best Solution Found:")
solution_details = best_solution.get_solution_details()
print(f"Task to Facility Assignments: {solution_details['assignments']}")
print(f"Facility 1 Tasks: {solution_details['task_assignments'][1]}")
print(f"Facility 2 Tasks: {solution_details['task_assignments'][2]}")
print(f"Facility 3 Tasks: {solution_details['task_assignments'][3]}")
print(f"Facility 1 Time Used: {solution_details['facility_time_used'][1]} / {facilities[1]['capacity']}")
print(f"Facility 2 Time Used: {solution_details['facility_time_used'][2]} / {facilities[2]['capacity']}")
print(f"Facility 3 Time Used: {solution_details['facility_time_used'][3]} / {facilities[3]['capacity']}")
print(f"Total Cost: {solution_details['total_cost']}")
print(f"Solution is {'feasible' if solution_details['feasible'] else 'infeasible'}")