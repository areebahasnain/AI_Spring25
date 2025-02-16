import heapq
import math

class DeliveryPoint:
    def __init__(self, id, x, y, time_window):
        self.id = id
        self.x = x
        self.y = y
        self.time_window = time_window  # (start, end)

    def distance_to(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


def greedy_best_first_search(start, delivery_points):
    route = []
    visited = set()
    priority_queue = []

    heapq.heappush(priority_queue, (0, start))

    while priority_queue:
        _, current = heapq.heappop(priority_queue)

        if current.id not in visited:
            visited.add(current.id)
            route.append(current)

            for point in delivery_points:
                if point.id not in visited:
                    priority = point.time_window[1]  # Prioritize by deadline
                    heapq.heappush(priority_queue, (priority, point))

    return route


delivery_points = [
    DeliveryPoint(1, 2, 3, (8, 10)),
    DeliveryPoint(2, 5, 7, (9, 12)),
    DeliveryPoint(3, 1, 4, (7, 9)),
    DeliveryPoint(4, 6, 2, (10, 14))
]

start = DeliveryPoint(0, 0, 0, (0, 24))  # Depot or starting point
optimized_route = greedy_best_first_search(start, delivery_points)

print("Optimized Delivery Route:")
for point in optimized_route:
    print(f"Delivery Point {point.id} at ({point.x}, {point.y}) within time window {point.time_window}")
