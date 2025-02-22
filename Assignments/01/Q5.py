from queue import PriorityQueue, Queue

# Graph representation of Romania map with cities as nodes and distances as edge weights
graph = {
    'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova': {'Drobeta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
    'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
    'Giurgiu': {'Bucharest': 90},
    'Urziceni': {'Bucharest': 85, 'Vaslui': 142, 'Hirsova': 98},
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Eforie': {'Hirsova': 86},
    'Vaslui': {'Urziceni': 142, 'Iasi': 92},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Neamt': {'Iasi': 87}
}

# Heuristic values (straight-line distance to Bucharest)
heuristic = {
    'Arad': 366, 'Bucharest': 0, 'Craiova': 160, 'Drobeta': 242, 'Eforie': 161,
    'Fagaras': 176, 'Giurgiu': 77, 'Hirsova': 151, 'Iasi': 226, 'Lugoj': 244,
    'Mehadia': 241, 'Neamt': 234, 'Oradea': 380, 'Pitesti': 100, 'Rimnicu Vilcea': 193,
    'Sibiu': 253, 'Timisoara': 329, 'Urziceni': 80, 'Vaslui': 199, 'Zerind': 374
}


# ------------------------- SEARCH ALGORITHMS IMPLEMENTATION -------------------------

# BFS (Breadth-First Search) - Uninformed Search
def bfs(start, goal):
    queue = Queue()
    queue.put((start, [start], 0))  # (Current Node, Path Taken, Path Cost)

    while not queue.empty():
        node, path, cost = queue.get()

        if node == goal:
            return path, cost  # Return path and cost if goal is found

        for neighbor, weight in graph[node].items():
            if neighbor not in path:  # Avoid revisiting nodes
                queue.put((neighbor, path + [neighbor], cost + weight))

    return None  # Return None if no path found


# UCS (Uniform Cost Search) - Uninformed Search (Guaranteed Optimal)
def ucs(start, goal):
    pq = PriorityQueue()
    pq.put((0, start, [start]))  # (Cost, Current Node, Path Taken)
    visited = {}

    while not pq.empty():
        cost, node, path = pq.get()

        if node == goal:
            return path, cost  # Return optimal path and cost

        if node not in visited or cost < visited[node]:  # Only explore better paths
            visited[node] = cost
            for neighbor, weight in graph[node].items():
                pq.put((cost + weight, neighbor, path + [neighbor]))

    return None


# GBFS (Greedy Best-First Search) - Informed Search (Not Guaranteed Optimal)
def gbfs(start, goal):
    pq = PriorityQueue()
    pq.put((heuristic[start], start, [start], 0))  # (Heuristic, Current Node, Path, Cost)
    visited = set()

    while not pq.empty():
        _, node, path, cost = pq.get()

        if node == goal:
            return path, cost  # Return path and cost

        if node not in visited:
            visited.add(node)
            for neighbor, weight in graph[node].items():
                if neighbor not in visited:
                    pq.put((heuristic[neighbor], neighbor, path + [neighbor], cost + weight))

    return None


# DLS (Depth-Limited Search) - Helper for IDDFS
def dls(node, goal, depth, path, cost):
    if depth == 0 and node == goal:
        return path, cost  # Return if goal is reached at depth limit
    if depth > 0:
        for neighbor, weight in graph[node].items():
            if neighbor not in path:  # Avoid cycles
                result = dls(neighbor, goal, depth - 1, path + [neighbor], cost + weight)
                if result:
                    return result
    return None


# IDDFS (Iterative Deepening Depth-First Search) - Uninformed Search
def iddfs(start, goal, max_depth=20):
    for depth in range(max_depth):
        result = dls(start, goal, depth, [start], 0)  # Calls DLS with increasing depth
        if result:
            return result
    return None


# ------------------------- INPUT & EXECUTION -------------------------

# Get user input for start and goal cities
start = input("Enter start city: ")
goal = input("Enter goal city: ")

results = []

# Run all search algorithms and store results
bfs_result = bfs(start, goal)
if bfs_result:
    results.append(("BFS", bfs_result[0], bfs_result[1]))

ucs_result = ucs(start, goal)
if ucs_result:
    results.append(("UCS", ucs_result[0], ucs_result[1]))

gbfs_result = gbfs(start, goal)
if gbfs_result:
    results.append(("GBFS", gbfs_result[0], gbfs_result[1]))

iddfs_result = iddfs(start, goal)
if iddfs_result:
    results.append(("IDDFS", iddfs_result[0], iddfs_result[1]))

# Sort results based on path cost (ascending order)
if results:
    results.sort(key=lambda x: x[2])
    print("\nComparison of Search Algorithms (Sorted by Cost):")
    for algo, path, cost in results:
        print(f"{algo}: Path = {' -> '.join(path)}, Cost = {cost}")
else:
    print("\n❌ No valid path found for any algorithm!")

