# DFS as a Goal-Based Agent
class DFSGoalBasedAgent:
    def __init__(self, graph, start, goal):
        self.graph = graph
        self.start = start
        self.goal = goal
        self.visited = set()
        self.stack = [start]  # Stack for DFS (LIFO order)

    def is_goal(self, node):
        return node == self.goal

    def act(self):
        while self.stack:
            current_node = self.stack.pop()
            if self.is_goal(current_node):
                return f"Goal found: {current_node}"
            if current_node not in self.visited:
                self.visited.add(current_node)
                for neighbor in self.graph.get(current_node, []):
                    if neighbor not in self.visited:
                        self.visited.add(neighbor)  # Mark before pushing
                        self.stack.append(neighbor)
        return "Goal not found"

# DLS as a Goal-Based Agent
class DLSGoalBasedAgent:
    def __init__(self, graph, start, goal, depth_limit):
        self.graph = graph
        self.start = start
        self.goal = goal
        self.depth_limit = depth_limit
        self.visited = set()
        self.stack = [(start, 0)]  # (node, depth)

    def is_goal(self, node):
        return node == self.goal

    def act(self):
        while self.stack:
            current_node, depth = self.stack.pop()
            if self.is_goal(current_node):
                return f"Goal found: {current_node}"
            if depth < self.depth_limit and current_node not in self.visited:
                self.visited.add(current_node)
                for neighbor in self.graph.get(current_node, []):
                    if neighbor not in self.visited:
                        self.stack.append((neighbor, depth + 1))
        return "Goal not found within depth limit"

# UCS as a Utility-Based Agent
import heapq

class UCSUtilityBasedAgent:
    def __init__(self, graph, start, goal):
        self.graph = graph
        self.start = start
        self.goal = goal
        self.visited = set()
        self.priority_queue = [(0, start)]  # (cumulative_cost, node)

    def is_goal(self, node):
        return node == self.goal

    def act(self):
        while self.priority_queue:
            cumulative_cost, current_node = heapq.heappop(self.priority_queue)
            if self.is_goal(current_node):
                return f"Goal found: {current_node} with cost {cumulative_cost}"
            if current_node not in self.visited:
                self.visited.add(current_node)
                for neighbor, edge_cost in self.graph.get(current_node, {}).items():
                    if neighbor not in self.visited:
                        heapq.heappush(self.priority_queue, (cumulative_cost + edge_cost, neighbor))
        return "Goal not found"
