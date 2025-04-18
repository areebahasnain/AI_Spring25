graph = {
    1: [(2, 10), (4, 25), (3, 30)],
    2: [(1, 10), (3, 35), (4, 40)],
    3: [(1, 30), (2, 35), (4, 30)],
    4: [(1, 25), (2, 40), (3, 30)]
}


def tsp_dfs(graph, current, visited, start, cost, min_cost):
    if len(visited) == len(graph):
        return_cost = next((d for neighbor, d in graph[current] if neighbor == start), float('inf'))
        return min(min_cost, cost + return_cost)

    for neighbor, distance in graph[current]:
        if neighbor not in visited:
            visited.add(neighbor)
            min_cost = tsp_dfs(graph, neighbor, visited, start, cost + distance, min_cost)
            visited.remove(neighbor)

    return min_cost


def find_shortest_tsp_path(graph):
    start = 1  # Assuming we start from city 1
    return tsp_dfs(graph, start, {start}, start, 0, float('inf'))


def iterative_deepening_dfs(graph, start, goal, max_depth):
    def dls(node, depth, visited):
        if depth == 0:
            return node == goal
        if node not in visited:
            visited.add(node)
            for neighbor, _ in graph.get(node, []):
                if dls(neighbor, depth - 1, visited):
                    return True
            visited.remove(node)
        return False

    for depth in range(max_depth + 1):
        if dls(start, depth, set()):
            return True
    return False


def bidirectional_search(graph, start, goal):
    from collections import deque

    if start == goal:
        return True

    forward_queue = deque([start])
    backward_queue = deque([goal])
    forward_visited = {start}
    backward_visited = {goal}

    while forward_queue and backward_queue:
        if forward_queue:
            node = forward_queue.popleft()
            for neighbor, _ in graph.get(node, []):
                if neighbor in backward_visited:
                    return True
                if neighbor not in forward_visited:
                    forward_visited.add(neighbor)
                    forward_queue.append(neighbor)

        if backward_queue:
            node = backward_queue.popleft()
            for neighbor, _ in graph.get(node, []):
                if neighbor in forward_visited:
                    return True
                if neighbor not in backward_visited:
                    backward_visited.add(neighbor)
                    backward_queue.append(neighbor)

    return False


print("Shortest TSP Path Cost:", find_shortest_tsp_path(graph))
