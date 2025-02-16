import heapq
import random
from collections import defaultdict

class Graph:
    def __init__(self):
        self.edges = defaultdict(dict)
        self.nodes = set()

    def add_edge(self, from_node, to_node, cost):
        self.edges[from_node][to_node] = cost
        self.nodes.add(from_node)
        self.nodes.add(to_node)

    def get_cost(self, from_node, to_node):
        return self.edges[from_node].get(to_node, float('inf'))

    def get_neighbors(self, node):
        return self.edges[node].keys()

    def update_edge_cost(self, from_node, to_node, new_cost):
        if to_node in self.edges[from_node]:
            self.edges[from_node][to_node] = new_cost
            print(f"Edge cost updated: {from_node} -> {to_node} = {new_cost}")


class AStar:
    def __init__(self, graph, start, goal, heuristic):
        self.graph = graph
        self.start = start
        self.goal = goal
        self.heuristic = heuristic
        self.reset()

    def reset(self):
        self.open_set = [(0, self.start)]  # Priority queue (f-score, node)
        self.came_from = {}
        self.g_score = {node: float('inf') for node in self.graph.nodes}
        self.g_score[self.start] = 0
        self.f_score = {node: float('inf') for node in self.graph.nodes}
        self.f_score[self.start] = self.heuristic(self.start, self.goal)

    def reconstruct_path(self, current):
        path = []
        while current in self.came_from:
            path.append(current)
            current = self.came_from[current]
        path.append(self.start)
        path.reverse()
        return path

    def search(self):
        while self.open_set:
            _, current = heapq.heappop(self.open_set)

            if current == self.goal:
                return self.reconstruct_path(current)

            for neighbor in self.graph.get_neighbors(current):
                tentative_g_score = self.g_score[current] + self.graph.get_cost(current, neighbor)

                if tentative_g_score < self.g_score[neighbor]:
                    self.came_from[neighbor] = current
                    self.g_score[neighbor] = tentative_g_score
                    f_score = tentative_g_score + self.heuristic(neighbor, self.goal)
                    heapq.heappush(self.open_set, (f_score, neighbor))

        return None

    def update_costs(self):
        """Randomly updates edge costs during execution."""
        for from_node in self.graph.edges:
            for to_node in self.graph.edges[from_node]:
                if random.random() < 0.3:  # 30% chance to update edge cost
                    new_cost = random.randint(1, 10)
                    self.graph.update_edge_cost(from_node, to_node, new_cost)


# Heuristic function (Manhattan distance)
def heuristic(node, goal):
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])


graph = Graph()
graph.add_edge((0, 0), (0, 1), 1)
graph.add_edge((0, 1), (1, 1), 1)
graph.add_edge((1, 1), (1, 0), 1)
graph.add_edge((1, 0), (0, 0), 1)

start = (0, 0)
goal = (1, 1)
astar = AStar(graph, start, goal, heuristic)

iteration = 0
max_iterations = 10

while iteration < max_iterations:
    path = astar.search()
    if path:
        print(f"Iteration {iteration + 1}: Optimal path: {path}")
    else:
        print(f"Iteration {iteration + 1}: No path found")

    astar.update_costs()
    astar.reset()
    iteration += 1
