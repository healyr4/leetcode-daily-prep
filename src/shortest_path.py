# You are given a directed weighted graph with n nodes numbered 0 to n - 1.
#
# Each edge is represented as:
# (from_node, to_node, weight)
# Return the shortest distance from source to every node.
# Return -1 for any unreachable node.

# Example:
#
# n = 5
#
# edges = [
#     (0, 1, 4),
#     (0, 2, 1),
#     (2, 1, 2),
#     (1, 3, 1),
#     (2, 3, 5),
# ]
#
# source = 0

# Expected output:
#
# [0, 3, 1, 4, -1]

# Assumptions:
#
# All edge weights are non-negative.
# The graph is directed.
# Multiple edges between the same nodes may exist.
# Some nodes may be unreachable.
from math import inf
import heapq

def shortest_paths(n: int, edges: list[tuple[int, int, int]], source: int):
    # Build adjacency list
    # adj_graph = {
    #     node: []
    #     for node in range(0, n)
    # }
    # for point in edges:
    #     (src, dest, weight) = point
    #     adj_graph[src].append((dest,weight))
    # print(adj_graph)

    adj_graph: list[list[tuple[int, int]]] = [
        [] for _ in range(n)
    ]

    for src, dest, weight in edges:
        adj_graph[src].append((dest, weight))
    print(adj_graph)

    # Want to set up shortest distances discovered so far
    # from source to each node
    distances = [inf] * n
    print(distances)
    distances[source] = 0

    # Min heap stores (distance from the source, node)
    # BEgin at source with distance of 0
    min_heap = [(0,source)]
    print("min heap: {}".format(min_heap))

    # repeatedly process cheapest route we have discovered so far
    while min_heap:
        # Pop the smallest item from the heap
        curr_distance, curr_node = heapq.heappop(min_heap)
        if curr_distance > distances[curr_node]:
            continue

        # explore every outgoing edge
        for neighbour, edge_weight in adj_graph[curr_node]:
            new_distance = curr_distance + edge_weight

            # Relax edge. Update neighbour if this rute is cheaper
            if new_distance < distances[neighbour]:
                distances[neighbour] = new_distance

                heapq.heappush(min_heap, (new_distance, neighbour))

    return [ -1 if distance == inf else distance for distance in distances]



def main():


    n = 5

    edges = [
        (0, 1, 4),
        (0, 2, 1),
        (2, 1, 2),
        (1, 3, 1),
        (2, 3, 5),
    ]

    source = 0
    res = shortest_paths(5, edges, source)
    print(res)


if __name__ == '__main__':
    main()