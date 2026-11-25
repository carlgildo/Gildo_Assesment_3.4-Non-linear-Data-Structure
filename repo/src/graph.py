"""Assessment 3.4 - Graph for the last name "GILDO"
Edges: G-I, G-L, I-D, L-O, D-O
        G           level 0
       / \
      I   L         level 1
      |   |
      D---O         level 2
"""
from collections import deque

graph = {
    "G": ["I", "L"],
    "I": ["G", "D"],
    "L": ["G", "O"],
    "D": ["I", "O"],
    "O": ["L", "D"],
}


def bfs(graph, start):
    """Breadth-First Search: visit nearest vertices first using a queue."""
    visited = {start}
    queue = deque([start])
    result = []
    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return result


def dfs(graph, vertex, visited=None, result=None):
    """Depth-First Search: follow one path as far as possible, then backtrack."""
    if visited is None:
        visited, result = set(), []
    visited.add(vertex)
    result.append(vertex)
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, result)
    return result


if __name__ == "__main__":
    print("Graph BFS:", " - ".join(bfs(graph, "G")))
    print("Graph DFS:", " - ".join(dfs(graph, "G")))
