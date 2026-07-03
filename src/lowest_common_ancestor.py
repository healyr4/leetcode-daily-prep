# Given the root of a binary tree and two nodes, p and q, return their lowest common ancestor.
#
# The lowest common ancestor is the deepest node in the tree that has both p and q as descendants.
# A node can be a descendant of itself.
#
#         3
#        / \
#       5   1
#      / \ / \
#     6  2 0  8
#       / \
#      7   4
#
# Example:
#
# p = 7
# q = 4
#
# # Output: node 2
#
# Assumptions:
#
# This is a normal binary tree, not necessarily a binary search tree.
# Both p and q exist in the tree.
# Node values are unique.

class TreeNode:
    def __init__(self, value:int):
        self.value = value
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None

    def __repr__(self):
        return f"TreeNode({self.value})"


def setup_test_tree():
    nodes = {
        value: TreeNode(value) for value in [3,5,1,7,2,0,8,3,6,4]
    }
    root = nodes[3]
    root.left = nodes[5]
    root.right = nodes[1]

    nodes[5].left = nodes[6]
    nodes[5].right = nodes[2]

    nodes[1].left = nodes[0]
    nodes[1].right = nodes[8]

    nodes[2].left = nodes[7]
    nodes[2].right = nodes[4]

    return root, nodes

# def dfs(node: TreeNode | None):
#     if node is None:
#         return
#     print(node.value)
#     dfs(node.left)
#     dfs(node.right)

def find_path(node: TreeNode, target: TreeNode, path: list[TreeNode]):
    if node is None:
        return False
    # Include the node temporarily
    path.append(node)
    if node is target:
        return True

    if find_path(node.left, target, path):
        return True
    if find_path(node.right, target, path):
        return True

    # Target not in this branch, so backtrack
    path.pop()
    return False


    return False

def get_lca(root: TreeNode | None,  p: TreeNode, q: TreeNode):
    path_to_p: list[TreeNode] = []
    path_to_q: list[TreeNode] = []
    p_path = find_path(root, p, path_to_p)
    q_path = find_path(root, q, path_to_q)
    if not p_path or not q_path:
        return None
    return path_to_p, path_to_q

def main():
    p = 7
    q = 4

    root, nodes = setup_test_tree()
    p = nodes.get(p)
    q = nodes.get(q)
    p_path, q_path = get_lca(root, p, q)

    lowest_common_ancestor = None
    for p_node, q_node in zip(p_path, q_path):
        if p_node is not q_node:
            break
        lowest_common_ancestor = p_node

    print(lowest_common_ancestor.value)
    return lowest_common_ancestor


if __name__ == '__main__':
    main()

