r"""Assessment 3.6 - DFS Methods in Binary Tree (Preorder, Inorder, Postorder)

Builds a binary tree from the letters of your FIRST NAME + LAST NAME
(Assessment 3.5), filling it level by level, left to right:

    index i -> left child = 2i + 1, right child = 2i + 2

Names used: first name CARL (second name Anderson is not included) + last name GILDO
Letters: C A R L G I L D O

                C
             /     \
           A         R
          / \       / \
         L   G     I   L
        / \
       D   O

Run it and just press Enter at both prompts to use Carl Gildo.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_tree(letters):
    """Create the binary tree from a list of letters (level order)."""
    if not letters:
        return None
    nodes = [Node(ch) for ch in letters]
    for i, node in enumerate(nodes):
        left, right = 2 * i + 1, 2 * i + 2
        if left < len(nodes):
            node.left = nodes[left]
        if right < len(nodes):
            node.right = nodes[right]
    return nodes[0]


def preorder(node, result=None):
    """Root -> Left -> Right"""
    if result is None:
        result = []
    if node:
        result.append(node.value)
        preorder(node.left, result)
        preorder(node.right, result)
    return result


def inorder(node, result=None):
    """Left -> Root -> Right"""
    if result is None:
        result = []
    if node:
        inorder(node.left, result)
        result.append(node.value)
        inorder(node.right, result)
    return result


def postorder(node, result=None):
    """Left -> Right -> Root"""
    if result is None:
        result = []
    if node:
        postorder(node.left, result)
        postorder(node.right, result)
        result.append(node.value)
    return result


def show(label, values):
    print(f"{label}: " + " -> ".join(values))


if __name__ == "__main__":
    first = input("Enter your first name (no second name) [Carl]: ").strip() or "Carl"
    last = input("Enter your last name [Gildo]: ").strip() or "Gildo"
    letters = list((first + last).upper().replace(" ", ""))
    print("Letters used:", " ".join(letters))

    root = build_tree(letters)
    show("Preorder  (Root-Left-Right)", preorder(root))
    show("Inorder   (Left-Root-Right)", inorder(root))
    show("Postorder (Left-Right-Root)", postorder(root))
