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


print("Shortest TSP Path Cost:", find_shortest_tsp_path(graph))
