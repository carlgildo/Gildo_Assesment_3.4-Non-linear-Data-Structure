"""Assessment 3.4 - Binary Tree for the last name "GILDO"
Tree:
          G            level 0
        /   \
       I     L         level 1
      / \
     D   O             level 2
"""
from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_tree():
    root = Node("G")
    root.left = Node("I")
    root.right = Node("L")
    root.left.left = Node("D")
    root.left.right = Node("O")
    return root


def bfs(root):
    """Breadth-First Search: visit level by level using a queue."""
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


def dfs(node, result=None):
    """Depth-First Search (preorder): go deep first, then backtrack."""
    if result is None:
        result = []
    if node is None:
        return result
    result.append(node.value)
    dfs(node.left, result)
    dfs(node.right, result)
    return result


if __name__ == "__main__":
    root = build_tree()
    print("Binary Tree BFS:", " - ".join(bfs(root)))
    print("Binary Tree DFS:", " - ".join(dfs(root)))
