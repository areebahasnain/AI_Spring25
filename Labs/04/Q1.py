from heapq import heappush, heappop

def best_first_search_multi_goal(maze, start, goals):
    def heuristic(node, unvisited_goals):
        # minimum distance to any unvisited goal
        return min(abs(node[0] - goal[0]) + abs(node[1] - goal[1]) for goal in unvisited_goals)

    unvisited_goals = set(goals)
    priority_queue = []
    heappush(priority_queue, (heuristic(start, unvisited_goals), start, [start]))
    visited = set()

    while priority_queue:
        _, current, path = heappop(priority_queue)

        if current in unvisited_goals:
            unvisited_goals.remove(current)
            if not unvisited_goals:
                return path  # All goals visited

        if current in visited:
            continue
        visited.add(current)

        # Explore neighbors
        for neighbor in get_neighbors(maze, current):
            if neighbor not in visited:
                new_path = path + [neighbor]
                priority = heuristic(neighbor, unvisited_goals)
                heappush(priority_queue, (priority, neighbor, new_path))

    return None  # No path found

def get_neighbors(maze, node):
    # Return valid neighbors (up, down, left, right) that are not walls
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    neighbors = []
    for dx, dy in directions:
        x, y = node[0] + dx, node[1] + dy
        if 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] != '#':
            neighbors.append((x, y))
    return neighbors


# Maze with dead ends and multiple goals
maze = [
[0, 1, 0, 0, 1],
[0, 1, 0, 1, 0],
[0, 0, 0, 1, 0],
[1, 1, 0, 1, 1],
[0, 0, 0, 0, 0]
]
start = (0, 0)
goals = [(4, 4), (2, 2), (1, 4)]  # Multiple goals at different locations

# Find the path
path = best_first_search_multi_goal(maze, start, goals)

if path:
    print("Path to visit all goals:", path)
else:
    print("No path found to all goals")