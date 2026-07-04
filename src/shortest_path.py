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

def shortest_paths(n: int, edges: list[tuple[int, int, int]], source: int):
    # Build adjacency list
    adj_graph = {}
    for tup in edges:
        (src, dest, weight) = tup
        print(src, dest, weight)
        node = adj_graph.get(src)
        if node is None:
            adj_graph[src] = [(dest, weight)]
        else:
            adj_graph[src].append((dest, weight))
    print(adj_graph)
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
    shortest_paths(5, edges, source)


if __name__ == '__main__':
    main()